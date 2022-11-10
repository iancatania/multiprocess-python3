import multiprocessing as mp
import os
import random
import string
import numpy as np
import argparse


# generates list of strings to be called as UIDs and File names
def generate_list(n, isFileName=False):
    arr = np.empty(n, dtype=object)
    randlist = set()

    set_random = ''.join(np.random.choice(np.array(list(string.ascii_lowercase)), size=10))

    for i in range(len(arr)):

        while set_random in randlist:
            set_random = ''.join(np.random.choice(np.array(list(string.ascii_lowercase)), size=10))

        if isFileName:
            set_random += '.txt'

        arr[i] = set_random
        randlist.add(set_random)

    return arr


# runs client data command
def execute(Source, File, UID):
    for i in range(len(UID)):
        os.system(f'python3 cloud_client.py --UID \'{UID[i]}\' --File \'{File[i]}\' --Data \'{Source}\' ')


if __name__ == '__main__':

    cpus = mp.cpu_count()

    # checks for user input of number of processes and source of file using parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', required = True)
    parser.add_argument('--source', required = True)
    args = parser.parse_args()

    # assigns args to vars
    n = args.n
    source = args.source

    n = int(n)
    d = n // cpus

    # generates lists for uids and files
    UIDset = generate_list(n)
    fileset = generate_list(n, True)

    p1 = mp.Pool(cpus)

    # runs execution
    for i in range(cpus):
        x = fileset[i * d:(i + 1) * d]
        y = UIDset[i * d:(i + 1) * d]
        p1.apply_async(execute, args=(source, x, y))

    p1.close()
    p1.join()
