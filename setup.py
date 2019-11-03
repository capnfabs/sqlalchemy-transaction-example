import os

from sqlalchemy import create_engine

import models


def setup():
    engine = create_engine(os.environ['DATABASE_URL'], echo=True)
    models.Base.metadata.create_all(engine)


if __name__ == '__main__':
    setup()