# Importar as bibliotecas necessárias
import csv
import time
import random

# Criar uma classe chamada Inventory para gerenciar o inventário de laptops
class Inventory:
    # Inicializar a classe com um arquivo CSV contendo dados de laptops
    def __init__(self, csv_filename):
        # Abrir o arquivo CSV fornecido e ler seu conteúdo
        """
        Inicializa a classe Inventory com os dados do arquivo CSV especificado.

        Argumentos:
            csv_filename (str): O nome do arquivo CSV contendo os dados dos laptops.
        """
        with open(csv_filename, encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            # Atribuir o cabeçalho (a primeira linha) do arquivo CSV a uma variável chamada header
            self.header = next(csv_reader)
            
            # Atribuir as linhas de dados (os laptops) do arquivo CSV a uma variável chamada rows
            self.rows = list(csv_reader)
            
            # Converter os preços dos laptops para números inteiros
            for row in self.rows:
                row[-1] = int(row[-1])
            
            # Criar um dicionário que mapeia IDs de laptop para suas linhas de dados correspondentes
            self.id_to_row = {}
            for row in self.rows:
                self.id_to_row[row[0]] = row
            
            # Criar um conjunto (set) contendo todos os preços dos laptops
            self.prices = set()
            for row in self.rows:
                self.prices.add(row[-1])

    # Método para obter informações de um laptop pelo ID de forma rápida
    """
    Retorna informações de um laptop com base no ID de forma rápida.

    Argumentos:
        laptop_id (str): O ID do laptop a ser procurado.

    Returns:
        list or None: As informações do laptop se encontrado, caso contrário, None.
    """
    def get_laptop_from_id_fast(self, laptop_id):
        if laptop_id in self.id_to_row:
            return self.id_to_row[laptop_id]
        else:
            return None

    # Método para obter informações de um laptop pelo ID de forma mais lenta
    def get_laptop_from_id(self, laptop_id):
        for row in self.rows:
            if row[0] == laptop_id:
                return row
        return None

    # Método para verificar se é possível encontrar um laptop com um preço específico usando busca lenta
    def check_promotion_dollars(self, dollars):
        for row in self.rows:
            if row[-1] == dollars:
                return True
        
        for i in range(len(self.rows)):
            for j in range(len(self.rows)):
                if i != j and self.rows[i][-1] + self.rows[j][-1] == dollars:
                    return True
        return False

    # Método para verificar se é possível encontrar um laptop com um preço específico usando busca rápida
    def check_promotion_dollars_fast(self, dollars):
        if dollars in self.prices:
            return True
        
        for price1 in self.prices:
            price2 = dollars - price1
            if price2 in self.prices:
                return True
        
        return False

    # Método para encontrar laptops dentro de uma faixa de preço
    def find_laptop_with_price_range(self, min_price, max_price):
        laptops_in_range = []
        for row in self.rows:
            price = row[-1]
            if min_price <= price <= max_price:
                laptops_in_range.append(row)
        return laptops_in_range

    # Método para encontrar o laptop mais barato com especificações (RAM e armazenamento)
    def find_cheapest_laptop_with_specifications(self, ram, storage):
        cheapest_laptop = None
        cheapest_price = float('inf')
        
        for row in self.rows:
            laptop_ram = row[8]  # Supondo que a coluna da RAM seja a nona (índice 8)
            laptop_storage = row[9]  # Supondo que a coluna do armazenamento seja a décima (índice 9)
            price = row[-1]
            
            if laptop_ram == ram and laptop_storage == storage and price < cheapest_price:
                cheapest_laptop = row
                cheapest_price = price
        
        return cheapest_laptop

# Gerar uma lista de 100 preços aleatórios entre 100 e 5.000
prices = [random.randint(100, 5000) for _ in range(100)]

# Criar uma instância da classe Inventory usando 'laptops.csv' como argumento
inventory = Inventory('laptops.csv')

# Inicializar variáveis para agregar o tempo de execução de cada método
total_time_no_set = 0
total_time_set = 0

# Medir o tempo para check_promotion_dollars
for price in prices:
    start = time.time()
    inventory.check_promotion_dollars(price)
    end = time.time()
    total_time_no_set += end - start

# Medir o tempo para check_promotion_dollars_fast
for price in prices:
    start = time.time()
    inventory.check_promotion_dollars_fast(price)
    end = time.time()
    total_time_set += end - start

# Imprimir o tempo total de execução para ambos os métodos
print("Total time for check_promotion_dollars: {:.5f} seconds".format(total_time_no_set))
print("Total time for check_promotion_dollars_fast: {:.5f} seconds".format(total_time_set))

# Consultar laptops dentro de uma faixa de preço (exemplo: de 500 a 1000)
laptops_in_range = inventory.find_laptop_with_price_range(500, 1000)
for laptop in laptops_in_range:
    print(laptop)

# Consultar o laptop mais barato com especificações específicas (exemplo: 8GB de RAM e 256GB de armazenamento)
cheapest_laptop = inventory.find_cheapest_laptop_with_specifications('8GB', '256GB')
print(cheapest_laptop)
