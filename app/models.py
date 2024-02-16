from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, String, Column, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship


BASE = declarative_base()

engine = create_engine("sqlite:///restaurant.db")

restaurant_customer = Table(
    "restaurant_customers",
    BASE.metadata,
    Column('restaurant_id', ForeignKey("restaurants.id"), primary_key=True),
    Column("customer_id", ForeignKey("customers.id")),
    extend_existing=True
)


class Restaurant(BASE):
    __tablename__ = "restaurants"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())

    # print("xxxxxxxxxxxx")
    #one to many relationship: This is the parent
    reviews = relationship("Review", backref="restaurant", cascade=("all, delete"))
    # print("yyyyyyyyyy")
    customers = relationship("Customer", secondary=restaurant_customer, back_populates="restaurants")
    
# rs1 = Restaurant("kem",s

class Customer(BASE):
    __tablename__ = "customers"

    id = Column(Integer(), primary_key=True)
    first_name =Column(String())
    last_name = Column(String())

    #One-many relationship: parent to child accessed parent.children
    #children will take foreignkey
    reviews = relationship("Review", backref="customer", cascade=("all, delete"))
    restaurants = relationship("Restaurant", secondary= restaurant_customer, back_populates="customers")

class Review(BASE):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    comment = Column(String())
    star_rating = Column(Integer())

    #foreignKey assignment
    customer_id = Column(Integer(), ForeignKey("customers.id"))
    restaurant_id = Column(Integer(), ForeignKey("restaurants.id"))
    #inverse relationship
    # customer = relationship("Customer", backref="review", cascade=("all, delete"))
    #foreignKey assignment
    # restaurant_id = Column(Integer(), ForeignKey("customers.id"))
    #inverse relationship
    # restaurant = relationship("Restaurant", backref="review", cascade=("all, delete"))



