class Activity:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __lt__(self, other):
        return self.finish < other.finish


def printMaxActivities(start, finish):
    activities = []
    n = len(finish)

    for i in range(n):
        activities.append(Activity(start[i], finish[i]))

    activities.sort()

    prevFinish = activities[0].finish
    s = "({}:{})"
    print(s.format(activities[0].start, activities[0].finish), end=' ')
    for j in range(n):
        if(activities[j].start >= prevFinish):
            print(s.format(activities[j].start, activities[j].finish), end=' ')
            prevFinish = activities[j].finish


if __name__ == '__main__':
    start = [5, 1, 3, 0, 5, 8]
    finish = [9, 2, 4, 6, 7, 9]
    printMaxActivities(start, finish)
