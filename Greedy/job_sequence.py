"""
Given an array of jobs where every job has a deadline and an associated profit if the job is finished before the deadline.
It is also given that every job takes a single unit of time to finish, so the minimum possible deadline for any job is 1.
How to maximize the profit if only one job can be scheduled at a time.
"""

class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

    def __lt__(self, other):
        return self.profit > other.profit

"""
Job: (id, deadline, profit)
"""
def jobSequence(jobs):
    jobArr = []
    for id, deadline, profit in jobs:
        job = Job(id, deadline, profit)
        jobArr.append(job)

    #Sort the job array
    jobArr.sort()

    #Try to maximize the profit
    result = ["#"] * len(jobs)
    availability = [True] * len(jobs)
    for job in jobArr:
        id, deadline = job.id, job.deadline
        while deadline >= 1 and not availability[deadline-1]:
            deadline -= 1
        if deadline >= 1:
            result[deadline-1] = id
            availability[deadline-1] = False
    return result

if __name__ == '__main__':
    jobs = [('A', 1, 100), ('B', 1, 19), ('C', 1, 27), ('D', 3, 25), ('E', 5, 15)]
    print(jobSequence(jobs))