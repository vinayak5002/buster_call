import heapq
INF = 10**10

V, E, r = map(int,input().split())
adj = [[] for i in range(V)] # 隣接リスト

for e in range(E):
    s, t, d = map(int,input().split())
    adj[s].append((t,d))

dists  = [INF for i in range(V)] # 重みの和
dists[r] = 0
pq = [(0, r)] # 二分ヒープの実体はリストやタプルとして表現する
　            # (重みの和, ノード番号)
while(pq):
    d, node = heapq.heappop(pq)
    if (d > dists[node]): # 探索の対象にする必要があるか確認
        continue
    for next, cost in adj[node]:
        if d + cost < dists[next]:# 探索の対象にする必要があるか確認
            dists[next] = d + cost # 次のノードにおける重みの和
            heapq.heappush(pq, (dists[next],next))
for d in dists:
    if d == INF:
        print ('INF')
    else:
        print (d)
