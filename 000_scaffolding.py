from dateutil import parser

import utils
from models import Zebra, Base, WateringHole
from utils import Session, now, DAY

Base.metadata.create_all(utils.engine)

session = Session()
session.add(Zebra(
    name='Stevie',
    when_born=parser.parse('2016-04-01')))

session.add(Zebra(
    name='Anya',
    when_born=parser.parse('2018-06-05'),
    number_of_stripes=73,
    when_stripes_counted=now() - 14*DAY))

session.add(WateringHole(
    name="Ol' Watering Hole",
    # There are no watering holes in Berlin but Weißensee is pretty cool
    latitude=52.554133,
    longitude=13.463599,
))

session.commit()
