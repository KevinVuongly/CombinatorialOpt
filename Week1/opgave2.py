def main():

    jobNumber = pickJob()

    with open("data/jobs" + str(jobNumber) + ".txt", "r") as file:
        jobs = file.readlines()

        for i in range(len(jobs)):
            jobs[i] = int(jobs[i].rstrip())

        numberOfMachines = pickMachines()

        machines = [[] for x in range(numberOfMachines)]
        jobsInMachine = []

        for i in range(len(jobs)):
            if sum(machines[0]) <= sum(machines[1]):
                machines[0].append(jobs[i])
                jobsInMachine.append(0)
            else:
                machines[1].append(jobs[i])
                jobsInMachine.append(1)

    for i in range(len(machines)):
        print(sum(machines[i]))

    print(jobsInMachine)

def pickJob():
    x = input("Which job do you want to schedule? ")
    return x

def pickMachines():
    x = input("How many identical machines do you want to use? ")

    return x

if __name__ == "__main__":
    main()
