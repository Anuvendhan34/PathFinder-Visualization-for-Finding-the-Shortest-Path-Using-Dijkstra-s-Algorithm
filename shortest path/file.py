import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

# Function to create a random graph
def generate_random_graph(nodes=5, max_weight=10):
    G = nx.Graph()
    # Add random edges
    for i in range(nodes):
        for j in range(i + 1, nodes):
            if random.random() < 0.5:  # 50% chance to create an edge
                weight = random.randint(1, max_weight)
                G.add_edge(i, j, weight=weight)
    return G

# Dijkstra's algorithm
def dijkstra(graph, start):
    distances = {node: np.inf for node in graph.nodes}
    predecessors = {node: None for node in graph.nodes}
    distances[start] = 0
    unvisited_nodes = list(graph.nodes)

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        unvisited_nodes.remove(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node

    return distances, predecessors

# Plot the graph using Matplotlib
def plot_graph(G, start_node, distances, predecessors):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')
    
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Highlight the shortest path
    path = []
    for node in predecessors:
        if predecessors[node] is not None:
            path.append((predecessors[node], node))

    nx.draw_networkx_edges(G, pos, edgelist=path, width=4, edge_color='red')

    plt.title(f"Shortest Path from {start_node}")
    plt.axis('off')
    plt.show()

# Generate a new random graph and display the result
def generate_and_show():
    nodes = int(node_count_entry.get())  # Number of nodes from user input
    max_weight = int(weight_max_entry.get())  # Maximum weight from user input
    
    # Generate random graph
    G = generate_random_graph(nodes, max_weight)
    
    # Choose a random start node
    start_node = random.choice(list(G.nodes))
    
    # Apply Dijkstra's algorithm
    distances, predecessors = dijkstra(G, start_node)

    # Display the shortest distances
    result = f"Shortest distances from node {start_node}:\n"
    for node in distances:
        result += f"{start_node} -> {node}: {distances[node]}\n"

    messagebox.showinfo("Shortest Path", result)

    # Plot the graph with the shortest path
    plot_graph(G, start_node, distances, predecessors)

# Create the Tkinter window
root = tk.Tk()
root.title("Dijkstra's Algorithm Random Graph Generator")

# Widgets for user input
tk.Label(root, text="Number of Nodes:").pack(pady=5)
node_count_entry = tk.Entry(root)
node_count_entry.insert(0, "5")
node_count_entry.pack(pady=5)

tk.Label(root, text="Max Weight for Edges:").pack(pady=5)
weight_max_entry = tk.Entry(root)
weight_max_entry.insert(0, "10")
weight_max_entry.pack(pady=5)

# Button to generate random graph and run Dijkstra's algorithm
generate_button = tk.Button(root, text="Generate Graph and Find Shortest Path", command=generate_and_show)
generate_button.pack(pady=20)

root.mainloop()
