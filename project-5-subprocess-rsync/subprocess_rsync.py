#!/usr/bin/env python
from multiprocessing import Pool
import subprocess
import os

src="/home/somak/python_practice/troubleshooting_exer/data/prod/"
dest="/home/somak//python_practice/troubleshooting_exer/data/prod_backup/"

#subprocess.call(["rsync", "-arq", src, dest])

def run(task):
  # Do something with task here
    for root, dir, files in os.walk(src):
        subprocess.call(["rsync", "-arq", src, dest])


if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)
