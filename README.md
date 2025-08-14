# Dependências
```
pip install qiskit
```

```
pip install qiskit-ibm-runtime
```

```
pip install qiskit[visualization]
```

```
pip install qiskit_aer
```
Caso esteja em wsl e tenha problemas com a instalação, tente usar a tag ``` --break-system-packages ```

# Executando testes
Para executar testes, basta configurar os parâmetros do teste no script [test.py](tests.py) e executá-lo usando o comando:

```
python3 test.py
```

Caso queira salvar os resultados em um arquivo de texto, use:

```
python3 test.py > nome.txt
```

### Parâmetros do teste
- n_numbers: Quantidade de semiprimos gerados para cada tamanho
- primes_max_size: lista de tamanhos dos fatores
- n_tests: número de iterações dos algoritmos para cada número gerado
- rd_seed: semente usada para usos da bibioteca `random` dentro do algoritmo de Shor
- graph_name: nome do arquivo onde será salvo o gráfico dos resultados

# Fontes e créditos
Esse repositório foi criado a partir do trabalho da comunidade QisKit e da computação quântica. Os algoritmos das seguintes fontes forem utilizados apenas para fins educativos.

[Tutorial e explicação do algoritmo de Shor da comunidade Qiskit](https://github.com/qiskit-community/qiskit-community-tutorials/blob/master/algorithms/shor_algorithm.ipynb)

[Algoritmo de Shor em computador quântico simulado em python 3 por toddwildey](https://github.com/toddwildey/shors-python/tree/master)

[Algoritmo de Shor e quebra do RSA por gcjordi](https://github.com/gcjordi/quantum_cracking_encryption/tree/master)

