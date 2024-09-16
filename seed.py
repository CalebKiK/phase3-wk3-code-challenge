#!/usr/bin/env python3

from faker import Faker
from models import Base, Band, Venue, Concert, band_venue
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///concert_info.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    Base.metadata.create_all(engine)
    
    # Initially clear the various tables before seeding the data to avoid duplicates
    session.query(Band).delete()
    session.query(Venue).delete()
    session.query(Concert).delete()
    session.execute(band_venue.delete())
    session.commit()
    
    # Communicating to the user that seeding in in progress
    print("Seeding data...")
    
    # Seeding of Band data to ensure the models function appropriately
    coldplay = Band(name="Coldplay", hometown="London")
    sauti_sol= Band(name="Sauti Sol", hometown="Nairobi")
    migos = Band(name="Migos", hometown="Georgia")
    maroon_5 = Band(name="Maroon 5", hometown="Los Angeles")
    the_beatles = Band(name="The Beatles", hometown="Liverpool")
    
    # Saving Band data to the database
    session.add_all([coldplay, sauti_sol, migos, maroon_5, the_beatles])
    
    # Seeding of Venue data to ensure the models function appropriately
    uhuru_gardens = Venue(title="Uhuru Gardens", city="Nairobi")
    greek_theatre = Venue(title="Greek Theatre", city="Los Angeles")
    bk_arena = Venue(title="BK Arena", city="Kigali")
    wembley = Venue(title="Wembley stadium", city="London")
    
    # Saving Venue data to the database
    session.add_all([uhuru_gardens, greek_theatre, bk_arena, wembley])
    session.commit()
    
    # Seeding of Concert data to ensure the models function appropriately
    blankets_and_wine = Concert(name="Blankets and wines", date=fake.date(), band_id=1, venue_id=3)
    coachella = Concert(name="Coachella", date=fake.date(), band_id=3, venue_id=4)
    sol_fest = Concert(name="Sol Fest", date=fake.date(), band_id=2, venue_id=1)
    superbowl = Concert(name="Superbowl Halftime", date=fake.date(), band_id=4, venue_id=2)

    # Saving Concert data to the database
    session.add(coachella)
    session.add(sol_fest)
    session.add(superbowl)
    session.add(blankets_and_wine)
    session.commit()
    
    # Adding data to the table object
    coldplay.all_venues.append(bk_arena)
    sauti_sol.all_venues.append(uhuru_gardens)
    migos.all_venues.append(wembley)
    maroon_5.all_venues.append(greek_theatre)
    coldplay.all_venues.append(wembley)
    the_beatles.all_venues.append(greek_theatre)
    maroon_5.all_venues.append(uhuru_gardens)
    coldplay.all_venues.append(uhuru_gardens)
    
    session.commit()
    session.close()
    
    # Communicating that the seeding was completed successfully
    print("Data seeded successfully")