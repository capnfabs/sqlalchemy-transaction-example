import os

import sqlalchemy
from sqlalchemy import orm

from models import Zebra, WateringHole
from utils import now, YEAR, step, configure_logger

# Comment out these instructions because once you use echo=True once it wrecks
# it for everyone and we can't use our custom logger.
"""
    # Configure a connection to the database at the URL specified by the
    # DATABASE_URL environment variable.
    # Remember that we're using `echo=True` so we can see all generated SQL.
    engine = sqlalchemy.create_engine(os.environ['DATABASE_URL'], echo=True)

    # Create a session factory. Calling `Session()` will create new SQLAlchemy
    # ORM sessions.
    Session = orm.sessionmaker(bind=engine)

    # Create a new session which we'll use for the following investigation.
    session = Session()
"""

with step():
    configure_logger()
    engine = sqlalchemy.create_engine(os.environ['DATABASE_URL'])
    Session = orm.sessionmaker(bind=engine)
    session = Session()

with step():
    q = session.query(Zebra).filter(Zebra.when_born <= now() - 2*YEAR)
    old_zebra = q.first()

with step():
    wh = session.query(WateringHole).first()

with step():
    session.rollback()

# Commit instead
with step():
    session = Session()
    # Grab any ol' Zebra
    print(session.query(Zebra).first())
    session.commit()
