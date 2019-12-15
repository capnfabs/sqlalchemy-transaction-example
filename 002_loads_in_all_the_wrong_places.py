from dateutil import parser
from sqlalchemy import inspect

from models import Zebra
from utils import step, configure_logger, Session, silence

configure_logger()

with step():
    session = Session()
    # Grab any ol' Zebra
    zebra = session.query(Zebra).first()
    session.commit()

with step():
    print(f'Hello, {zebra.name}!')

# Don't show this
with silence():
    session.close()

# JUST FOR MY OWN VERIFICATION: What happens when you rollback?
with step():
    session = Session()
    # Grab any ol' Zebra
    print(session.query(Zebra).first())
    # Rollback instead of commit
    session.rollback()
    print(f'Hello, {zebra.name}!')

with step():
    session = Session()
    zebra = session.query(Zebra).first()
    print(f'Hello, {zebra.name}!')
    session.expunge(zebra)
    session.commit()
    print(f'{zebra.name}, are you still there?')


with step():
    assert inspect(zebra).detached
    zebra.number_of_stripes = 63
    session.commit()
    other_session = Session()
    # Reload the zebra in a different session
    zr = other_session.query(Zebra).filter(Zebra.id == zebra.id).one()
    print(f'{zr.name} has {zr.number_of_stripes} stripes')


with silence():
    session.close()
    other_session.close()

with step():
    session = Session()
    janet = Zebra(name='Janet', when_born=parser.parse('2018-06-05'))
    session.add(janet)
    session.flush()
    # ID should have been set when we flushed Janet to the database,
    # which indicates that she was correctly saved.
    assert janet.id
    session.expunge(janet)
    session.commit()
    print(f"Hi {janet.name}, we're glad you're still here!")

# NOTE rollback
with step():
    session = Session()
    [za, zb] = session.query(Zebra).limit(2)
    session.close()
    assert inspect(za).detached
    assert inspect(zb).detached
    print(f"Hi {za.name}, we're glad you're still here!")
    print(f"Hi {zb.name}, we're glad you're here too!")

# NOTE commit
with step():
    session = Session()
    [za, zb] = session.query(Zebra).limit(2)
    # Expunge one explicitly before session close
    session.expunge(za)
    # Or rollback, both have the same effect
    session.commit()
    session.close()
    # Should work, was detached before commit()
    print(f"Hi {za.name}, we're glad you're still here!")
    # Will raise, was detached after being expired
    print(f"Hi {zb.name}, we're glad you're here too!")

