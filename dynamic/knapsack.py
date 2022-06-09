from typing import List
from pprint import pprint
from collections import namedtuple


Job = namedtuple("Job", "profit, deadline")


def _allocate(job: Job, schedule: List[Job], jobs: List[Job]):
    attempt_index = job.deadline - 1
    while attempt_index > 0:
        if schedule[attempt_index] == 0:
            schedule[attempt_index] = jobs[attempt_index]  # fill slots
        else:
            attempt_index -= 1


"""
To prioritise the work we have to prioritise the work such that the 
most profitable is taken first. It has to be implemented the latest deadline permits.

Thus, the idea of the algorithm is create an empty array of slots and populate it 
starting with Deadline - 1, and go backwards until the beginning. If no slots left, repeat for the
other item.
"""
def sequence_for_max_profit(jobs: Job):
    schedule = [0] * 8
    for job in sorted(jobs, key=lambda job: job.profit):
        _allocate(job, schedule, jobs)
    return schedule


def main():
    jobs: Job = [  # definition
        Job(profit=5, deadline=1),
        Job(profit=2, deadline=2),
        Job(profit=3, deadline=3),
        Job(profit=1, deadline=1),
        Job(profit=15, deadline=1),
        Job(profit=15, deadline=4),
        Job(profit=15, deadline=7),
    ]
    allocations = sequence_for_max_profit(jobs)
    pprint(allocations)


if __name__ == "__main__":
    main()
