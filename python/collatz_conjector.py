import networkx as nx
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
# Function to generate the sequence
def generate_sequence(start):
    num = start
    sequence = []
    while num != 1:
        sequence.append(num)
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
    sequence.append(1)  # Append 1 at the end of the sequence
    return sequence

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Create a directed graph
G = nx.DiGraph()

# Generate sequences from 500 to 1 and add edges to the graph
for x in range(8096, 0, -1):
    sequence = generate_sequence(x)
    for i in range(len(sequence) - 1):
        G.add_edge(sequence[i], sequence[i + 1])

# Position nodes using a graph layout
pos = nx.spring_layout(G, k=0.15, iterations=20)  # Adjust parameters for better spacing

# Draw nodes and edges
plt.figure(figsize=(20, 15))
node_colors = []
for node in G.nodes():
    if is_prime(node):
        color = mcolors.to_rgba('red', alpha=0.5)  # 50% opacity for prime numbers
    else:
        color = 'blue'
    node_colors.append(color)
    
nx.draw_networkx_nodes(G, pos, node_size=50, node_color=node_colors)  # Smaller nodes
nx.draw_networkx_edges(G, pos, edge_color='lightgrey', arrows=False)  # Light-colored edges without arrows

# Remove labels
plt.axis('off')

# Display the graph
plt.title("Tree Structure of Sequences with Prime Numbers Highlighted")
plt.show()


# import networkx as nx
# import matplotlib.pyplot as plt

# # Function to generate the sequence
# def generate_sequence(start):
#     num = start
#     sequence = []
#     while num != 1:
#         sequence.append(num)
#         if num % 2 == 0:
#             num = num // 2
#         else:
#             num = 3 * num + 1
#     sequence.append(1)  # Append 1 at the end of the sequence
#     return sequence

# # Function to check if a number is prime
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Create a directed graph
# G = nx.DiGraph()

# # Generate sequences from 500 to 1 and add edges to the graph
# for x in range(500, 0, -1):
#     sequence = generate_sequence(x)
#     for i in range(len(sequence) - 1):
#         G.add_edge(sequence[i], sequence[i + 1])

# # Position nodes using a graph layout
# pos = nx.spring_layout(G, k=0.15, iterations=20)  # Adjust parameters for better spacing

# # Draw nodes and edges
# plt.figure(figsize=(20, 15))
# node_colors = ['red' if is_prime(node) else 'blue' for node in G.nodes()]
# nx.draw_networkx_nodes(G, pos, node_size=50, node_color=node_colors)  # Smaller nodes
# nx.draw_networkx_edges(G, pos, edge_color='lightgrey', arrows=False)  # Light-colored edges without arrows

# # Remove labels
# plt.axis('off')

# # Display the graph
# plt.title("Tree Structure of Sequences with Prime Numbers Highlighted")
# plt.show()


# # import networkx as nx
# # import matplotlib.pyplot as plt

# # # Function to generate the sequence
# # def generate_sequence(start):
# #     num = start
# #     sequence = []
# #     while num != 1:
# #         sequence.append(num)
# #         if num % 2 == 0:
# #             num = num // 2
# #         else:
# #             num = 3 * num + 1
# #     sequence.append(1)  # Append 1 at the end of the sequence
# #     return sequence

# # # Function to check if a number is prime
# # def is_prime(n):
# #     if n <= 1:
# #         return False
# #     for i in range(2, int(n**0.5) + 1):
# #         if n % i == 0:
# #             return False
# #     return True

# # # Create a directed graph
# # G = nx.DiGraph()

# # # Generate sequences from 500 to 1 and add edges to the graph
# # for x in range(2048, 0, -1):
# #     sequence = generate_sequence(x)
# #     for i in range(len(sequence) - 1):
# #         G.add_edge(sequence[i], sequence[i + 1])

# # # Position nodes using a graph layout
# # pos = nx.spring_layout(G, k=0.15, iterations=20)  # Adjust parameters for better spacing

# # # Draw nodes and edges
# # plt.figure(figsize=(20, 15))
# # node_colors = ['lightgreen' if is_prime(node) else 'skyblue' for node in G.nodes()]
# # nx.draw_networkx_nodes(G, pos, node_size=500, node_color=node_colors)
# # nx.draw_networkx_edges(G, pos, arrows=True)
# # nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

# # # Highlight prime nodes
# # prime_nodes = [node for node in G.nodes() if is_prime(node)]
# # nx.draw_networkx_nodes(G, pos, nodelist=prime_nodes, node_color='red', node_size=600)

# # # Display the graph
# # plt.title("Tree Structure of Sequences with Prime Numbers Highlighted")
# # plt.show()


# # # import networkx as nx
# # # import matplotlib.pyplot as plt

# # # # Function to generate the sequence
# # # def generate_sequence(start):
# # #     num = start
# # #     sequence = []
# # #     while num != 1:
# # #         sequence.append(num)
# # #         if num % 2 == 0:
# # #             num = num // 2
# # #         else:
# # #             num = 3 * num + 1
# # #     sequence.append(1)  # Append 1 at the end of the sequence
# # #     return sequence

