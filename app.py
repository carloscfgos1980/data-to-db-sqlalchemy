from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Painting(Base):
    __tablename__ = "paintings"

    paint_id = Column("paint_id", Integer, primary_key=True)
    title = Column("title", String)
    tech = Column("tech", String)
    size = Column("size", String)
    price = Column("price", Integer)
    img = Column("img", String)
    reserved = Column("reserved", BOOLEAN)
    sold = Column("sold", BOOLEAN)

    def __init__(self, paint_id, title, tech, size, price, img, reserved, sold):
        self.paint_id = paint_id
        self.title = title
        self.tech = tech
        self.size = size
        self.price = price
        self.img = img
        self.reserved = reserved
        self.sold = sold

    def __repr__(self):
        return f"({self.paint_id}) {self.title} {self.tech} {self.size} ({self.price}) {self.img} {self.reserved} {self.sold})"


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column("customer_id", Integer, primary_key=True)
    paint = Column(Integer, ForeignKey("paintings.paint_id"))
    name = Column("name", String)
    last_name = Column("last_name", String)
    country = Column("country", String)
    email = Column("email", String)
    comment = Column("comment", String)

    def __init__(self, custumer_id, paint, name, last_name, country, email, comment):
        self.custumer_id = custumer_id
        self.paint = paint
        self.name = name
        self.last_name = last_name
        self.country = country
        self.email = email
        self.comment = comment

    def __repr__(self):
        return f"{self.customer_id} {self.paint} {self.name} {self.last_name} {self.country} {self.email} {self.comment}"


class Fan(Base):
    __tablename__ = "fans"

    customer_id = Column("customer_id", Integer, primary_key=True)
    name = Column("name", String)
    last_name = Column("last_name", String)
    country = Column("country", String)
    email = Column("email", String)
    comment = Column("comment", String)

    def __init__(self, custumer_id, name, last_name, country, email, comment):
        self.custumer_id = custumer_id
        self.name = name
        self.last_name = last_name
        self.country = country
        self.email = email
        self.comment = comment

    def __repr__(self):
        return f"{self.customer_id} {self.name} {self.last_name} {self.country} {self.email} {self.comment}"


engine = create_engine("sqlite:///amet.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# Update the data base
x1 = session.query(Painting).get(3)
x2 = session.query(Painting).get(4)
x3 = session.query(Painting).get(5)
x4 = session.query(Painting).get(6)

x1.img = "./images/paintings_available/gossip.jpg"
x2.img = "./images/paintings_available/burning.jpg"
x3.img = "./images/paintings_available/idolatry.jpg"
x4.img = "./images/paintings_available/bread-circus.jpg"
session.commit()

result = session.query(Painting).all()
print(result)

outcome = session.query(Painting).filter(Painting.title == 'Gossip')
for x in outcome:
    print(x)


more = session.query(Painting).filter(Painting.price >= 500)
for x in more:
    print(x)

# I can filter by just adding a combination of letter that will loop into the database and find the match. Example bellow
otherResult = session.query(Painting).filter(Painting.title.like("%elc%"))
for x in otherResult:
    print(x)

Checking = session.query(Painting).filter(
    Painting.title.in_(["Gossip", "Burning"]))
for x in Checking:
    print(x)

# print the objects to belon to the person and the person data with the folled example
print('Combining tables!')
xxx = session.query(Customer, Painting).filter(
    Customer.paint == Painting.paint_id).filter(Painting.title == "Cuban Party").all()

for r in xxx:
    print(r)
