from faker import Faker
from models import Band, Venue, Concert, band_venue
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///concert_info.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    import ipdb; ipdb.set_trace()