# # # # Create a directed graph
# # # G = nx.DiGraph()

# # # # Generate sequences from 500 to 1 and add edges to the graph
# # # for x in range(100, 0, -1):
# # #     sequence = generate_sequence(x)
# # #     for i in range(len(sequence) - 1):
# # #         G.add_edge(sequence[i], sequence[i + 1])

# # # # Draw the graph
# # # plt.figure(figsize=(15, 10))
# # # pos = nx.spring_layout(G)  # positions for all nodes
# # # nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=15)
# # # plt.title("Tree Structure of Sequences")
# # # plt.show()
# # # # import csv
# # # # import openpyxl
# # # # from openpyxl.styles import PatternFill

# # # # # Function to generate the sequence
# # # # def generate_sequence(start):
# # # #     num = start
# # # #     sequence = []
# # # #     while num != 1:
# # # #         sequence.append(num)
# # # #         if num % 2 == 0:
# # # #             num = num // 2
# # # #         else:
# # # #             num = 3 * num + 1
# # # #     sequence.append(1)  # Append 1 at the end of the sequence
# # # #     return sequence

# # # # # Function to check if a number is prime
# # # # def is_prime(n):
# # # #     if n <= 1:
# # # #         return False
# # # #     for i in range(2, int(n**0.5) + 1):
# # # #         if n % i == 0:
# # # #             return False
# # # #     return True

# # # # # List to hold all sequences
# # # # all_sequences = []

# # # # # Generate sequences from 500 to 1
# # # # for x in range(1000, 0, -1):
# # # #     sequence = generate_sequence(x)
# # # #     all_sequences.append((x, sequence[::-1]))  # Reverse the sequence

# # # # # Create an Excel workbook and worksheet
# # # # wb = openpyxl.Workbook()
# # # # ws = wb.active
# # # # ws.title = "Sequences"

# # # # # Define a fill pattern for highlighting prime numbers
# # # # highlight_fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")

# # # # # Write sequences to the worksheet
# # # # for x, sequence in all_sequences:
# # # #     ws.append(sequence)
# # # #     if is_prime(x):
# # # #         for cell in ws[f"A{ws.max_row}":f"{openpyxl.utils.get_column_letter(len(sequence))}{ws.max_row}"]:
# # # #             for c in cell:
# # # #                 c.fill = highlight_fill

# # # # # Save the workbook
# # # # wb.save("sequences.xlsx")

# # # # print("Sequences have been written to sequences.xlsx with prime numbers highlighted")

# # # # # import csv

# # # # # # Function to generate the sequence
# # # # # def generate_sequence(start):
# # # # #     num = start
# # # # #     sequence = []
# # # # #     while num != 1:
# # # # #         sequence.append(num)
# # # # #         if num % 2 == 0:
# # # # #             num = num // 2
# # # # #         else:
# # # # #             num = 3 * num + 1
# # # # #     sequence.append(1)  # Append 1 at the end of the sequence
# # # # #     return sequence

# # # # # # List to hold all sequences
# # # # # all_sequences = []

# # # # # # Generate sequences from 500 to 1
# # # # # for x in range(1000, 0, -1):
# # # # #     sequence = generate_sequence(x)
# # # # #     all_sequences.append(sequence[::-1])  # Reverse the sequence

# # # # # # Write sequences to a CSV file
# # # # # with open('sequences.csv', 'w', newline='') as csvfile:
# # # # #     csv_writer = csv.writer(csvfile)
# # # # #     for sequence in all_sequences:
# # # # #         csv_writer.writerow(sequence)

# # # # # print("Sequences have been written to sequences.csv in reverse order")



# # # # # # import csv

# # # # # # # Function to generate the sequence
# # # # # # def generate_sequence(start):
# # # # # #     num = start
# # # # # #     sequence = []
# # # # # #     while num != 1:
# # # # # #         sequence.append(num)
# # # # # #         if num % 2 == 0:
# # # # # #             num = num // 2
# # # # # #         else:
# # # # # #             num = 3 * num + 1
# # # # # #     sequence.append(1)  # Append 1 at the end of the sequence
# # # # # #     return sequence

# # # # # # # List to hold all sequences
# # # # # # all_sequences = []

# # # # # # # Generate sequences from 500 to 1
# # # # # # for x in range(500, 0, -1):
# # # # # #     sequence = generate_sequence(x)
# # # # # #     all_sequences.append(sequence)

# # # # # # # Write sequences to a CSV file
# # # # # # with open('sequences.csv', 'w', newline='') as csvfile:
# # # # # #     csv_writer = csv.writer(csvfile)
# # # # # #     for sequence in all_sequences:
# # # # # #         csv_writer.writerow(sequence)

# # # # # # print("Sequences have been written to sequences.csv")