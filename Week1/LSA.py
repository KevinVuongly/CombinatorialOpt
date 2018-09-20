import numpy as np
import time

def main():

    jobNumber = pickJob()

    with open("data/jobs" + str(jobNumber) + ".txt", "r") as file:
        jobs = file.readlines()

        for i in range(len(jobs)):
            jobs[i] = int(jobs[i].rstrip())

        numberOfMachines = pickMachines()

        machines = [0 for x in range(numberOfMachines)]

        tic = time.time()

        for i in range(len(jobs)):
            put = machines.index(min(machines))

            machines[put] += jobs[i]

        elapsed = time.time() - tic

    print("\nLongest machine is {} with duration {}.\n".format(machines.index(max(machines)), max(machines)))
    print("Elapsed time:", "%.6f" % float(elapsed))

def pickJob():
    x = input("Which job do you want to schedule? ")
    return int(x)

def pickMachines():
    x = input("How many identical machines do you want to use? ")
    return int(x)

if __name__ == "__main__":
    main()
