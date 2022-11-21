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
int n = v.size();
for (int i = 0; i < n; i++) {
    while (v[i] > 0 && v[i] <= n && v[i] != v[v[i]-1]) {
        std::swap(v[i], v[v[i]-1]);
    }
}
""",
"""
int char_code = int(input[i] - 'a');
if (prev_char[char_code] == -1 || prev_char[char_code] < prev_pointer) {
    curr_len++;
    max_len = std::max(max_len, curr_len);
    prev_char[char_code] = i;
}
""",
"""
else if (prev_char[char_code] >= prev_pointer) {
    curr_len = i - prev_char[char_code];
    prev_pointer = prev_char[char_code] + 1;
    max_len = std::max(max_len, curr_len);
    prev_char[char_code] = i;
}
""",
"""
for (int j = n-1; j >= 0; j--) {
    for (int i = n-1; i >= j; i--) {
        if (dp[j][i] == 1) {
            if (i - j + 1 > max_len) {
                range = {j, i};
                max_len = i - j + 1;
            }
        }
    }
}
""",
"""
def export(sqlQuery):
    db = connect_db()
    print('Connected to the DB')
    data_array = pd.read_sql(sqlQuery, con=db)
    print('Data fetching complete')
    return data_array
""",
"""
def get_job_name_id(name):
    if name is None:
        name = 'unnamed'
    uuid = str(uuid.uuid4())
    today = (datetime.today() + timedelta(hours=5.5)).strftime('%Y-%m-%d')
    job_name = name + '-' + today + '-' + uuid[:8]
    return (job_name, uuid)
""",
"""
def initialise_dynamic_map(self):
    self.dynamic_function_map = {
        'promotion': self.get_promotion,
        'reviews': self.get_reviews
    }
""",
"""
cat_strs = []
for cat in cat_items:
    cat_str = cat.text.strip()
    cat_strs.append(cat_str)
extracted_category = " > ".join(cat_strs)
""",
"""
product_spec_dict = self.get_product_spec_dict(html_element)
parameters = ['Brand', 'Manufacturer']
for param in parameters:
    if param in product_spec_dict.keys():
        extracted_mfgr = product_spec_dict[param]
        break
""",
"""
mfgr_raw_can = canonicalize(mfgr_raw)
entry = session.query(Mfgr).filter_by(mfgrValue=mfgr_raw_can).first()
if entry is not None:
    m1 = Mfgr(mfgrCanonical_id=entry.id, mfgrValue=mfgr_raw, comment='')
    session.add_all([m1])
    session.commit()
    return m1
""",
"""
m2 = Mfgr(mfgrValue=mfgr_raw_can, comment='')
session.add_all([m2])
session.commit()
m2.mfgrCanonical_id = m2.id
session.commit()
""",
"""
__tablename__ = "ut_availability"
id = Column(Integer, primary_key=True)
site_id = Column(Integer)
stringValue = Column(String(255))
mapper_id = Column(Integer, default=-5)
map_status = Column(Integer, nullable=True)
""",
"""
def get_delivery_time_days_upto(self, html_element):
    delivery_str = self.get_delivery_time_raw(html_element)
    delivery_time_days_upto = self.get_delivery_str_to_int(delivery_str)[1]
    return delivery_time_days_upto

""",
"""
await self.page.wait_for_timeout(1000)
await self.pre_action()
await self.set_location()
await self.page.wait_for_timeout(1000)
await self.page.mouse.wheel(delta_x=0, delta_y=5000)
await self.page.wait_for_timeout(3000)
""",
"""
std::vector<std::string> inputs = {"bb", "bbbbsd", "ababdd", "cbbd"};
for (string s : inputs) {
    std::string ans = longestPalindrome(s);
    cout << "Input: " << s << endl;
    std::cout << "Result: " << ans << std::endl;

}
""",
"""
void print2DArray (std::vector<std::vector<int>>& array) {
    for (auto row : array) {
        for (auto e : row) {
            cout << e << " ";
        }
        cout << endl;
    }
    cout << endl;
}
""",
"""
int char_code = int(input[i] - 'a');
if (prev_char[char_code] == -1 || prev_char[char_code] < prev_pointer) {
    curr_len++;
    max_len = std::max(max_len, curr_len);
    prev_char[char_code] = i;
}
""",
"""
else if (prev_char[char_code] >= prev_pointer) {
    curr_len = i - prev_char[char_code];
    prev_pointer = prev_char[char_code] + 1;
    max_len = std::max(max_len, curr_len);
    prev_char[char_code] = i;
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
""",
"""
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
""",
"""
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

new_arr = []
for a in arr:
    lines = a.split('\n')
    batch_num = 6
    for i in range(0, len(lines), 6):
        batch_lines = lines[i:i+batch_num]
        new_arr.append("\n".join(batch_lines))


file_path = 'data/data.json'
f = open(file_path, 'w+')
json.dump(arr, f, indent=2)
f.close()
