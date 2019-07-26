import time


input("Press enter and count 10!")
start = time.time()


input("After you count 10, press enter again")
end = time.time()


et = end - start
print("Actual time:", et, "seconds")
print("Difference:", abs(et - 10), "seconds")
