from database import SessionLocal
from models import User
import time

db = SessionLocal()


def deleteUsers():
    start = time.perf_counter()
    items = db.query(User).delete()
    db.commit()
    print(items)
    end = time.perf_counter() - start
    print("end:{0}".format(end) + "[sec]")

deleteUsers()
