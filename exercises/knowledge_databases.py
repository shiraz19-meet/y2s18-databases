from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(fave_food, food_good, rating):
	knowledge_object= Knowledge(
		fave_food = fave_food,
		food_good = food_good,
		rating = rating)
	session.add(knowledge_object)
	session.commit()



	

def query_all_articles():
	article = session.query(
	 	Knowledge).all()
	return article

def query_article_by_topic(fave_food):
	article = session.query(
		Knowledge).filter_by(
		fave_food=fave_food).all()
	return article

def delete_article_by_topic(fave_food):
	session.query(Knowledge).filter_by(
		fave_food=fave_food).delete()
	session.commit()
#delete_article_by_topic("fries")

def delete_all_articles():
	session.query(Knowledge).filter_by().delete()
	session.commit()
	return article

def query_article_by_topic(fave_food):
	article = session.query(
		Knowledge).filter_by(
		fave_food=fave_food).all()
	return article

def edit_article_rating(new_rate, topic):
	article_title=input("rate the article")
	updated_rate=input("update the rating")
	add_article_object = session.query(
	Knowledge).filter_by(
	rate=new_rate).first()
	Knowledge_object.rating = new_rating
	session.commit()
#edit_article_rating(2)
#query_all()

add_article("Food Good", "Spaghetti", 4)
# edit_article_rating(2, "food_good")
print(query_all_articles())