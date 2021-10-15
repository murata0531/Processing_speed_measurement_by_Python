from database import SessionLocal
from models import User
import time

db = SessionLocal()


def seed():
    start = time.perf_counter()
    for i in range(100):
        user = User(username='user'+ str(i))
        db.add(user)
    db.commit()
    end = time.perf_counter() - start
    print("end:{0}".format(end) + "[sec]")

if __name__ == '__main__':
    BOS = '\033[92m'  # 緑色表示用
    EOS = '\033[0m'

    print(f'{BOS}Seeding data...{EOS}')
    seed()