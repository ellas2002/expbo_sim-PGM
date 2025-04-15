Ella Stiller

contents: each submitted file’s name and purpose:

I have one additional file called expbo_sim-PGM. This file includes three functions and the main loop:

def try_time_slot(k): This function simulates the Truncated Binary Exponential Backoff. It takes one argument,
k, which represents the number of senders.

def ev_oneOK(k): This function runs try_time_slot() multiple times (for n iterations) to collect
the coefficient of variation based on how many rounds it took for the senders to succeed.

def run_all_ev(): This function runs simulations with k senders ranging from 1 to 14. It helps me
gather the mean number of attempts for each simulation. The results are plotted to show the relationship
between the mean and the number of senders, giving a visual representation of the outcome.

How I Know the Program Works:

I know the program works because, for k=1, I get a coefficient of variation of 0, which makes sense since
there's only one sender and one slot. However, it's tricky to fully validate the program because of the randomness
involved. Everything compiles correctly, and the output seems reasonable, but I can't be sure it's the perfect
implementation of the assignment.

How I Tested the Program:

I tested the program by running it with small sets and troubleshooting anything that didn’t make sense.
I used a lot of print statements to make sure the logic was functioning as expected.

Determining the Number of Samples:

Once I figured out how the code should behave, I needed to decide on the sample sizes. I’m not sure if my approach
is fully correct, but since the focus is on the coefficient of variation, I opted for larger sample sizes.
As the sample size increases, the bar graph becomes left-skewed, which I think happens because with k=2,
the collision/success ratio is roughly 50/50, making the results less accurate. Larger sample sizes seem to flatten
out the graph after a certain number of attempts.

Impact of Varying max_b:

When I decrease max_b, the plot for the coefficient of variation becomes right-skewed. On the other hand,
increasing max_b makes the plot left-skewed. This isn’t always the case with every run, but this is the
main pattern I’ve observed.

How I Used AI:

I used AI to help me better understand the assignment. I asked it for clarifications to make sure
I was on the right track.