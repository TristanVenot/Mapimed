import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from networkx.algorithms.community import greedy_modularity_communities

def generate_random_network(num_nodes=10, num_edges=5):
    # Create a random graph
    G = nx.gnm_random_graph(num_nodes, num_edges)
    # Adjacency matrix
    adj_matrix = nx.adjacency_matrix(G).todense()
    return G, adj_matrix

def plot_network_2d(G):
    pos = nx.spring_layout(G)  # 2D layout
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=500, font_size=10)
    plt.title("2D Network Visualization")
    plt.show()

def plot_network_3d(G):
    pos = nx.spring_layout(G, dim=3)  # 3D layout
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="3d")
    for node, (x, y, z) in pos.items():
        ax.scatter(x, y, z, color='skyblue', s=100)
        ax.text(x, y, z, str(node), fontsize=10, color='black')
    for (u, v) in G.edges():
        x = np.array([pos[u][0], pos[v][0]])
        y = np.array([pos[u][1], pos[v][1]])
        z = np.array([pos[u][2], pos[v][2]])
        ax.plot(x, y, z, color='gray')
    plt.title("3D Network Visualization")
    plt.show()

def calculate_metrics(G):
    # Global efficiency
    global_eff = nx.global_efficiency(G)
    # Modularity (using greedy modularity communities)
    communities = list(greedy_modularity_communities(G))
    modularity = nx.algorithms.community.quality.modularity(G, communities)
    # Density
    density = nx.density(G)
    # Node degree
    degree = dict(G.degree())
    # Node betweenness
    betweenness = nx.betweenness_centrality(G)
    return global_eff, modularity, density, degree, betweenness

def main(num_nodes=10, num_edges=5):
    num_nodes = 10
    num_edges = 10
    G, adj_matrix = generate_random_network(num_nodes, num_edges)
    print("Adjacency Matrix:")
    print(adj_matrix)
    # plt.figure(figsize=(8, 6))
    # nx.draw(G, with_labels=True, node_color='lightblue', node_size=700, font_size=12, edge_color='gray')
    # plt.title("Network Visualization from Adjacency Matrix")
    # plt.show()
    # Plot the network in 2D and 3D
    plot_network_2d(G)
    plot_network_3d(G)

    # Calculate metrics
    global_eff, modularity, density, degree, betweenness = calculate_metrics(G)
    print(f"Global Efficiency: {global_eff}")
    print(f"Modularity: {modularity}")
    print(f"Density: {density}")
    print("Node Degrees:")
    print(degree)
    print("Node Betweenness Centrality:")
    print(betweenness)

if __name__ == "__main__":
    # Customize the number of nodes and edges here
    main(num_nodes=100, num_edges=200)
