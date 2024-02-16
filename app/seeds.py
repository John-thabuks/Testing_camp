from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Review, Restaurant, Customer
import ipdb

fake = Faker()

if __name__ == "__main__":
    engine = create_engine("sqlite:///restaurant.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    # session.query(Review).delete() #clear table
    print("before")

    ipdb.set_trace()

    customer = [Customer(
        first_name= fake.name(),
        last_name= fake.name()
    ) for _ in range(50)]

    restaurant = [Restaurant(
        name= fake.name(),
        price = random.randint(100, 3500)
    ) for _ in range(50)]

    review = [Review(
        star_rating = random.randint(1,6),
        comment = fake.sentence(),
        customer_id = i,
        restaurant_id= i
    ) for i in range(50)]
    print("After")
    # session.query(review).delete() #clear table
    session.add_all(customer)
    session.commit()

    session.add_all(restaurant)
    session.commit()

    session.add_all(review)
    session.commit()

    print("start test")
    review1 = session.query(Review).get(1)
    print(review1)
    print("Done")