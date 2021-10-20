import time
pi4 = 0
start = time.perf_counter()
for i in range(100000000):
    pi4 += (1 / (i * 4 + 1) - 1 / (i * 4 + 3))

end = time.perf_counter() - start

print("end:{0}".format(end) + "[sec]")
print(pi4 * 4)