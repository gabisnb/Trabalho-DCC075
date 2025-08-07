from math import gcd,log
from random import randint
from qiskit import *

import RSA_module
import Shor_module
import time

# N=18727 # 61*307
# assert N>0,"Input must be positive"
# print(Shor_module.shors_breaker(N))

N = []
n = 5
prime_max = 500
n_trials = 27

for i in range(n):
    while True:
        prime = Shor_module.get_semiprime(prime_max)
        if prime not in N and prime > 1000 and prime < 2**16:
            N.append(prime)
            break

print("Generated semiprimes:", N)

# Teste com algoritmo de força bruta
brute_force_results = []

print("\n=========Brute force results=========")
for semiprime in N:
    total_time = 0
    for i in range(n_trials):
        start = time.time()
        factors = Shor_module.shors_breaker_brute_force(semiprime)
        end = time.time()
        total_time += end - start
    average_time = total_time / n_trials
    brute_force_results.append((semiprime, factors, average_time))
    print(f"Semiprime: {semiprime}, Factors: {factors}, Average Time: {average_time:.6f} seconds")


# Teste em ambiente simulado
simulated_results = []

print("\n=========Simulated results=========")
for semiprime in N:
    total_time = 0
    for i in range(n_trials):
        start = time.time()
        factors = Shor_module.shors_breaker(semiprime)
        end = time.time()
        total_time += end - start
    average_time = total_time / n_trials
    simulated_results.append((semiprime, factors, average_time))
    print(f"Semiprime: {semiprime}, Factors: {factors}, Average Time: {average_time:.6f} seconds")

