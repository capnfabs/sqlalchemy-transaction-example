import datetime
import os
import subprocess
import traceback
from contextlib import contextmanager

import sqlalchemy
from sqlalchemy import orm

now = datetime.datetime.now
DAY = datetime.timedelta(days=1)
YEAR = datetime.timedelta(days=365)

SQL = '''
SELECT
    backend_start,
    xact_start,
    query_start,
    state_change,
    state,
    substring(query for 50) AS query
FROM pg_stat_activity
WHERE backend_type = 'client backend' AND pid != pg_backend_pid();
'''

engine = sqlalchemy.create_engine(os.environ['DATABASE_URL'])
Session = orm.sessionmaker(bind=engine)

@contextmanager
def step():
    def header(text):
        print(f'\033[91m{text}\033[00m')
    header('Log output:')
    print('```')
    try:
        yield
    except:
        traceback.print_exc()
    print('```')

    header('sql')
    print('```')
    subprocess.run(['psql', 'sqlalchemy_example', '-x', '-c', SQL])
    print('```\n\n\n')

@contextmanager
def silence():
    """Use this for steps that won't be shown to the user"""
    import logging
    logger = logging.getLogger('sqlalchemy.engine')
    level = logger.level
    logger.setLevel(logging.WARNING)
    try:
        yield
    finally:
        logger.setLevel(level)


def configure_logger():
    import logging
    import sys
    sql_output = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter('%(message)s')
    sql_output.setFormatter(formatter)

    sql_logger = logging.getLogger('sqlalchemy.engine')
    sql_logger.addHandler(sql_output)
    sql_logger.setLevel(logging.INFO)
