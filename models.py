
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, Table
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///concert_info.db')
Session = sessionmaker(bind=engine)
session = Session()

# Band and Venue table object as an intermediary for the many to many relationship
band_venue = Table(
    'band_venues',
    Base.metadata,
    Column('id', Integer(), primary_key=True),
    Column('band_id', ForeignKey('bands.id')),
    Column('venue_id', ForeignKey('venues.id')),
    extend_existing=True,
)

# Band model to handle the band instances
class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    hometown = Column(String(), nullable=False)
    
    all_concerts = relationship('Concert', backref=backref('a_band'))
    all_venues = relationship("Venue", secondary=band_venue, back_populates='all_bands')
            
    def concerts(self):
        """Returns a collection of all concerts that the band has played"""
        return self.all_concerts
    
    def venues(self):
        """Returns a collection of all venues that the band has played"""
        return {concert.venue for concert in self.all_concerts}
    
    def play_in_venue(self, venue, date):
        """Creates a new concert for the band in that venue on the date"""
        if isinstance(venue, Venue) and isinstance(date, str):
            new_concert = Concert(band_id = self.id, venue_id = venue.id, date = date)
            session.add(new_concert)
            session.commit()
        else:
            raise Exception("Venue should be an instance in Venue and date should be a string")
        
    def all_introductions(self):
        """Returns an array of strings representing all the band's introductions"""
        return [concert.introduction() for concert in self.all_concerts]
    
    @classmethod
    def most_performances(cls):
        """Returns the band that has played the most concerts"""
        bands = session.query(Band).all()
        
        return max(bands, key=lambda band: len(band.all_concerts))
    
    def __repr__(self):
        return f"Band {self.id} " \
            + f"Name: {self.name}" \
            + f" Hometown: {self.hometown}"


# Venue model to handle the venue instances     
class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    city = Column(String(), nullable=False)
    
    all_concerts = relationship('Concert', backref=backref('a_venue'))
    all_bands = relationship('Band', secondary=band_venue, back_populates='all_venues')
            
    def concerts(self):
        """Returns a collection of all concerts from the venue"""
        return self.all_concerts
    
    def bands(self):
        """Returns a collection of all bands that performed at the venue"""
        return {concert.band for concert in self.all_concerts}
    
    def concert_on(self, date):
        """Returns the first concert on that date in that venue"""
        return session.query(Concert).filter_by(venue_id=self.id, date=date).first()
    
    def most_frequent_band(self):
        """Returns the band with the most concerts at the venue"""
        bands = [concert.band for concert in self.all_concerts]
        return max(bands, key=bands.count)
    
    def __repr__(self):
        return f"Venue {self.id} " \
            + f"Title: {self.title}" \
            + f" City: {self.city}"
    

# Concert model that provides the one to many relationship for both the Band and Venue model
class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    date = Column(String(), nullable=False)
    band_id = Column(Integer(), ForeignKey('bands.id'), nullable=False)
    venue_id = Column(Integer(), ForeignKey('venues.id'), nullable=False)
    
    def band(self):
        """Returns the Band instance for this concert"""
        return self.a_band
    
    def venue(self):
        """Returns the Venue instance for this concert"""
        return self.a_venue
    
    def hometown_show(self):
        """Returns true if the concert is in the band's hometown and false if not"""
        return self.a_band.hometown == self.a_venue.city
    
    def introduction(self):
        """Returns a string with the band's introduction to a concert"""
        return f"Hello {self.a_venue.city}!!!!! We are {self.a_band.name} and we're from {self.a_band.hometown}"
    
    def __repr__(self):
        return f"Concert {self.id} " \
            + f"Name: {self.name}" \
            + f" Date: {self.date}"
    