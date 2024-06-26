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

def dijkstra(graph, source):
    # Initialize distances with infinity for all nodes
    distances = {node: float('inf') for node in graph.nodes()}
    distances[source] = 0

    # Initialize predecessors
    predecessors = {node: None for node in graph.nodes()}

    # Priority queue to keep track of the next node to visit
    priority_queue = [(0, source)]  # (distance, node)

    visited_order = []  # To store the order of visited nodes

    start_time = time.time()  # Start timing

    while priority_queue:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the distance already found, skip
        if current_distance > distances[current_node]:
            continue

        # Append the current node to the visited_order list
        visited_order.append(current_node)

        # Iterate over neighbors of the current node
        for neighbor in graph.neighbors(current_node):
            distance = current_distance + graph[current_node][neighbor]['weight']
            # Update the distance if the new distance is smaller
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    end_time = time.time()  # End timing
    execution_time = end_time - start_time  # Calculate execution time

    return distances, predecessors, visited_order, execution_time

def visualize_graph(graph):
    plt.figure(figsize=(10, 8))  # Larger figsize
    pos = nx.spring_layout(graph)  # Layout for better visualization
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold")
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title("Graph Visualization")
    plt.show()

def visualize_dijkstra(graph, distances, predecessors, source, visited_order, execution_time):
    plt.figure(figsize=(10, 8))  # Larger figsize
    pos = nx.spring_layout(graph)  # Layout for better visualization
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold")
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    # Highlight shortest path
    node_colors = ['yellow' if node == source else 'lightgreen' for node in graph.nodes()]
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=500)

    plt.title("Dijkstra Visualization")
    plt.show()

    print("Order of visited nodes:")
    for i, node in enumerate(visited_order):
        print(f"{i + 1}. Node {node}")

    print(f"Execution time: {execution_time} seconds")

# Generate and visualize graphs for different numbers of nodes
for num_nodes in [5, 10, 25, 50, 75, 100]:
    print(f"Generating and visualizing graph with {num_nodes} nodes...")
    graph = generate_random_graph(num_nodes)
    visualize_graph(graph)

    # Choose a random source node
    source = random.choice(list(graph.nodes()))

    # Perform Dijkstra's algorithm
    distances, predecessors, visited_order, execution_time = dijkstra(graph, source)

    # Visualize Dijkstra's algorithm
    visualize_dijkstra(graph, distances, predecessors, source, visited_order, execution_time)