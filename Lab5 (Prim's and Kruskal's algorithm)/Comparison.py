# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cMWLMrpbeSprtwxiH3NJoQSwmibTXIys
"""

import time
import random
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append((src, dest, weight))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        start_time = time.time()

        result = []
        i = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        for edge in self.graph:
            u, v, w = edge
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append((u, v, w))
                self.union(parent, rank, x, y)
                i += 1
                if i == self.V - 1:
                    break

        end_time = time.time()
        total_time = end_time - start_time

        return total_time

    def prim_mst(self):
        parent = [-1] * self.V
        key = [float('inf')] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        start_time = time.time()

        while False in mst_set:
            u = min((key[i], i) for i in range(self.V) if not mst_set[i])[1]
            mst_set[u] = True
            for edge in self.graph:
                src, dest, weight = edge
                if (src == u or dest == u) and not mst_set[dest if src == u else src] and key[dest if src == u else src] > weight:
                    key[dest if src == u else src] = weight
                    parent[dest if src == u else src] = u

        end_time = time.time()

        total_time = end_time - start_time

        return total_time

def plot_comparison(n_values, prim_times, kruskal_times):
    plt.plot(n_values, prim_times, marker='o', label='Prim')
    plt.plot(n_values, kruskal_times, marker='o', label='Kruskal')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Comparison of Prim and Kruskal Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    max_nodes = 500
    step = 50
    n_values = list(range(2, max_nodes + 1, step))
    prim_times = []
    kruskal_times = []

    for n in n_values:
        graph = Graph(n)
        for i in range(n):
            for j in range(i+1, n):
                graph.add_edge(i, j, random.randint(1, 100))

        prim_time = graph.prim_mst()
        kruskal_time = graph.kruskal_mst()

        prim_times.append(prim_time)
        kruskal_times.append(kruskal_time)

    plot_comparison(n_values, prim_times, kruskal_times)