from sqlalchemy import Column, String, Numeric, Integer
from database import Base

#This creates the database

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    price = Column(Numeric(10, 2))
    forward_pe = Column(Numeric(10, 2))
    forward_eps = Column(Numeric(10, 2))
    dividend_yield = Column(Numeric(10, 2))
    ma50 = Column(Numeric(10, 2))
    ma200 = Column(Numeric(10, 2))
    #five_year_return = Column(Numeric(10, 2))
    year_high = Column(Numeric(10, 2))
    short_ratio = Column(Numeric(10, 2))
    percent_decrease = Column(Numeric(10, 2))

    # email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)
