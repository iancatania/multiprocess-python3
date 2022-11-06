import multiprocessing as mp
import numpy as np
import time


result_list = []
def result_action(result):
    result_list.append(result)

def square(x):
    return x*x

if __name__ == '__main__':
    cpus = 4
    n = 100
    d = n//cpus
    X = np.asarray(np.random.random(n)*n+1,dtype=int)
    p1 = mp.Pool(cpus)
    for i in range(cpus):
        x = X[i*d:(i+1)*d]
        p1.apply_async(square,args=(x,),callback=result_action)
    p1.close()
    p1.join()

    Y = []
    for result in result_list:
        Y += list(result)
    Y = np.array(Y)
    print(X)
    print(Y)