import random
import time
import decimal

def generate_randoms (size):
    i = 0
    list_of_values = {}
    for j in range(100):
        i += 1
        list_of_values[i] = random.sample(range(1,100000),size)

    return list_of_values

def sequential_search(list,value):
    k = 0
    found = False
    start = time.time()
    while k < len(list) and found is False:
        if list[k] == value:
            found = True
        else:
            k += 1
    stop = time.time()
    duration = stop - start
    return duration, found

def run_sequential_search():
    generated_randoms = generate_randoms(500)
    duration_for_500 = 0
    for x in range(1,101):
        duration, value = sequential_search(generated_randoms[x],-1)
        duration_for_500 = duration_for_500 + duration
    average_duration_500 = duration_for_500/x
    
    #now for 1000
    generated_randoms = generate_randoms(1000)
    duration_for_1000 = 0
    for x in range(1,101):
        duration, value = sequential_search(generated_randoms[x],-1)
        duration_for_1000 = duration_for_1000 + duration
    average_duration_1000 = duration_for_1000/x

     #now for 1000
    generated_randoms = generate_randoms(10000)
    duration_for_10000 = 0
    for x in range(1,101):
        duration,value = sequential_search(generated_randoms[x],-1)
        duration_for_10000 = duration_for_10000 + duration
    average_duration_10000 = duration_for_10000/x

    final_avg_sequential = decimal.Decimal(average_duration_500 + average_duration_1000 + average_duration_10000)

    return final_avg_sequential


#Ordered Sequential Search

def ordered_sequential_search(list,value):
    i = 0
    found = False
    start = time.time()
    while i < len(list) and found is False:
        if list[i] == value:
            found = True
        else:
            i = i+1
    stop = time.time()
    duration = stop - start
    return duration, found

def run_ordered_seq_search():
    generated_randoms = generate_randoms(500)
    duration_for_500 = 0
    for x in range(1,101):
        generated_randoms[x].sort()
        duration,value = ordered_sequential_search(generated_randoms[x],-1)
        duration_for_500 = duration_for_500 + duration
    average_duration_500 = duration_for_500/x
    #1000
    generated_randoms = generate_randoms(1000)
    duration_for_1000 = 0
    for x in range(1,101):
        generated_randoms[x].sort()
        duration,value = ordered_sequential_search(generated_randoms[x],-1)
        duration_for_1000 = duration_for_1000 + duration
    average_duration_1000 = duration_for_1000/x
    #10000
    generated_randoms = generate_randoms(10000)
    duration_for_10000 = 0
    for x in range(1,101):
        generated_randoms[x].sort()
        duration,value = ordered_sequential_search(generated_randoms[x],-1)
        duration_for_10000 = duration_for_10000 + duration
    average_duration_10000 = duration_for_10000/x

    final_avg_ord_seq = decimal.Decimal(average_duration_500 + average_duration_1000 + average_duration_10000)
    return final_avg_ord_seq

#Binary iterative Search
def binary_search_iterative(list, value):
    first = 0
    last = len(list) - 1
    found = False
    start = time.time()
    while first <= last and found is False:
        mid = (first + last) // 2
        if list[mid] == value:
            found = True
        else:
            if value < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    stop = time.time()
    duration = stop - start
    return duration, found


def run_binary_iterative():
    generated_randoms = generate_randoms(500)
    duration_for_500 = 0
    for x in range(1,101):
        generated_randoms[x].sort()
        duration,value = binary_search_iterative(generated_randoms[x],-1)
        duration_for_500 = duration_for_500 + duration
    average_duration_500 = duration_for_500/x

    generated_randoms = generate_randoms(1000)
    duration_for_1000 = 0
    for x in range(1,101):
        generated_randoms[x].sort()
        duration,value = binary_search_iterative(generated_randoms[x],-1)
        duration_for_1000 = duration_for_1000 + duration
    average_duration_1000 = duration_for_1000/x

    generated_randoms = generate_randoms(10000)
    duration_for_10000 = 0
    for x in range(1,101):
        generated_randoms[x].sort()
        duration,value = binary_search_iterative(generated_randoms[x],-1)
        duration_for_10000 = duration_for_10000 + duration
    average_duration_10000 = duration_for_10000/x

    final_bin_iter = decimal.Decimal(average_duration_500 + average_duration_1000 + average_duration_10000)
    return final_bin_iter

#binary recursive search
def binary_search_recursive(list,value):
    found = False
    start = time.time()
    if len(list) == 0:
        found = False
    else:
        mid = len(list)//2
        if list[mid] == value:
            found = True
        else:
            if value < list[mid]:
                duration,found = binary_search_recursive(list[:mid],value)
            else:
                duration,found = binary_search_recursive(list[mid+1:],value)
    stop = time.time()
    duration = stop - start
    return duration,found
    
def run_binary_recursive():
    generated_randoms = generate_randoms(500)
    duration_for_500 = 0
    for x in range(1,101):
        generated_randoms[x].sort()
        duration,value = binary_search_recursive(generated_randoms[x],-1)
        duration_for_500 = duration_for_500 + duration

    average_duration_500 = duration_for_500/x

    generated_randoms = generate_randoms(1000)
    duration_for_1000 = 0
    for x in range(1,101):
        generated_randoms[x].sort()
        duration,value = binary_search_recursive(generated_randoms[x],-1)
        duration_for_1000 = duration_for_1000 + duration

    average_duration_1000 = duration_for_1000/x

    generated_randoms = generate_randoms(10000)
    duration_for_10000 = 0
    for x in range(1,101):
        generated_randoms[x].sort()
        duration,value = binary_search_recursive(generated_randoms[x],-1)
        duration_for_10000 = duration_for_10000 + duration

    average_duration_10000 = duration_for_10000/x

    final_avg_bin_rec = decimal.Decimal(average_duration_500 + average_duration_1000 + average_duration_10000)
    return (final_avg_bin_rec)


def main():

    seq_1 = run_sequential_search()
    print ("Sequential Search took {0:10.7f} seconds to run, on average".format(seq_1))

    seq_2 = run_ordered_seq_search()
    print ("Ordered Sequential Search took {0:10.7f} seconds to run, on average".format(seq_2))

    seq_3 = run_binary_iterative()
    print ("Iterative Binary Search took {0:10.7f} seconds to run, on average".format(seq_3, 3))

    seq_4 = run_binary_recursive()
    print ("Recursive Binary Search took {0:10.7f} seconds to run, on average".format(seq_4))




if __name__ == "__main__":
    main()