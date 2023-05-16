from main import engine, Record,Session

session = Session(bind = engine)

print(session.query(Record).all())