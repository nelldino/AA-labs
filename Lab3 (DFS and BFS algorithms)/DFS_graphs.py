# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10cyBwqWL56TOumH8TsTx-9jh1mX6yVd5
"""

import random
import networkx as nx
import matplotlib.pyplot as plt
import time

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs_util(self, v, visited):
        visited[v] = True

        for i in self.adj_list[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_node):
        visited = [False] * self.vertices
        self.dfs_util(start_node, visited)
        return visited

# Function to generate a path graph with the given number of nodes and plot it
def generate_and_plot_path_graph(num_nodes):
    G = nx.Graph()
    graph = Graph(num_nodes)

    # Add edges to the graph to create a path
    for i in range(num_nodes - 1):
        graph.add_edge(i, i + 1)
        G.add_edge(i, i + 1)

    # Plot the graph
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    plt.title(f"Path Graph with {num_nodes} Nodes")
    plt.show()

    return graph

# Function to generate a cycle graph with the given number of nodes and plot it
def generate_and_plot_cycle_graph(num_nodes):
    G = nx.Graph()
    graph = Graph(num_nodes)

    # Add edges to the graph to create a cycle
    for i in range(num_nodes):
        graph.add_edge(i, (i + 1) % num_nodes)
        G.add_edge(i, (i + 1) % num_nodes)

    # Plot the graph
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    plt.title(f"Cycle Graph with {num_nodes} Nodes")
    plt.show()

    return graph

# Function to generate a sparse graph with the given number of nodes and plot it
def generate_and_plot_sparse_graph(num_nodes, edge_probability):
    G = nx.Graph()
    graph = Graph(num_nodes)

    # Add edges to the graph with a given edge probability
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < edge_probability:
                graph.add_edge(i, j)
                G.add_edge(i, j)

    # Plot the graph
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    plt.title(f"Sparse Graph with {num_nodes} Nodes")
    plt.show()

    return graph

# Function to generate a tree graph with the given number of nodes and plot it
def generate_and_plot_tree_graph(num_nodes):
    G = nx.Graph()
    graph = Graph(num_nodes)

    # Add edges to the graph to create a tree
    for i in range(1, num_nodes):
        parent = random.randint(0, i - 1)
        graph.add_edge(parent, i)
        G.add_edge(parent, i)

    # Plot the graph
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    plt.title(f"Tree Graph with {num_nodes} Nodes")
    plt.show()

    return graph

# Function to generate a complete graph with the given number of nodes and plot it
def generate_and_plot_complete_graph(num_nodes):
    G = nx.complete_graph(num_nodes)
    graph = Graph(num_nodes)

    # Add edges to the graph
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            graph.add_edge(i, j)

    # Plot the graph
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    plt.title(f"Complete Graph with {num_nodes} Nodes")
    plt.show()

    return graph

# Function to generate a bipartite graph with the given number of nodes in each partition and plot it
def generate_and_plot_bipartite_graph(partition1_nodes, partition2_nodes):
    G = nx.complete_bipartite_graph(partition1_nodes, partition2_nodes)
    graph = Graph(partition1_nodes + partition2_nodes)

    # Add edges to the graph
    for i in range(partition1_nodes):
        for j in range(partition1_nodes, partition1_nodes + partition2_nodes):
            graph.add_edge(i, j)

    # Plot the graph
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    plt.title(f"Bipartite Graph with {partition1_nodes} and {partition2_nodes} Nodes")
    plt.show()

    return graph

# Perform DFS on path, cycle, sparse, tree, complete, and bipartite graphs with different number of nodes and plot the graphs
def perform_dfs_and_plot_graphs():
    nodes_list = [10, 25, 50, 75, 100, 150]
    edge_probability = 0.1

    for num_nodes in nodes_list:
        print(f"\nNumber of Nodes: {num_nodes}")
        start_time = time.time()
        graph = generate_and_plot_path_graph(num_nodes)
        start_node = random.randint(0, num_nodes - 1)
        visited = graph.dfs(start_node)
        end_time = time.time()
        print("Visited Nodes after DFS in Path Graph:", visited)
        print("Execution Time for Path Graph:", end_time - start_time, "seconds")

        start_time = time.time()
        graph = generate_and_plot_cycle_graph(num_nodes)
        start_node = random.randint(0, num_nodes - 1)
        visited = graph.dfs(start_node)
        end_time = time.time()
        print("\nVisited Nodes after DFS in Cycle Graph:", visited)
        print("Execution Time for Cycle Graph:", end_time - start_time, "seconds")

        start_time = time.time()
        graph = generate_and_plot_sparse_graph(num_nodes, edge_probability)
        start_node = random.randint(0, num_nodes - 1)
        visited = graph.dfs(start_node)
        end_time = time.time()
        print("\nVisited Nodes after DFS in Sparse Graph:", visited)
        print("Execution Time for Sparse Graph:", end_time - start_time, "seconds")

        start_time = time.time()
        graph = generate_and_plot_tree_graph(num_nodes)
        start_node = random.randint(0, num_nodes - 1)
        visited = graph.dfs(start_node)
        end_time = time.time()
        print("\nVisited Nodes after DFS in Tree Graph:", visited)
        print("Execution Time for Tree Graph:", end_time - start_time, "seconds")

        start_time = time.time()
        graph = generate_and_plot_complete_graph(num_nodes)
        start_node = random.randint(0, num_nodes - 1)
        visited = graph.dfs(start_node)
        end_time = time.time()
        print("\nVisited Nodes after DFS in Complete Graph:", visited)
        print("Execution Time for Complete Graph:", end_time - start_time, "seconds")

        partition1_nodes = num_nodes // 2
        partition2_nodes = num_nodes - partition1_nodes
        start_time = time.time()
        graph = generate_and_plot_bipartite_graph(partition1_nodes, partition2_nodes)
        start_node = random.randint(0, num_nodes - 1)
        visited = graph.dfs(start_node)
        end_time = time.time()
        print("\nVisited Nodes after DFS in Bipartite Graph:", visited)
        print("Execution Time for Bipartite Graph:", end_time - start_time, "seconds")

# Call the function
perform_dfs_and_plot_graphs()