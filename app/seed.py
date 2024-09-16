#!/usr/bin/env python3

from faker import Faker
from models import Base, Band, Venue, Concert
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///concert_info.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    Base.metadata.create_all(engine)
    
    session.query(Band).delete()
    session.query(Venue).delete()
    session.query(Concert).delete()
    session.commit()
    
    print("Seeding data...")
    
    coldplay = Band(name="Coldplay", hometown="London")
    sauti_sol= Band(name="Sauti Sol", hometown="Nairobi")
    migos = Band(name="Migos", hometown="Georgia")
    maroon_5 = Band(name="Maroon 5", hometown="Los Angeles")
    the_beatles = Band(name="The Beatles", hometown="Liverpool")
    
    uhuru_gardens = Venue(title="Uhuru Gardens", city="Nairobi")
    greek_theatre = Venue(title="Greek Theatre", city="Los Angeles")
    bk_arena = Venue(title="BK Arena", city="Kigali")
    wembley = Venue(title="Wembley stadium", city="London")
    
    blankets_and_wine = Concert(name="Blankets and wines", date=fake.date(), band_id=1, venue_id=3)
    coachella = Concert(name="Coachella", date=fake.date(), band_id=3, venue_id=4)
    sol_fest = Concert(name="Sol Fest", date=fake.date(), band_id=2, venue_id=1)
    superbowl = Concert(name="Superbowl Halftime", date=fake.date(), band_id=4, venue_id=2)
    
    
    session.bulk_save_objects([coldplay, sauti_sol, uhuru_gardens, migos, maroon_5, the_beatles, greek_theatre, bk_arena, wembley, coachella, sol_fest, superbowl, blankets_and_wine])
    
    session.commit()
    session.close()
    
    print("Data seeded successfully")