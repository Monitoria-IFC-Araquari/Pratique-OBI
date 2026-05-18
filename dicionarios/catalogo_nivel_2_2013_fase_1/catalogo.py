import sys

n = int(sys.stdin.readline())
trie = {}
files = []

for _ in range(n):
    path = sys.stdin.readline().strip().split('/')
    files.append(path)
    node = trie
    for p in path:
        if p not in node:
            node[p] = {}
        node = node[p]

total = 0
for path in files:
    total += len(''.join(path)) + len(path) - 1

def solve(node, depth, saved):
    global total
    child_save = 0
    max_save = 0
    for ch in node:
        if node[ch]:
            child_save = max(child_save, solve(node[ch], depth + len(ch) + 1, 0))
    max_save = max(max_save, child_save)
    can_save = depth + max_save
    if depth > 0:
        for ch in node:
            if node[ch]:
                can_save = max(can_save, solve(node[ch], depth + len(ch) + 1, 1))
    return max(can_save, max_save)

best_save = solve(trie, 0, 0)

# Actually, I need to compute the answer differently
# The answer is: total_chars - max_savable
# Let me recompute

import sys
sys.setrecursionlimit(1 << 20)

n = int(sys.stdin.readline())
trie = {}

total = 0
for _ in range(n):
    parts = sys.stdin.readline().strip().split('/')
    total += sum(len(p) for p in parts) + len(parts) - 1
    node = trie
    for p in parts:
        if p not in node:
            node[p] = {}
        node = node[p]

best = [0]
def dfs(node, depth):
    max_child = 0
    for ch in node:
        if node[ch]:
            max_child = max(max_child, dfs(node[ch], depth + len(ch) + 1))
    save_at_this = depth + max_child
    best[0] = max(best[0], save_at_this)
    return len(ch) + 1 + max_child if depth > 0 else 0

for ch in trie:
    dfs(trie[ch], 0)

print(total - best[0])
