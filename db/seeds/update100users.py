from database import SessionLocal
from models import User
import time

db = SessionLocal()


def updateUsers():
    start = time.perf_counter()
    items = db.query(User).all()
    for user in items:
        user.username = "delete"

    db.commit()
    end = time.perf_counter() - start
    print("end:{0}".format(end) + "[sec]")

updateUsers()