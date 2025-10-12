import time
from threading import *

# It will become True when P ends
done = False


class Program(Thread):
    def run(self):
        while True:
            print("Still here")

        # This instruction is never reached since the previous condition is
        # always true and the loop will never end.
        done = True


class Checker(Thread):
    def run(self):
        print("Checking whether P ended or not")

        # Let's wait for 2 seconds
        waiting_period = 2
        # time.time() returns the current time
        time_started = time.time()

        while not done:
            # Return if we are out of time and P still didn't end
            if time.time() - time_started > waiting_period:
                print("P didn't finish, but I'm out of time")
                return

            # Otherwise print something just to see it working
            print("P is still not done")


# We need to run 2 programs at the same time:
# 1) the initial program P
# 2) the program that actually checks if P is over
#
# Threads are required to run the programs in parallel.
# For each function (1, 2) we create a class. To simulate the program we need
# to call the method start.

p = Program()
p.start()

q = Checker()
q.start()

q.join()
