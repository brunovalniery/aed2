#UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
#CENTRO DE TECNOLOGIA
#DEPARTAMENTO DE ENGENHARIA DE COMPUTAÇÃO E AUTOMAÇÃO
#DCA0209 - ALGORITMOS E ESTRUTURAS DE DADOS II

#Bruno Valniery Gomes de Sousa

#Desafio: Autocompletar Palavras
#Objetivo: Criar um sistema de autocompletar palavras usando uma árvore AVL.
#Como exe

# Implementação da Árvore AVL

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance_factor(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    update_height(x)
    update_height(y)

    return y

def insert(root, key):
    if not root:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root  # Duplicates not allowed

    update_height(root)

    balance = get_balance_factor(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

# Construção da Árvore AVL a partir do Corpus

def preprocess_text(text):
    text = text.lower()
    text = ''.join(e for e in text if e.isalnum() or e.isspace())
    words = text.split()
    stopwords = set(["e", "ou", "mas", "a", "o", "e"])
    return [word for word in words if word not in stopwords]

def build_avl_tree(corpus):
    avl_tree = None
    unique_words = set()

    for sentence in corpus:
        words = preprocess_text(sentence)
        for word in words:
            unique_words.add(word)

    for word in unique_words:
        avl_tree = insert(avl_tree, word)

    return avl_tree

# Autocompletar com a Árvore AVL

def autocomplete(root, prefix):
    suggestions = []

    def search(node, current_prefix):
        if not node:
            return

        if node.key.startswith(current_prefix):
            suggestions.append(node.key)

        if current_prefix < node.key:
            search(node.left, current_prefix)
        search(node.right, current_prefix)  # Não importa o valor, procuramos em ambos os lados

    search(root, prefix)

    return suggestions

# Exemplos de Uso

corpus = [
    "O sol brilha durante o dia enquanto a lua brilha durante a noite.",
    "O gato caça o rato, enquanto o cachorro caça o gato.",
    "As frutas são saudáveis. Adoro comer maçãs, bananas e uvas.",
    "Programar em Python, Java e C++ é divertido.",
    "Gosto de café, chá e suco. Mas evito refrigerante.",
    "Ela estuda matemática, física e química.",
    "Os planetas do sistema solar são Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano e Netuno."
]

avl_tree = build_avl_tree(corpus)

prefix = "ca"
suggestions = autocomplete(avl_tree, prefix)

print("Lista de Palavras:", suggestions)
