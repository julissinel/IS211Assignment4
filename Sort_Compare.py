import random
import decimal
import time

def generate_randoms (size):
    i = 0
    list_of_randoms = {}

    for _j in range(100):
        i +=1
        list_of_randoms [i] = random.sample(range(1,100000), size)
    return list_of_randoms

#Insertion Sort
def insertion_sort(list):
    start = time.time()
    for i in range(1, len(list)):
        current = list[i]
        pos = i
        while pos > 0 and list[pos - 1] > current:
            list[pos] = list[pos - 1]
            pos = pos - 1
        list[pos] = current
    stop = time.time()
    duration = stop - start
    return duration

def run_isort():
    generated_randoms = generate_randoms(500)
    duration_for_500 = 0
    for x in range(1,101):
        duration = insertion_sort(generated_randoms[x])
        duration_for_500 = duration_for_500 + duration

    average_for_500 = duration_for_500/x
    #for 1000
    generated_randoms = generate_randoms(1000)
    duration_for_1000 = 0
    for x in range(1,101):
        duration = insertion_sort(generated_randoms[x])
        duration_for_1000 = duration_for_1000 + duration

    average_for_1000 = duration_for_1000/x
    #for 100000
    generated_randoms = generate_randoms(10000)
    duration_for_10000 = 0
    for x in range(1,101):
        duration = insertion_sort(generated_randoms[x])
        duration_for_10000 = duration_for_10000 + duration

    average_for_10000 = duration_for_10000/x
    
    final_avg_is = decimal.Decimal(average_for_500 + average_for_1000 + average_for_10000)
    return (final_avg_is)

def shell_sort(list):
    start = time.time()
    sub_count = len(list) // 2
    while sub_count >0:
        for initial_pos in range(sub_count):
            gap_insertion(list,initial_pos,sub_count)
        sub_count = sub_count//2
    stop = time.time()
    duration = stop - start
    return duration
def gap_insertion(list,start,gap):
    for i in range(start+gap,len(list),gap):
        current = list[i]
        pos = i
    while pos >=gap and list[pos - gap] > current:
        list[pos] = list[pos - gap]
        pos = pos = gap
        list[pos] = current


def run_ssort():
    generated_randoms = generate_randoms(500)
    duration_for_500 = 0
    for x in range(1,101):
        duration = shell_sort(generated_randoms[x])
        duration_for_500 = duration_for_500 + duration
    average_for_500 = duration_for_500/x

    #for 1000
    generated_randoms = generate_randoms(1000)
    duration_for_1000 = 0
    for x in range(1,101):
        duration = shell_sort(generated_randoms[x])
        duration_for_1000 = duration_for_1000 + duration
    average_for_1000 = duration_for_1000/x

    #for 10000
    generated_randoms = generate_randoms(10000)
    duration_for_10000 = 0
    for x in range(1,101):
        duration = shell_sort(generated_randoms[x])
        duration_for_10000 = duration_for_10000 + duration
    average_for_10000 = duration_for_10000/x

    final_avg_ss = decimal.Decimal(average_for_500 + average_for_1000 + average_for_10000)
    return(final_avg_ss)

#Python Sort
def python_sort(list):
    start = time.time()
    list.sort()
    stop = time.time
    duration = stop - start
    return duration

def run_psort():
    generated_randoms = generate_randoms(500)
    duration_for_500 = 0
    for x in range(1,101):
        duration = python_sort(generated_randoms[x])
        duration_for_500 = duration_for_500 + duration
    average_for_500 = duration_for_500/x
    #for 1000
    generated_randoms = generate_randoms(1000)
    duration_for_1000 = 0
    for x in range(1,101):
        duration = python_sort(generated_randoms[x])
        duration_for_1000 = duration_for_1000 + duration
    average_for_1000 = duration_for_1000/x
    #for 100000
    generated_randoms = generate_randoms(10000)
    duration_for_10000 = 0
    for x in range(1,101):
        duration = python_sort(generated_randoms[x])
        duration_for_10000 = duration_for_10000 + duration
    average_for_10000 = duration_for_10000/x

    final_avg_ps = decimal.Decimal(average_for_500 + average_for_1000 + average_for_10000)
    return (final_avg_ps)

def main():
    sort1 = run_isort()
    print("Insertion Sort took {10.7f} seconds to run on average".format(sort1))
    sort2 = run_ssort()
    print("Shell sort took {10.7f} seconds to run on average".format(sort2))
    sort3 = run_psort()
    print("Python sort took {10.7f} seconds to run on average".format(sort3))

if __name__ == "__main__":
    main()
