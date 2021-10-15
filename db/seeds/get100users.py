from database import SessionLocal
from models import User
import time

db = SessionLocal()


def getUsers():
    start = time.perf_counter()
    items = db.query(User).all()
    for user in items:
        print(user.username)
    end = time.perf_counter() - start
    print("end:{0}".format(end) + "[sec]")

getUsers()