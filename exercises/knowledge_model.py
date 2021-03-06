from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'knowledge'
	food_id=Column(Integer, primary_key=True) 
	fave_food=Column(String)
	food_good=Column(String)
	rating=Column(Integer)
		
	def __repr__(self):
		return (
               "Fave Food: {} \n"
               "Food Good: {} \n"
               "rating: {}").format(
                    self.fave_food, self.food_good, self.rating)
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	pass
x = Knowledge(fave_food="fries", food_good="ran article", rating="10")