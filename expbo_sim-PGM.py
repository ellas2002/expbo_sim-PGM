#Ella Stiller
import numpy as np
import matplotlib.pyplot as plt
import random

"global variables BECAUSE they are constant :)"
sample_size = 1000 #the number trials to run to compute expected values
max_k = 14
max_b = 4
max_w = pow(2, max_b) #maximum backoff window size (== 2^max_b).



"function for the main part of the simulation"
def try_time_slot(k):
    b = [0 for _ in range(k)]
    rounds = 0

    while True:
        slots = []

        for i in range(k):
            b_i = min(b[i], max_b)
            time = random.randint(1, pow(2, b_i))
            slots.append(time)

        if slots.count(1) == 1: #if there is only one sender with 1 "success"
            #print(f"Success! Round {rounds + 1}")
            #print(slots)
            return rounds + 1 #return this for later, but added a round because it is not accounted for
        else:
            for i in range(k):
                if slots.count(slots[i]) > 1:
                    b[i] += 1

            rounds += 1
            #print(slots)




"function for going over main simulation for sample_size times"
def ev_oneOK(k):
    evs = []

    # loops through main simulation sample size times and then
    # adds the return (rounds) to the above array for later use
    for i in range(sample_size):
        evs.append(try_time_slot(k))

    m = np.mean(evs)
    sd = np.std(evs)
    cv = sd / m

    return cv

"What teacher wants to see plus a bar plot to give some sort of understanding"
"to what this simulation is doing"
def run_all_ev():
    print("max_k = %d, max_b = %d, sample_size = %d" % (max_k, max_w, sample_size)) #syntax recommended
    means = []

    #grabs each mean value
    #prints out all the different mean values for each k (senders)
    for k in range(1, max_k + 1):
        mean = ev_oneOK(k)
        means.append(mean)
        print(f"k={k}, ev_oneOK(k)= {mean:.4f}") #syntax recommended

    #matplotlib set up for bar graph
    plt.bar(range(1, max_k + 1), means)
    plt.xlabel('number of senders')
    plt.ylabel('mean of sender collisions')
    plt.title('Representation?')
    plt.show()



def main():
    run_all_ev()

if __name__== "__main__":
    main()