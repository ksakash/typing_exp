import json

code_array = [
"""
void print_vector(std::vector<int>& v) {
    for (auto x : v) {
        std::cout << x << " ";
    }
    std::cout << std::endl;
    std::cout << "-----------------" << std::endl;
}
""",
"""
void search(std::vector<int>& v, int k, int n) {
    if (k == n) {
        print_vector(v);
        return;
    }
    search(v, k+1, n);
    v.push_back(k);
    search(v, k+1, n);
    v.pop_back();
}
""",
"""
int main () {
    std::vector<int> v;
    int n = 5;
    for (int b = 0; b < (1 << n); b++) {
        std::vector v;
        for (int i = 0; i < n; i++) {
            if (b & (1 << i)) v.push_back(i);
        }
        print_vector(v);
    }
}
""",
"""
void search(std::vector<int>& permuation, std::vector<int>& choosen, int n) {
    if (permuation.size() == n) {
        print_vector(permuation);
        return;
    }
    for (int i = 0; i < n; i++) {
        if (choosen[i]) continue;
        choosen[i] = true;
        permuation.push_back(i);
        search(permuation, choosen, n);
        permuation.pop_back();
        choosen[i] = false;
    }
}
""",
"""
visited[x] = true;
distance[x] = 0;
q.push(x);
while (!q.empty()) {
    int s = q.front(); q.pop();
    // process node s
    for (auto u : adj[s]) {
        if (visited[u]) continue;
        visited[u] = true;
        distance[u] = distance[s]+1;
        q.push(u);
    }
}
""",
"""
void dfs(int s) {
    if (visited[s]) return;
    visited[s] = true;
    // process node s
    for (auto u: adj[s]) {
        dfs(u);
    }
}
""",
"""
for (int i = 1; i <= n; i++) distance[i] = INF;
    distance[x] = 0;
    for (int i = 1; i <= n-1; i++) {
    for (auto e : edges) {
        int a, b, w;
        tie(a, b, w) = e;
        distance[b] = min(distance[b], distance[a]+w);
    }
}
""",
"""
for (int i = 1; i <= n; i++) distance[i] = INF;
distance[x] = 0;
q.push({0,x});
while (!q.empty()) {
    int a = q.top().second; q.pop();
    if (processed[a]) continue;
    processed[a] = true;
    for (auto u : adj[a]) {
        int b = u.first, w = u.second;
        if (distance[a]+w < distance[b]) {
        distance[b] = distance[a]+w;
        q.push({-distance[b],b});
        }
    }
}
""",
"""
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
        if (i == j) distance[i][j] = 0;
        else if (adj[i][j]) distance[i][j] = adj[i][j];
        else distance[i][j] = INF;
    }
}

for (int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            distance[i][j] = min(distance[i][j],
            distance[i][k]+distance[k][j]);
        }
    }
}
""",
"""
void dfs(int s, int e) {
    count[s] = 1;
    for (auto u : adj[s]) {
        if (u == e) continue;
        dfs(u, s);
        count[s] += count[u];
    }
}
"""
]

arr = []
for code_snippet in code_array:
    code = code_snippet.replace("    ", "\t")
    arr.append(code)

f = open('data.json', 'w+')
json.dump(arr, f, indent=2)
f.close()
