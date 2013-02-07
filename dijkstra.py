#coding: utf-8

"""
start  10  10
     A── B ──C
 20／＼       ＼20
 ／   30        ＼
D       ＼        E
  ＼20    ＼     ／
    ＼      ＼ ／20
      F── G ──H
       10   10
"""
graph = [[ 0, 10,  0, 20,  0,  0,  0, 30],   # A (0)
         [10,  0, 10,  0,  0,  0,  0,  0],   # B (1)
         [ 0, 10,  0,  0, 20,  0,  0,  0],   # C (2)
         [20,  0,  0,  0,  0, 20,  0,  0],   # D (3)
         [ 0,  0, 20,  0,  0,  0,  0, 20],   # E (4)
         [ 0,  0,  0, 20,  0,  0, 10,  0],   # F (5)
         [ 0,  0,  0,  0,  0, 10,  0, 10],   # G (6)
         [30,  0,  0,  0, 20,  0, 10,  0]    # H (7)
         ]

MAX_SIZE = len(graph)
INF = 10000
rest = set(range(MAX_SIZE))
dist = [INF] * MAX_SIZE
prev = [None] * MAX_SIZE

buf = []

def dijkstra(g, start, goal):
    dist[start] = 0
    while len(rest) > 0:
        min_ = INF
        idx = None
        for u in rest:                  # i: vertex in "rest" with smallest dist.
            if dist[u] <= min_:
                min_ = dist[u]
                idx = u
        rest.remove(idx)
        if min_ == INF:
            break

        for v,d in enumerate(g[idx]):
            if d > 0:
                alt = dist[idx] + d       # v: distance from index
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = idx

    # import ipdb; ipdb.set_trace()
    return dist[goal]
    
print "Distance:",dijkstra(graph, 0,4)
        
