from math import gcd,log
from random import randint
import numpy as np
from qiskit import *
import random, itertools

from qiskit.primitives import BackendSamplerV2
from qiskit.providers.basic_provider import BasicProvider
from qiskit_aer import AerSimulator
from qiskit_aer.primitives import Sampler

# algoritmo de Shor feito por gcjordi
def period(a,N):
    available_qubits = 16 
    r=-1
    
    if N >= 2**available_qubits:
        print(str(N)+' is too big for IBMQX')
    
    qr = QuantumRegister(available_qubits)   
    cr = ClassicalRegister(available_qubits)
    qc = QuantumCircuit(qr,cr)
    x0 = randint(1, N-1) 
    x_binary = np.zeros(available_qubits, dtype=bool)
    
    for i in range(1, available_qubits + 1):
        bit_state = (N%(2**i)!=0)
        if bit_state:
            N -= 2**(i-1)
        x_binary[available_qubits-i] = bit_state    
    
    for i in range(0,available_qubits):
        if x_binary[available_qubits-i-1]:
            qc.x(qr[i])
    x = x0
    
    while np.logical_or(x != x0, r <= 0):
        r+=1
        qc.measure(qr, cr) 
        for i in range(0,3): 
            qc.x(qr[i])
        qc.cx(qr[2],qr[1])
        qc.cx(qr[1],qr[2])
        qc.cx(qr[2],qr[1])
        qc.cx(qr[1],qr[0])
        qc.cx(qr[0],qr[1])
        qc.cx(qr[1],qr[0])
        qc.cx(qr[3],qr[0])
        qc.cx(qr[0],qr[1])
        qc.cx(qr[1],qr[0])
        
        sampler = Sampler()
        job = sampler.run(qc, shots=1024)
        result = job.result()
        quasi_dist = result.quasi_dists[0]
        total_shots = result.metadata[0]['shots'] # Get total shots from metadata
        counts = {}
        for bitstring, prob in quasi_dist.items():
            count = round(prob * total_shots)
            if count > 0: # Only include outcomes with non-zero counts
                counts[bitstring] = count
        # print(qc)
        results = [[],[]]
        for key,value in counts.items(): #the result should be deterministic but there might be some quantum calculation error so we take the most reccurent output
            results[0].append(key)
            results[1].append(int(value))
        s = results[0][np.argmax(np.array(results[1]))]
    return r

def find_period_classical(x, N):
    n = 1
    t = x
    while t != 1:
        t *= x
        t %= N
        n += 1
    return n

def shors_breaker(N, seed=None):
    if(seed is not None):
        random.seed(seed)
    N = int(N)
    while True:
        a=randint(0,N-1)
        g=gcd(a,N)
        if g!=1 or N==1:
            return g,N//g
        else:
            r=period(a,N) 
            if r % 2 != 0:
                continue
            elif pow(a,r//2,N)==-1:
                continue
            else:
                p=gcd(pow(a,r//2)+1,N)
                q=gcd(pow(a,r//2)-1,N)
                if p==N or q==N:
                    continue
                return p,q
            
def shors_breaker_brute_force(N, seed=None):
    if(seed is not None):
        random.seed(seed)
    N = int(N)
    while True:
        a=randint(0,N-1)
        g=gcd(a,N)
        if g!=1 or N==1:
            return g,N//g
        else:
            r=period(a,N) 
            if r % 2 != 0:
                continue
            elif pow(a,r//2,N)==-1:
                continue
            else:
                p=gcd(pow(a,r//2)+1,N)
                q=gcd(pow(a,r//2)-1,N)
                if p==N or q==N:
                    continue
                return p,q
            
def sieve( ): # gera primos usando o algoritmo de Eratosthenes
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def get_primes_sieve(n):
    return list(itertools.takewhile(lambda p: p<n, sieve())) # gera um primo para cada p em range(n)

def get_semiprime(n, seed=None):
    if(seed is not None):
        random.seed(seed)
    primes = get_primes_sieve(n) # gera n inteiros primos
    l = len(primes)
    p = primes[random.randrange(l)] # seleciona um primo aleatoriamente
    q = primes[random.randrange(l)] # seleciona um primo aleatoriamente
    return p*q
                