import numpy as np

"""
Create an array with 10 million entries.
0 represents a vote for 'A' and 1 represents a vote for 'B'
"""


def sample(population, size):
    num_samples = 1000
    sample_counts = np.zeros(num_samples)
    for i in range(num_samples):
        sample = np.random.choice(population, size)
        Bcount = np.count_nonzero(sample)
        if Bcount <= size * 0.5:
            sample_counts[i] = 1
    percentage = np.count_nonzero(sample_counts) / num_samples * 100
    return percentage

size = 10000000
A = 0.55
B = 1-A
print("The population percentage for A is ", A)

Avotes = np.zeros(int(A*size))
Bvotes = np.ones(int(B*size))
totalVotes = np.concatenate((Avotes,Bvotes))
np.random.shuffle(totalVotes)

sample_sizes = [20,100,400]
for size in sample_sizes:
    print("Random sampling of size: ", size)
    percentage = sample(totalVotes, size)
    print("A vote was the majority in ", percentage, " percent of samples sizes of ", size)
    print("\n")

majority = False
size = 100
while (majority == False):
    percentage = sample(totalVotes, size)
    if (percentage >=90):
        #print("Just reached 90 percent majority with sample size of ", size)
        accuracy_counts = np.zeros(1000)
        for i in range(1000):
            percentage = sample(totalVotes, size)
            if (percentage >=90):
                accuracy_counts[i] = 1
        accuracy = np.count_nonzero(accuracy_counts) / 1000 * 100
        if (accuracy >= 99.9):
            print("The sample size with 90 percent accuracy 99.9 percent of the time is ", size)
            majority = True
        else:
            size = size + 10
    else:
        size = size + 10
    

