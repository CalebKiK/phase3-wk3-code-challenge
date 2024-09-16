import pytest
from models import Base, Band, Venue, Concert
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@pytest.fixture(scope='module')
def session():
    engine = create_engine('sqlite:///concert_info.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
    
    session.close()


def test_concert_band(session):
    concert = session.query(Concert).first()
    band = concert.band()
    assert isinstance(band, Band)
    assert band.name
    assert band.hometown 
    
def test_concert_venue(session):
    concert = session.query(Concert).first()
    venue = concert.venue()
    assert isinstance(venue, Venue)
    assert venue.title 
    assert venue.city
    
def test_venue_concerts(session):
    venue = session.query(Venue).first()
    concerts = venue.concerts()
    assert len(concerts) >= 1
    assert all(isinstance(concert, Concert) for concert in concerts)
    
def test_venue_bands(session):
    venue = session.query(Venue).first()
    bands = venue.all_bands
    assert len(bands) >= 1
    assert all(isinstance(band, Band) for band in bands)
    
def test_band_concerts(session):
    band = session.query(Band).first()
    concerts = band.concerts()
    assert len(concerts) >= 1
    assert all(isinstance(concert, Concert) for concert in concerts)
    
def test_band_venues(session):
    band = session.query(Band).first()
    venues = band.all_venues
    assert len(venues) >= 1
    assert all(isinstance(venue, Venue) for venue in venues)
    
def test_concert_hometown_show(session):
    concert = session.query(Concert).first()
    assert isinstance(concert.hometown_show(), bool)
    
def test_concert_introduction(session):
    concert = session.query(Concert).first()
    intro = concert.introduction()
    assert isinstance(intro, str)
    assert concert.band().name in intro
    assert concert.band().hometown in intro
    assert concert.venue().city in intro
    
def test_band_play_in_venue(session):
    band = session.query(Band).first()
    venue = session.query(Venue).first()
    band.play_in_venue(venue, "2023-09-15")
    concert = session.query(Concert).filter(Concert.date == "2023-09-15").first()
    assert concert is not None
    
def test_band_most_performances(session):
    most_performances_band = Band.most_performances()
    assert most_performances_band
    assert isinstance(most_performances_band, Band)
    assert most_performances_band.name
    
def test_venue_concert_on(session):
    venue = session.query(Venue).first()
    concert = venue.concert_on("2023-09-15")
    assert concert
    assert isinstance(concert, Concert)
    assert concert.band()
    assert concert.band().name
    
def test_venue_most_frequent_band(session):
    venue = session.query(Venue).first()
    band = venue.most_frequent_band()
    assert band is not None
    