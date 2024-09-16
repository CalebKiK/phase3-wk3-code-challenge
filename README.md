- This phase 3 week 3 code challenge belongs to Caleb Karimi.

For this assignment, we'll be working with a Concert domain.

We have three models: Band(name and hometown),Venue(title and city), and Concert.

For our purposes, a Band has many Concerts, a Venue has many Concerts, 
and a Concert belongs to a Band and to a Venue.

Band - Venue is a many to many relationship.

Deliverables
Write the following methods in the classes you will write. Feel free to build out any helper methods if needed.

Remember: SQLAlchemy gives your classes access to a lot of methods already! Keep in mind what methods SQLAlchemy gives you access to on each of your classes when you're approaching the deliverables below.

Migrations
Before working on these deliverables, you will need to create migrations for the concerts  tables. This is assuming you had already created and migrated the band and venues table above.

A Concert belongs to a Band, and a Concert also belongs to a Venue. In your migration, create any columns your concerts table will need to establish these relationships.
The concerts table should also have:
A date column that stores an string.
After creating the concerts table using a migration, create instances of your classes so you can test your code.

Once you've set up your tables, work on building out the following deliverables.

 

Object Relationship Methods
Use SQLAlchemy query methods where appropriate.

Concert
Concert band()
should return the Band instance for this Concert
Concert venue()
should return the Venue instance for this Concert
Venue
Venue concerts()
returns a collection of all the concerts for the Venue
Venue bands()
returns a collection of all the bands who performed at the Venue
Band
Band concerts()
should return a collection of all the concerts that the Band has played
Band venues()
should return a collection of all the venues that the Band has performed at
 

Ensure these methods work before proceeding. For example, you should be able to call session. query(Band).first().venues and see a list of the venues for the first band in the database based on your test data, and session. query(Band).first() should return the band for the first concert in the database.

Aggregate and Relationship Methods
Concert
Concert hometown_show()
returns true if the concert is in the band's hometown, false if it is not
Concert introduction()
returns a string with the band's introduction for this concert
an introduction is in the form:
"Hello {insert venue city}!!!!! We are {insert band name} and we're from {insert band hometown}"

Band
Band play_in_venue(venue, date)
takes a venue (Venue instance) and date (as a string) as arguments
creates a new concert for the band in that venue on that date\
Band all_introductions()
returns an array of strings representing all the introductions for this band
each introduction is in the form:
"Hello {insert venue city}!!!!! We are {insert band name} and we're from {insert band hometown}"

Band most_performances() class method
returns the Band instance for the band that has played the most concerts
Note: solving this using only SQLAlchemy methods is possible, but difficult. Feel free to use regular Python enumerable methods here.
Venue
Venue concert_on(date)
takes a date (string) as an argument
finds and returns the first concert on that date at that venue
Venue most_frequent_band()
returns the band with the most concerts at the venue
Note: solving this using only SQLAlchemy methods is possible, but difficult. Feel free to use regular Python enumerable methods here.