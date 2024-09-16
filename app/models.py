
from sqlalchemy import create_engine
from sqlalchemy import (Column, Integer, String, ForeignKey)
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///concert_info.db')
Session = sessionmaker(bind=engine)
session = Session()

class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    hometown = Column(String(), nullable=False)
    
    concerts = relationship('Concert', back_populates='band')
    venues = relationship("Venue", back_populates='band')
    
    def __repr__(self):
        return f"Band {self.id}: " \
            + f"Name: {self.name}" \
            + f"Hometown: {self.hometown}"
            
    def concerts(self):
        """Returns a collection of all concerts that the band has played"""
        return self.concerts
    
    def venues(self):
        """Returns a collection of all venues that the band has played"""
        return {concert.venue for concert in self.concerts}
    
    def play_in_venue(self, venue, date):
        """Creates a new concert for the band in that venue on the date"""
        if isinstance(venue, Venue) and isinstance(date, str):
            new_concert = Concert(band_id = self.id, venue_id = venue.id, date = date)
            session.add(new_concert)
            session.commit()
        else:
            raise Exception("Venue should be an instance in Venue and date should be a string")
        
    def all_introductions(self):
        """Returns an array of strings representing all introductions"""
        return [concert.introduction() for concert in self.concerts]
    
    def all_introductions(self):
        """Returns a string with the band's introduction to a concert"""
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
    
    @classmethod
    def most_performances(cls):
        """Returns the band that has played the most concerts"""
        bands = session.query(Band).all()
        
        return max(bands, key=lambda band: len(band.concerts))
        
        
class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    city = Column(String(), nullable=False)
    
    concerts = relationship('Concert', back_populates='venue')
    bands = relationship('Band', back_populates='venue')
    
    def __repr__(self):
        return f"Venue {self.id}: " \
            + f"Title: {self.title}" \
            + f"City: {self.city}"
            
    def concerts(self):
        """Returns a collection of all concerts from the venue"""
        return self.concerts
    
    def bands(self):
        """Returns a collection of all bands that performed at the venue"""
        return {concert.band for concert in self.concerts}
    
    def concert_on(self, date):
        """Returns the first concert on that date in that venue"""
        return session.query(Concert).filter_by(venue_id=self.id, date=date).first()
    
    def most_frequent_band(self):
        """Returns the band with the most cincerts at the venue"""
        bands = [concert.band for concert in self.concerts]
        return max(bands, key=bands.count)
    

class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    date = Column(String(), nullable=False)
    band_id = Column(Integer(), ForeignKey('bands.id'), nullable=False)
    venue_id = Column(Integer(), ForeignKey('venues.id'), nullable=False)
    
    def band(self):
        """Returns the Band instance for this concert"""
        return self.band
    
    def venue(self):
        """Returns the Venue instance for this concert"""
        return self.venue
    
    def hometown_show(self):
        """Returns true if the concert is in the band's hometown and false if not"""
        return self.band.hometown == self.venue.city
    
    def introduction(self):
        """Returns a string with the band's introduction to a concert"""
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
    