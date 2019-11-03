import datetime
import os

import sqlalchemy
from dateutil import parser
from sqlalchemy import orm

from models import Zebra


def _configure_logger():
    import logging
    import sys
    sql_output = logging.StreamHandler(sys.stdout)

    # Print SQL in red
    formatter = logging.Formatter('\033[91m%(message)s\033[00m')
    sql_output.setFormatter(formatter)

    sql_logger = logging.getLogger('sqlalchemy.engine')
    sql_logger.addHandler(sql_output)
    sql_logger.setLevel(logging.INFO)


engine = sqlalchemy.create_engine(os.environ['DATABASE_URL'])
Session = orm.sessionmaker(bind=engine)
_configure_logger()

now = datetime.datetime.now
YEAR = datetime.timedelta(days=365)

def add_zebras():
    session = Session()
    session.add(Zebra(name='Stevie', when_born=parser.parse('2013-04-02')))
    session.add(Zebra(
        name='Anya',
        when_born=parser.parse('2012-04-02'),
        when_stripes_counted=parser.parse('2015-07-31'),
        number_of_stripes=74,
    ))
    session.commit()
    session.close()


def zebra_lookup():
    # Find all Zebras older than 2 years
    session = Session()
    q = session.query(Zebra).filter(Zebra.when_born <= now() - 2 * YEAR)
    zebras = q.all()
    print(zebras)
    session.close()
