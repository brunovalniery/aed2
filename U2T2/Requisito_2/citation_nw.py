import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# Carregue os dados da rede
# Substitua 'caminho_para_o_arquivo' pelo caminho do arquivo de dados da rede
#df = pd.read_csv('/content/cit-Patents.txt', delimiter='\t')
df = pd.read_csv('/content/cit-Patents.txt', delimiter='\t', error_bad_lines=False, quoting=3)


# Crie um grafo bipartido
B = nx.Graph()
B.add_nodes_from(df['source'].unique(), bipartite=0)
B.add_nodes_from(df['target'].unique(), bipartite=1)
B.add_edges_from([(row['source'], row['target']) for idx, row in df.iterrows()])

# Calcule o grau dos nós
degree_df = pd.DataFrame(B.degree(), columns=['node', 'degree'])

# Crie figuras em um layout de grid
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Plote a assortatividade para cada conjunto de nós
for i, node_set in enumerate(nx.bipartite.sets(B)):
    subgraph = B.subgraph(node_set)
    assortativity = nx.degree_assortativity_coefficient(subgraph)
    nx.draw(subgraph, ax=axs[i // 2, i % 2])
    axs[i // 2, i % 2].set_title(f'Assortatividade: {assortativity:.2f}')

plt.tight_layout()
plt.show()