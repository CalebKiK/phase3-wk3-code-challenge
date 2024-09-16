import pytest
from models import Band, Venue, Concert
from seed import session


def test_concert_band(session):
    concert = session.query(Concert).first()
    band = concert.band()
    assert band.name == "The Rolling Stones"
    assert band.hometown == "London"
    
def test_concert_venue(session):
    concert = session.query(Concert).first()
    venue = concert.venue()
    assert venue.title == "Nyayo Stadium"
    assert venue.city =="Nairobi"
    
def test_venue_concerts(session):
    venue = session.query(Venue).filter_by(title="Nyayo Stadium").first()
    concerts = venue.concerts()
    assert len(concerts) == 2



