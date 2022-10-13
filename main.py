# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import networkx as nx

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def generate_graph():
    print("in generate_graph")
    scc_file = open('small_scc.txt', 'r')
    g_arr = []
    lines = scc_file.readlines()
    '''
    for line in lines:
        print(line)
        arr = line.split(' ')
        g_arr.append((arr[0], arr[1].strip()))
    print(g_arr)
    G = nx.MultiDiGraph()
    G.add_edges_from(g_arr)
    plt.figure(figsize=(8, 8))
    nx.draw(G, connectionstyle='arc3, rad=0.1')
    plt.show()
    '''
    g_arr = {}
    rev_g_arr = {}
    for line in lines:
        arr = line.split(' ')
        a0 = int(arr[0])
        a1 = int(arr[1].strip())
        try:
            g_arr[a0].append(a1)
            rev_g_arr[a1].append(a0)
        except KeyError:
            g_arr[a0] = [a1]
            rev_g_arr[a1] = [a0]
    print(g_arr)
    print(rev_g_arr)
    return (g_arr, rev_g_arr)

def reverse_graph(graph):
    print('in reverse graph')


explored = [0 for i in range(10)]
finish_time_arr = [0 for i in range(10)]
curr_finish_time = 1


def DFS(graph, i):
    explored[i] = 1
    for arc in graph[i]:
        if explored[arc] == 0:
            DFS(graph, arc)
            finish_time_arr[arc] = curr_finish_time
            curr_finish_time = curr_finish_time + 1

def generate_scc_pass1(graph):
    print("in generate scc pass1")
    for i in range(1, 10):
        if explored[i] == 0:
            DFS(graph, i)
    print(finish_time_arr)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    graph, rev_graph = generate_graph()
    generate_scc_pass1(rev_graph)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
