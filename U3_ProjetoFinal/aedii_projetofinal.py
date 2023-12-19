# -*- coding: utf-8 -*-
"""AEDII-ProjetoFinal

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ojuPhUwvQQmLOSAo_A1Q5RoeEruzfBU1
"""

pip install osmnx

import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
from geopy.distance import geodesic

# 1. Escolha das Cidades ou Áreas de Estudo:
# Cidade ou área de estudo desejada.
place_name = 'Natal, Brazil'

# 2. Extração da Rede de Ruas:
# Utilização da função graph_from_place para extrair a rede de ruas da área escolhida.
graph = ox.graph_from_place(place_name, network_type='all')

# 3. Visualização da Rede:
# Plote a rede de ruas utilizando Matplotlib.
ox.plot_graph(ox.project_graph(graph))
plt.show()

# Calcular o número total de nós e arestas na rede
num_nodes = nx.number_of_nodes(graph)
num_edges = nx.number_of_edges(graph)

print(f"Número total de nós na rede: {num_nodes}")
print(f"Número total de arestas na rede: {num_edges}")

densidade = 2*num_edges/(num_nodes*(num_nodes-1))
print(f"Densidade da rede: {densidade}")



# Função para calcular o comprimento de uma aresta em metros
def calculate_edge_length(graph, edge):
    # Extrai as coordenadas dos nós que formam a aresta
    u, v, key = edge
    coordinates_u = graph.nodes[u]['y'], graph.nodes[u]['x']
    coordinates_v = graph.nodes[v]['y'], graph.nodes[v]['x']

    # Calcula a distância entre os dois pontos usando a fórmula de Haversine
    length = ox.distance.great_circle_vec(coordinates_u, coordinates_v)

    return length

# Calcular o comprimento total das ruas na rede
total_length = sum(calculate_edge_length(graph, edge) for edge in graph.edges(keys=True))

print(f"Comprimento total das ruas na rede: {total_length:.2f} metros")



# Calcule a centralidade de betweenness para cada nó no grafo
betweenness_centrality = nx.betweenness_centrality(graph)

# Imprima a centralidade de betweenness para cada nó
for node, centrality in betweenness_centrality.items():
    print(f"Nó {node}: {centrality}")


# Calcule a centralidade de grau para cada nó no grafo
degree_centrality = nx.degree_centrality(graph)

# Imprima a centralidade de grau para cada nó
for node, centrality in degree_centrality.items():
    print(f"Nó {node}: {centrality}")