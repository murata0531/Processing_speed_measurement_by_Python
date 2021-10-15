import time

def Measure(repeat_cnt,principal,goal):
    for i in range(repeat_cnt):
        age_cnt = 0
        inner_principal = principal
        while True:
            inner_principal = inner_principal * 1.05
            age_cnt += 1
            if inner_principal >= goal:
                print(inner_principal)
                print(age_cnt)
                break

repeat_cnt = int(input("繰り返し回数:"))
principal = int(input("元本:"))
goal = int(input("目標金額:"))

start = time.perf_counter()
Measure(repeat_cnt,principal,goal)
end = time.perf_counter() - start

print("end:{0}".format(end) + "[sec]")

