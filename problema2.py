from queue import PriorityQueue, Queue

def main():
    n, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    depth = [0] * n
    parent = [ -1 ] * n
    q = Queue()
    q.put(0)
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                q.put(v)
    
    pq = PriorityQueue()
    for i in range(n):
        pq.put((-depth[i], i))
    
    used = [False] * n
    groups = 0
    
    while not pq.empty():
        _, u = pq.get()
        if not used[u]:
            count = 0
            current = u
            while current != -1 and count < k and not used[current]:
                used[current] = True
                count += 1
                current = parent[current]
            if count == k:
                groups += 1
    
    print(groups)

if __name__ == '__main__':
    main()
