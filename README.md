https://www.alixaprodev.com/2022/04/convert-excel-to-database-in-python.html

* demo.py
Use <sqlite3> to convert .xlsx to SQL


* check.py to fill a ORM (SQL) to an existance databe

# Bug
xxx = session.query(Customer, Painting).filter(
    Customer.paint == Painting.paint_id).filter(Painting.title == "Gossip").all()

for r in xxx:
    print(r)

* It does not resolve this. I don't know why