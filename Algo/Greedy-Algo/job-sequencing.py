class jobprofile:
    def __init__(self, jobID, deadline, profit):
        self.jobID = jobID
        self.deadline = deadline
        self.profit = profit

    def __lt__(self, other):
        return self.profit < other.profit


def printJobScheduling(arr, n):
    jobArray = []
    for i in range(len(arr)):
        jobArray.append(jobprofile(arr[i][0], arr[i][1], arr[i][2]))

    jobArray.sort(reverse=True)

    jobSlots = []
    for i in range(n):
        jobSlots.append([])

    for job in jobArray:
        i = job.deadline - 1
        while(i != -1):
            if(jobSlots[i] == []):
                jobSlots[i] = job
                break
            i -= 1

    for job in jobSlots:
        if(job != []):
            print(job.jobID, end=' ')


if __name__ == '__main__':
    arr = [['a', 4, 20],  # Job Array
           ['b', 1, 50],
           ['c', 1, 40],
           ['d', 1, 30]]

    # print("Following is maximum profit sequence of jobs")

    # Function Call
    printJobScheduling(arr, len(arr))
