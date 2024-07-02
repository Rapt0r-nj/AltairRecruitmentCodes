import heapq

n, m = map(int, input().split())
inf = 0x3f3f3f3f3f3f

def dijk(st, en, edg):
    dist = {i: inf for i in range (1, n+1)}
    part = {i: None for i in range (1, n+1)}
    dist[st] = 0

    pq = [(0, st)]
    while pq:
        od, fr = heapq.heappop(pq)
        if od>dist[fr]:
            continue
        for to, wt in edg[fr]:
            nd = od+wt
            if(nd<dist[to]):
                dist[to]=nd
                part[to]=fr
                heapq.heappush(pq, (nd, to))

    path = []
    node = n

    if dist[n]==inf:
        return -1
    while node:
        path.append(node)
        node = part[node]
    path.reverse()
    return path


edg = {i: [] for i in range (1, n+1)}

for _O in range (m):
    fr, to, wt = map(int, input().split())
    edg[fr].append((to, wt))
    edg[to].append((fr, wt))

path = dijk(1, n, edg)
print(path)

