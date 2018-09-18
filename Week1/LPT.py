import numpy as np

def main():

    jobNumber = pickJob()

    with open("data/jobs" + str(jobNumber) + ".txt", "r") as file:
        jobs = file.readlines()

        for i in range(len(jobs)):
            jobs[i] = int(jobs[i].rstrip())

        jobs.sort(reverse=True)

        numberOfMachines = pickMachines()

        machines = [[] for x in range(numberOfMachines)]
        timeSumMachines = [0 for x in range(numberOfMachines)]
        jobsInMachine = []

        for i in range(len(jobs)):
            put = timeSumMachines.index(min(timeSumMachines))

            machines[put].append(jobs[i])
            jobsInMachine.append(put)
            timeSumMachines[put] = sum(machines[put])

    for i in range(len(machines)):
        print("Timetable of machine {} is {}".format(i, machines[i]))

    positionJob = [[] for x in range(len(jobs))]

    for i in range(len(jobs)):
        positionJob[i].append(jobs[i])
        positionJob[i].append(jobsInMachine[i])

    print("\nJobs are in:\n{}".format(np.matrix(positionJob)))

    print("\nLongest machine is {} with duration {}.\n".format(machines.index(max(machines)), sum(max(machines))))

def pickJob():
    x = input("Which job do you want to schedule? ")
    return x

def pickMachines():
    x = input("How many identical machines do you want to use? ")

    return x

if __name__ == "__main__":
    main()
