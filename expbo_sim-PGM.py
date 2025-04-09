import numpy as np
import matplotlib as mpl

"global variables BECAUSE they are constant :)"
max_k = 14 #maximum number of senders
max_b = 4 #maximum backoff doubling
max_w = pow(2, max_b) #maximum backoff window size (== 2^max_b).
sample_size = 5  #the number trials to run to compute expected values
counter = 0

xb = 1 #maximum allowed backoff

"define time into discrete slots"
def time_slots(k):
    time = [k-1]
    return time

"trying to figure out how to increase senders for each cycle"
def senders(k):
    for i in range(max_k):
        k = k + 1
        break
    return k

"each station tries to transmit packets at a certain time"
def packet_send_off(k):
    sender = senders(k)
    slot = time_slots(k)
    for i in range(sender):
        if slot[i] < sender:
            return is_collision()
        else:
            slot.append(slot[i])
            return "success"


"transmission rules: 1 station transmits in a slot --> success"\
"2+ station transmits in a slot --> collision"
def is_collision():
    is_collision.counter += 1 #need to record amount of attempts senders have used
    exponential_backoff()
    print("abort transmission")
    return is_collision.counter

is_collision.counter = 0

#for each time slot
    #check which time slots are attempting to transmit
def who_is_it():
    return

    #count n of simultaneous  transmissions
def how_many():
    return


def exponential_backoff():
    attempts = is_collision()
    for i in range(attempts):
        if attempts < sample_size:
            calculation = 1 * pow(2, attempts - 1)
            seconds = attempts * 2
            return calculation, seconds
        else:
            return print("exceeded amount of attempts allowed")


"function tracks the collision rate metric"
def collision_rate(n, attempts):
    #collision rate = number of collisions / total transmission attempts
    return n / attempts

#sucessful transmission per unit
def throughput():
    return

#time taken for packet to succeed
def average_delay():
    return

def run_all_ev():
    print("max_k = %d, max_b = %d, sample_size = %d" % (max_k, max_b, sample_size))
    print("k=", k ,"ev_oneOK(k)=", exponential_backoff())


def main():
    run_all_ev()


if __name__== "__main__":
    main()