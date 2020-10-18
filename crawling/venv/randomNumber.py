import random

Ns = []

for i in range(9999):
    N = []
    while sum(N) <= 1:
        N.append(random.uniform(0,1))

    Ns.append(len(N))

print(sum(Ns)/len(Ns))
