# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N2XJrg1cA52QFHCGScZDlmEdNzAs4XgS
"""

import random
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import time

def generate_dense_graph(num_nodes):
    graph = nx.Graph()
    for i in range(num_nodes):
        graph.add_node(i)
        for j in range(i + 1, num_nodes):
            if random.random() < 0.7:  # Randomly connect nodes with 70% probability for denser graph
                weight = random.randint(1, 10)
                graph.add_edge(i, j, weight=weight)
    return graph

def generate_sparse_graph(num_nodes):
    graph = nx.Graph()
    for i in range(num_nodes):
        graph.add_node(i)
        for j in range(i + 1, num_nodes):
            if random.random() < 0.3:  # Randomly connect nodes with 30% probability for sparse graph
                weight = random.randint(1, 10)
                graph.add_edge(i, j, weight=weight)
    return graph


def floyd_warshall(graph):
    num_nodes = len(graph.nodes)
    dist = [[float('inf')] * num_nodes for _ in range(num_nodes)]

    # Initialize distances with edge weights
    for u, v, weight in graph.edges(data='weight'):
        dist[u][v] = weight
        dist[v][u] = weight

    # Initialize distances to self as 0
    for i in range(num_nodes):
        dist[i][i] = 0

    start_time = time.time()

    # Floyd-Warshall algorithm
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time

# Generate execution time data for both dense and sparse graphs
num_nodes_list = list(range(10, 800, 50))  # Generate numbers of nodes from 10 to 1000
dense_execution_times = []
sparse_execution_times = []

for num_nodes in num_nodes_list:
    dense_graph = generate_dense_graph(num_nodes)
    sparse_graph = generate_sparse_graph(num_nodes)

    dense_time = floyd_warshall(dense_graph)
    sparse_time = floyd_warshall(sparse_graph)

    dense_execution_times.append(dense_time)
    sparse_execution_times.append(sparse_time)

# Plot execution time against number of nodes
plt.figure(figsize=(10, 6))
plt.plot(num_nodes_list, dense_execution_times, label='Dense Graph', marker='o')
plt.plot(num_nodes_list, sparse_execution_times, label='Sparse Graph', marker='o')
plt.xlabel('Number of Nodes')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of Floyd-Warshall Algorithm')
plt.legend()
plt.grid(True)
plt.show()