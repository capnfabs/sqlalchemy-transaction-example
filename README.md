# How does SQLAlchemy Manage Database Transactions?

Probably not a question that everyone's asking, but certainly a question that I was asking in September 2019. This is an example repo corresponding to the exploration I did for [this article](https://capnfabs.net/posts/sqlalchemy-connection-management/).

## How to run:

- Install [`pipenv`](https://pipenv.readthedocs.io/en/latest/)
- Clone this repo
- `pipenv install`
- Ensure you've got a Postgres database called `sqlalchemy_example` that can be accessed with your default account credentials (i.e. run `createdb sqlalchemy_example`).

Then, you can run `pipenv run python [filename]` to run a file from the repo.

## Here's what's in each of the files:

- `000_scaffolding.py` -- getting the data for the examples set up (adding Zebras, Waterholes, etc)
- `001_rollback_and_commit.py` -- the basic intro, corresponds to the 'Digging In' section in the article
- `002_loads_in_all_the_wrong_places.py` -- corresponds to the 'Finding loads in all the wrong places' section. 
