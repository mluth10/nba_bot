import math

def arbitrage(tuples):
    graph = []
    v_set = set()

    for tuple in tuples:
        graph.append([tuple[0], tuple[1], -1*math.log(tuple[2])])
        v_set.add(tuple[0])
        v_set.add(tuple[1])
    
    V = len(v_set)
    dist = {}
    path = {}
    for v in v_set:
        dist[v] = float("Inf")
        path[v] = []
    
    dist[v_set[0]] = 0 # make one random node the starting node


    for _ in range(0, V):
        for start, end, weight in graph:
            


if __name__ == "__main__":
    tuples = []
    tuples.append((1, 2, 130))
    tuples.append((2, 3, .006))
    tuples.append((3, 1, 1.3))
    arbitrage(tuples)