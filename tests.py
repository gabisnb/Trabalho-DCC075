from math import gcd,log
from random import randint
from qiskit import *

import RSA_module
import Shor_module
import time
import matplotlib.pyplot as plt
import random

def test_shor(n, prime_max, n_trials, seed): # This seed is for the random number in the Shor's algorithm
    N = []
    for i in range(n):
        while True:
            semiprime = Shor_module.get_semiprime(prime_max, time.time()) # Seed for random number generation
            if semiprime not in N and semiprime > prime_max and semiprime < prime_max*2 and semiprime < 2**16:
                N.append(semiprime)
                break
    print("=========Size ", prime_max, "=========")
    print("Generated semiprimes:", N)

    # Teste com algoritmo de força bruta
    brute_force_results = []

    print("\n=========Brute force results=========")
    for semiprime in N:
        total_time = 0
        for i in range(n_trials):
            start = time.time()
            factors = Shor_module.shors_breaker_brute_force(semiprime, seed=seed)
            end = time.time()
            total_time += end - start
        average_time = total_time / n_trials
        brute_force_results.append((semiprime, average_time))
        print(f"Semiprime: {semiprime}, Factors: {factors}, Average Time: {average_time:.6f} seconds")


    # Teste em ambiente simulado
    simulated_results = []

    print("\n=========Simulated results=========")
    for semiprime in N:
        total_time = 0
        for i in range(n_trials):
            start = time.time()
            factors = Shor_module.shors_breaker(semiprime, seed=seed)
            end = time.time()
            total_time += end - start
        average_time = total_time / n_trials
        simulated_results.append((semiprime, average_time))
        print(f"Semiprime: {semiprime}, Factors: {factors}, Average Time: {average_time:.6f} seconds")
    print("====================================\n\n")
    return brute_force_results, simulated_results

### Configuração do teste ################################
n_numbers = 10
primes_max_size = [50, 100, 500, 1000, 5000, 10000]
n_tests = 30
rd_seed = 1637593
graph_name = "TrueTest_PlotLog"
##########################################################

brute_force_results = []
simulated_results = []
for primes_max in primes_max_size:
    brute_force, simulated = test_shor(n_numbers, primes_max, n_tests, rd_seed)
    brute_force_results.extend(brute_force)
    simulated_results.extend(simulated)

brute_force_results.sort()
simulated_results.sort()

fig, ax = plt.subplots()
ax.plot([x[0] for x in brute_force_results], [x[1] for x in brute_force_results], label='Brute Force', color='blue', marker='o', linestyle="None", alpha=0.5)
ax.plot([x[0] for x in simulated_results], [x[1] for x in simulated_results], label='Simulated', color='red', marker='o', linestyle="None", alpha=0.5)
ax.set_title("Simulated results vs Brute force results")
ax.set_xlabel("Semiprimo (log)")
ax.set_ylabel("Tempo médio (segundos) (log)")
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend()
plt.savefig(graph_name + ".png") 