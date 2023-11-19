import networkx as nx
import matplotlib.pyplot as plt

def DFSUtil(G, v, visited, sl):
    visited[v] = True
    sl.append(v)
    for i in G[v]:
        if not visited[i]:
            DFSUtil(G, i, visited, sl)
    return sl

def DFS(G, source):
    visited = [False] * len(G.nodes())
    sl = []
    dfs_stk = []
    dfs_stk.append(DFSUtil(G, source, visited, sl))
    for i in range(len(G.nodes())):
        if not visited[i]:
            sl = []
            dfs_stk.append(DFSUtil(G, i, visited, sl))
    return dfs_stk

def CreateGraph():
    G = nx.DiGraph()
    f = open('input.txt')
    n = int(f.readline())
    wtMatrix = []
    for _ in range(n):
        list1 = list(map(int, f.readline().split()))
        wtMatrix.append(list1)
    source = int(f.readline())
    for i in range(n):
        for j in range(n):
            if wtMatrix[i][j] > 0:
                G.add_edge(i, j, length=wtMatrix[i][j])
    return G, source

def DrawDFSPath(G, dfs_stk):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    edge_labels = dict([((u, v,), d['length']) for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=11)
    for i in dfs_stk:
        if len(i) > 1:
            for j in i[:(len(i) - 1)]:
                if i[i.index(j) + 1] in G[j]:
                    nx.draw_networkx_edges(G, pos, edgelist=[(j, i[i.index(j) + 1])], width=2.5, alpha=0.6, edge_color='r')
                else:
                    for k in i[1::-1]:
                        if k in G[j]:
                            nx.draw_networkx_edges(G, pos, edgelist=[(j, k)], width=2.5, alpha=0.6, edge_color='r')
                            break

if __name__ == "__main__":
    G, source = CreateGraph()
    dfs_stk = DFS(G, source)
    if dfs_stk:
        DrawDFSPath(G, dfs_stk)
        plt.show()
    else:
        print("DFS traversal not found.")
