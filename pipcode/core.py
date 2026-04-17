def practical_1():
    print("""# ===================== Practical 1 =====================
# Aim: To study and implement recursive algorithms using C++ by solving:
# 1. Factorial Computation
# 2. Tower of Hanoi problem

# --------------------- Program 1: Factorial (Recursive) ---------------------
#include <iostream>
using namespace std;

int factorial(int n)
{
    if (n == 0)
        return 1;
    else
        return n * factorial(n - 1);
}

int main()
{
    int num;
    cout << "Enter a number: ";
    cin >> num;

    cout << "Factorial of " << num << " is: " << factorial(num);

    return 0;
}

# --------------------- Program 2: Tower of Hanoi ---------------------
#include <iostream>
using namespace std;

void towerOfHanoi(int n, char from, char to, char aux)
{
    if (n == 1)
    {
        cout << "Move disk 1 from " << from << " to " << to << endl;
        return;
    }
    towerOfHanoi(n - 1, from, aux, to);
    cout << "Move disk " << n << " from " << from << " to " << to << endl;
    towerOfHanoi(n - 1, aux, to, from);
}

int main()
{
    int n;
    cout << "Enter number of disks: ";
    cin >> n;
    cout << "Steps to solve Tower of Hanoi:\\n";
    towerOfHanoi(n, 'A', 'C', 'B');
    return 0;
}
""")
    

def practical_2():
    print("""# ===================== Practical 2 =====================
# Aim: To study and implement non-recursive (iterative) sorting algorithms—Bubble Sort, Insertion Sort, and Selection Sort—using C++.

# --------------------- Program 1: Bubble Sort ---------------------
#include <iostream>
using namespace std;

int main() {
    int n, a[50];
    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter elements:\\n";
    for(int i = 0; i < n; i++)
        cin >> a[i];

    for(int i = 0; i < n - 1; i++) {
        for(int j = 0; j < n - i - 1; j++) {
            if(a[j] > a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }

    cout << "Sorted array:\\n";
    for(int i = 0; i < n; i++)
        cout << a[i] << " ";

    return 0;
}

# --------------------- Program 2: Insertion Sort ---------------------
#include <iostream>
using namespace std;

int main() {
    int n, a[50];
    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter elements:\\n";
    for(int i = 0; i < n; i++)
        cin >> a[i];

    for(int i = 1; i < n; i++) {
        int key = a[i];
        int j = i - 1;

        while(j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }

    cout << "Sorted array:\\n";
    for(int i = 0; i < n; i++)
        cout << a[i] << " ";

    return 0;
}

# --------------------- Program 3: Selection Sort ---------------------
#include <iostream>
using namespace std;

int main() {
    int n, a[50];
    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter elements:\\n";
    for(int i = 0; i < n; i++)
        cin >> a[i];

    for(int i = 0; i < n - 1; i++) {
        int min = i;

        for(int j = i + 1; j < n; j++) {
            if(a[j] < a[min])
                min = j;
        }

        int temp = a[i];
        a[i] = a[min];
        a[min] = temp;
    }

    cout << "Sorted array:\\n";
    for(int i = 0; i < n; i++)
        cout << a[i] << " ";

    return 0;
}
""")
    


def practical_3():
    print("""# ===================== Practical 3 =====================
# Aim: To study and implement Binary Search, Merge Sort, Quick Sort.

# --------------------- Program 1: Binary Search ---------------------
#include <iostream>
using namespace std;

int main() {
    int n, key;
    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];
    cout << "Enter sorted elements:\\n";
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    cout << "Enter element to search: ";
    cin >> key;

    int low = 0, high = n - 1, mid;
    bool found = false;

    while(low <= high) {
        mid = (low + high) / 2;
        if(arr[mid] == key) {
            cout << "Element found at position " << mid + 1;
            found = true;
            break;
        }
        else if(key < arr[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }

    if(!found)
        cout << "Element not found";

    return 0;
}

# --------------------- Program 2: Merge Sort ---------------------
#include <iostream>
using namespace std;

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];

    for(int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for(int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;

    while(i < n1 && j < n2) {
        if(L[i] <= R[j])
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }

    while(i < n1)
        arr[k++] = L[i++];

    while(j < n2)
        arr[k++] = R[j++];
}

void mergeSort(int arr[], int l, int r) {
    if(l < r) {
        int m = (l + r) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];
    cout << "Enter elements:\\n";
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    mergeSort(arr, 0, n - 1);

    cout << "Sorted array:\\n";
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}

# --------------------- Program 3: Quick Sort ---------------------
#include <iostream>
using namespace std;

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for(int j = low; j < high; j++) {
        if(arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if(low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];
    cout << "Enter elements:\\n";
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    quickSort(arr, 0, n - 1);

    cout << "Sorted array:\\n";
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}
""")
    
def practical_4():
    print("""# ===================== Practical 4 =====================
# Aim: To study and implement following problems using Greedy method:
# 1. Fractional Knapsack Problem
# 2. Activity Selection Problem
# 3. Job sequencing with deadline

# --------------------- Program 1: Fractional Knapsack ---------------------
#include <iostream>
#include <algorithm>
using namespace std;

struct Item {
    int profit, weight;
};

bool compare(Item a, Item b) {
    return (double)a.profit / a.weight >
           (double)b.profit / b.weight;
}

int main() {
    int n, capacity;
    cout << "Enter number of items: ";
    cin >> n;

    Item items[n];
    for(int i = 0; i < n; i++) {
        cout << "Enter profit and weight of item " << i+1 << ": ";
        cin >> items[i].profit >> items[i].weight;
    }

    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    sort(items, items + n, compare);

    double totalProfit = 0.0;

    for(int i = 0; i < n && capacity > 0; i++) {
        if(items[i].weight <= capacity) {
            totalProfit += items[i].profit;
            capacity -= items[i].weight;
        } else {
            totalProfit += items[i].profit *
                           ((double)capacity / items[i].weight);
            break;
        }
    }

    cout << "Maximum profit: " << totalProfit;
    return 0;
}

# --------------------- Program 2: Activity Selection ---------------------
#include <iostream>
#include <algorithm>
using namespace std;

struct Activity {
    int start, finish;
};

bool compare(Activity a, Activity b) {
    return a.finish < b.finish;
}

int main() {
    int n;
    cout << "Enter number of activities: ";
    cin >> n;

    Activity act[n];
    for(int i = 0; i < n; i++) {
        cout << "Enter start and finish time of activity " << i+1 << ": ";
        cin >> act[i].start >> act[i].finish;
    }

    sort(act, act + n, compare);

    cout << "Selected activities:\\n";
    int lastFinish = act[0].finish;
    cout << "(" << act[0].start << "," << act[0].finish << ")\\n";

    for(int i = 1; i < n; i++) {
        if(act[i].start >= lastFinish) {
            cout << "(" << act[i].start << "," << act[i].finish << ")\\n";
            lastFinish = act[i].finish;
        }
    }

    return 0;
}

# --------------------- Program 3: Job Sequencing ---------------------
#include <iostream>
#include <algorithm>
using namespace std;

struct Job {
    char id;
    int deadline, profit;
};

bool compare(Job a, Job b) {
    return a.profit > b.profit;
}

int main() {
    int n;
    cout << "Enter number of jobs: ";
    cin >> n;

    Job jobs[n];
    for(int i = 0; i < n; i++) {
        cout << "Enter job id, deadline and profit: ";
        cin >> jobs[i].id >> jobs[i].deadline >> jobs[i].profit;
    }

    sort(jobs, jobs + n, compare);

    int maxDeadline = 0;
    for(int i = 0; i < n; i++)
        maxDeadline = max(maxDeadline, jobs[i].deadline);

    char slot[maxDeadline];
    bool filled[maxDeadline] = {false};

    int totalProfit = 0;

    for(int i = 0; i < n; i++) {
        for(int j = jobs[i].deadline - 1; j >= 0; j--) {
            if(!filled[j]) {
                filled[j] = true;
                slot[j] = jobs[i].id;
                totalProfit += jobs[i].profit;
                break;
            }
        }
    }

    cout << "Job sequence:\\n";
    for(int i = 0; i < maxDeadline; i++)
        if(filled[i])
            cout << slot[i] << " ";

    cout << "\\nTotal profit: " << totalProfit;
    return 0;
}
""")


def practical_5():
    print("""# ===================== Practical 5 =====================
# Aim: To study and implement following problems:
# 1. 0/1 Knapsack Problem
# 2. Coin Change-Making Problem
# 3. Weighted Job Scheduling Problem

# --------------------- Program 1: 0/1 Knapsack ---------------------
#include <iostream>
using namespace std;

int max(int a, int b) {
    return (a > b) ? a : b;
}

int main() {
    int n, W;
    cout << "Enter number of items: ";
    cin >> n;

    int wt[n], val[n];
    for(int i = 0; i < n; i++) {
        cout << "Enter weight and profit of item " << i+1 << ": ";
        cin >> wt[i] >> val[i];
    }

    cout << "Enter knapsack capacity: ";
    cin >> W;

    int dp[n+1][W+1];

    for(int i = 0; i <= n; i++) {
        for(int w = 0; w <= W; w++) {
            if(i == 0 || w == 0)
                dp[i][w] = 0;
            else if(wt[i-1] <= w)
                dp[i][w] = max(val[i-1] +
                               dp[i-1][w - wt[i-1]],
                               dp[i-1][w]);
            else
                dp[i][w] = dp[i-1][w];
        }
    }

    cout << "Maximum profit: " << dp[n][W];
    return 0;
}

# --------------------- Program 2: Coin Change ---------------------
#include <iostream>
#include <climits>
using namespace std;

int min(int a, int b) {
    return (a < b) ? a : b;
}

int main() {
    int n, amount;
    cout << "Enter number of coin types: ";
    cin >> n;

    int coins[n];
    cout << "Enter coin denominations:\\n";
    for(int i = 0; i < n; i++)
        cin >> coins[i];

    cout << "Enter amount: ";
    cin >> amount;

    int dp[amount + 1];
    dp[0] = 0;

    for(int i = 1; i <= amount; i++)
        dp[i] = INT_MAX;

    for(int i = 1; i <= amount; i++) {
        for(int j = 0; j < n; j++) {
            if(coins[j] <= i && dp[i - coins[j]] != INT_MAX)
                dp[i] = min(dp[i], dp[i - coins[j]] + 1);
        }
    }

    cout << "Minimum coins required: " << dp[amount];
    return 0;
}

# --------------------- Program 3: Weighted Job Scheduling ---------------------
#include <iostream>
#include <algorithm>
using namespace std;

struct Job {
    int start, finish, profit;
};

bool compare(Job a, Job b) {
    return a.finish < b.finish;
}

int main() {
    int n;
    cout << "Enter number of jobs: ";
    cin >> n;

    Job jobs[n];
    for(int i = 0; i < n; i++) {
        cout << "Enter start, finish and profit: ";
        cin >> jobs[i].start >> jobs[i].finish >> jobs[i].profit;
    }

    sort(jobs, jobs + n, compare);

    int dp[n];
    dp[0] = jobs[0].profit;

    for(int i = 1; i < n; i++) {
        int incl = jobs[i].profit;

        for(int j = i - 1; j >= 0; j--) {
            if(jobs[j].finish <= jobs[i].start) {
                incl += dp[j];
                break;
            }
        }

        dp[i] = max(incl, dp[i - 1]);
    }

    cout << "Maximum profit: " << dp[n - 1];
    return 0;
}
""")
    

def practical_6():
    print("""# ===================== Practical 6 =====================
# Aim: To study and implement following algorithms to find the shortest path:
# 1. Bellman–Ford Algorithm
# 2. Floyd–Warshall Algorithm
# 3. Travelling Salesman Problem (TSP)

# --------------------- Program 1: Bellman–Ford ---------------------
#include <iostream>
#include <climits>
using namespace std;

struct Edge {
    int src, dest, weight;
};

int main() {
    int V, E;
    cout << "Enter number of vertices and edges: ";
    cin >> V >> E;

    Edge edges[E];
    for(int i = 0; i < E; i++) {
        cout << "Enter source, destination and weight: ";
        cin >> edges[i].src >> edges[i].dest >> edges[i].weight;
    }

    int src;
    cout << "Enter source vertex: ";
    cin >> src;

    int dist[V];
    for(int i = 0; i < V; i++)
        dist[i] = INT_MAX;
    dist[src] = 0;

    for(int i = 1; i <= V - 1; i++) {
        for(int j = 0; j < E; j++) {
            int u = edges[j].src;
            int v = edges[j].dest;
            int w = edges[j].weight;

            if(dist[u] != INT_MAX && dist[u] + w < dist[v])
                dist[v] = dist[u] + w;
        }
    }

    for(int j = 0; j < E; j++) {
        if(dist[edges[j].src] != INT_MAX &&
           dist[edges[j].src] + edges[j].weight < dist[edges[j].dest]) {
            cout << "Graph contains negative weight cycle";
            return 0;
        }
    }

    cout << "Vertex   Distance from Source\\n";
    for(int i = 0; i < V; i++)
        cout << i << "\\t\\t" << dist[i] << endl;

    return 0;
}

# --------------------- Program 2: Floyd–Warshall ---------------------
#include <iostream>
#include <climits>
using namespace std;

#define INF 99999

int main() {
    int V;
    cout << "Enter number of vertices: ";
    cin >> V;

    int dist[V][V];
    cout << "Enter adjacency matrix (use 99999 for INF):\\n";

    for(int i = 0; i < V; i++)
        for(int j = 0; j < V; j++)
            cin >> dist[i][j];

    for(int k = 0; k < V; k++)
        for(int i = 0; i < V; i++)
            for(int j = 0; j < V; j++)
                if(dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];

    cout << "Shortest distance matrix:\\n";
    for(int i = 0; i < V; i++) {
        for(int j = 0; j < V; j++) {
            if(dist[i][j] == INF)
                cout << "INF ";
            else
                cout << dist[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}

# --------------------- Program 3: Travelling Salesman Problem ---------------------
#include <iostream>
#include <climits>
using namespace std;

#define N 4
#define INF 99999

int dist[N][N] = {
    {0, 10, 15, 20},
    {10, 0, 35, 25},
    {15, 35, 0, 30},
    {20, 25, 30, 0}
};

int dp[1 << N][N];

int tsp(int mask, int pos) {
    if(mask == (1 << N) - 1)
        return dist[pos][0];

    if(dp[mask][pos] != -1)
        return dp[mask][pos];

    int ans = INF;

    for(int city = 0; city < N; city++) {
        if((mask & (1 << city)) == 0) {
            int newAns = dist[pos][city] +
                         tsp(mask | (1 << city), city);
            ans = min(ans, newAns);
        }
    }

    return dp[mask][pos] = ans;
}

int main() {
    for(int i = 0; i < (1 << N); i++)
        for(int j = 0; j < N; j++)
            dp[i][j] = -1;

    cout << "Minimum travelling cost: " << tsp(1, 0);
    return 0;
}
""")


def practical_7():
    print("""# ===================== Practical 7 =====================
# Aim: To study and implement following algorithms/Problems:
# 1. String Matching (Naïve Method)
# 2. Subset Sum Problem
# 3. 8-Queens Problem

# --------------------- Program 1: String Matching ---------------------
#include <iostream>
#include <string>
using namespace std;

int main() {
    string text, pattern;
    cout << "Enter text: ";
    cin >> text;
    cout << "Enter pattern: ";
    cin >> pattern;

    int n = text.length();
    int m = pattern.length();
    bool found = false;

    for(int i = 0; i <= n - m; i++) {
        int j;
        for(j = 0; j < m; j++) {
            if(text[i + j] != pattern[j])
                break;
        }
        if(j == m) {
            cout << "Pattern found at position " << i << endl;
            found = true;
        }
    }

    if(!found)
        cout << "Pattern not found";

    return 0;
}

# --------------------- Program 2: Subset Sum ---------------------
#include <iostream>
using namespace std;

int n, target;
int arr[10];

void subsetSum(int index, int sum) {
    if(sum == target) {
        cout << "Subset found\\n";
        return;
    }
    if(index == n || sum > target)
        return;

    subsetSum(index + 1, sum + arr[index]);
    subsetSum(index + 1, sum);
}

int main() {
    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter elements:\\n";
    for(int i = 0; i < n; i++)
        cin >> arr[i];

    cout << "Enter target sum: ";
    cin >> target;

    subsetSum(0, 0);
    return 0;
}

# --------------------- Program 3: 8-Queens Problem ---------------------
#include <iostream>
using namespace std;

int board[8][8];

bool isSafe(int row, int col) {
    for(int i = 0; i < col; i++)
        if(board[row][i])
            return false;

    for(int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if(board[i][j])
            return false;

    for(int i = row, j = col; i < 8 && j >= 0; i++, j--)
        if(board[i][j])
            return false;

    return true;
}

bool solve(int col) {
    if(col >= 8)
        return true;

    for(int i = 0; i < 8; i++) {
        if(isSafe(i, col)) {
            board[i][col] = 1;
            if(solve(col + 1))
                return true;
            board[i][col] = 0;
        }
    }
    return false;
}

int main() {
    if(solve(0)) {
        cout << "One solution:\\n";
        for(int i = 0; i < 8; i++) {
            for(int j = 0; j < 8; j++)
                cout << board[i][j] << " ";
            cout << endl;
        }
    } else {
        cout << "No solution exists";
    }
    return 0;
}
""")


def practical_8():
    print("""# ===================== Practical 8 =====================
# Aim: To study and implement following algorithms/Problems:
# 1. N-Queens Problem
# 2. Graph Coloring Problem
# 3. Hamiltonian Cycle Problem

# --------------------- Program 1: N-Queens ---------------------
#include <iostream>
using namespace std;

int board[10][10], N;

bool isSafe(int row, int col) {
    for (int i = 0; i < col; i++)
        if (board[row][i]) return false;

    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j]) return false;

    for (int i = row, j = col; i < N && j >= 0; i++, j--)
        if (board[i][j]) return false;

    return true;
}

bool solve(int col) {
    if (col >= N) return true;

    for (int i = 0; i < N; i++) {
        if (isSafe(i, col)) {
            board[i][col] = 1;
            if (solve(col + 1)) return true;
            board[i][col] = 0;
        }
    }
    return false;
}

int main() {
    cout << "Enter number of queens: ";
    cin >> N;

    if (solve(0)) {
        cout << "Solution:\\n";
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)
                cout << board[i][j] << " ";
            cout << endl;
        }
    } else {
        cout << "No solution exists";
    }
    return 0;
}

# --------------------- Program 2: Graph Coloring ---------------------
#include <iostream>
using namespace std;

int graph[10][10], color[10], n, m;

bool isSafe(int v, int c) {
    for (int i = 0; i < n; i++)
        if (graph[v][i] && color[i] == c)
            return false;
    return true;
}

bool graphColoring(int v) {
    if (v == n) return true;

    for (int c = 1; c <= m; c++) {
        if (isSafe(v, c)) {
            color[v] = c;
            if (graphColoring(v + 1)) return true;
            color[v] = 0;
        }
    }
    return false;
}

int main() {
    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter adjacency matrix:\\n";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> graph[i][j];

    cout << "Enter number of colors: ";
    cin >> m;

    if (graphColoring(0)) {
        cout << "Coloring Solution:\\n";
        for (int i = 0; i < n; i++)
            cout << "Vertex " << i << " -> Color " << color[i] << endl;
    } else {
        cout << "No solution exists";
    }
    return 0;
}

# --------------------- Program 3: Hamiltonian Cycle ---------------------
#include <iostream>
using namespace std;

int graph[10][10], path[10], n;

bool isSafe(int v, int pos) {
    if (!graph[path[pos - 1]][v]) return false;

    for (int i = 0; i < pos; i++)
        if (path[i] == v) return false;

    return true;
}

bool hamiltonian(int pos) {
    if (pos == n) {
        return graph[path[pos - 1]][path[0]];
    }

    for (int v = 1; v < n; v++) {
        if (isSafe(v, pos)) {
            path[pos] = v;
            if (hamiltonian(pos + 1)) return true;
            path[pos] = -1;
        }
    }
    return false;
}

int main() {
    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter adjacency matrix:\\n";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> graph[i][j];

    for (int i = 0; i < n; i++) path[i] = -1;
    path[0] = 0;

    if (hamiltonian(1)) {
        cout << "Hamiltonian Cycle:\\n";
        for (int i = 0; i < n; i++)
            cout << path[i] << " ";
        cout << path[0];
    } else {
        cout << "No Hamiltonian Cycle exists";
    }
    return 0;
}
""")


def practical_9():
    print("""# ===================== Practical 9 =====================
# Aim: To study and implement LIFO node selection using a Stack and FIFO node selection using a Queue.

# --------------------- Program 1: LIFO using Stack ---------------------
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    int n, x;

    cout << "Enter number of nodes: ";
    cin >> n;

    cout << "Enter node values:\\n";
    for (int i = 0; i < n; i++) {
        cin >> x;
        s.push(x);
    }

    cout << "LIFO Node Selection Order:\\n";
    while (!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }

    return 0;
}

# --------------------- Program 2: FIFO using Queue ---------------------
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    int n, x;

    cout << "Enter number of nodes: ";
    cin >> n;

    cout << "Enter node values:\\n";
    for (int i = 0; i < n; i++) {
        cin >> x;
        q.push(x);
    }

    cout << "FIFO Node Selection Order:\\n";
    while (!q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }

    return 0;
}
""")


def practical_10():
    print("""# ===================== Practical 10 =====================
# Aim: To solve the 0/1 Knapsack Problem using FIFO and Least Cost (LC) Branch and Bound approach,
# and Travelling Salesman Problem (TSP) using Least Cost Branch and Bound approach.

# --------------------- Program 1: 0/1 Knapsack (LC Branch & Bound) ---------------------
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int level, profit, weight;
    float bound;
};

int n, W;
int wt[10], val[10];

float bound(Node u) {
    if (u.weight >= W) return 0;

    float profit_bound = u.profit;
    int j = u.level + 1;
    int totweight = u.weight;

    while (j < n && totweight + wt[j] <= W) {
        totweight += wt[j];
        profit_bound += val[j];
        j++;
    }

    if (j < n)
        profit_bound += (W - totweight) * ((float)val[j] / wt[j]);

    return profit_bound;
}

int knapsackLC() {
    priority_queue<pair<float, Node>> pq;

    Node u, v;
    u.level = -1;
    u.profit = u.weight = 0;
    u.bound = bound(u);

    pq.push({u.bound, u});

    int maxProfit = 0;

    while (!pq.empty()) {
        u = pq.top().second;
        pq.pop();

        if (u.bound > maxProfit) {
            v.level = u.level + 1;

            v.weight = u.weight + wt[v.level];
            v.profit = u.profit + val[v.level];

            if (v.weight <= W && v.profit > maxProfit)
                maxProfit = v.profit;

            v.bound = bound(v);
            if (v.bound > maxProfit)
                pq.push({v.bound, v});

            v.weight = u.weight;
            v.profit = u.profit;
            v.bound = bound(v);

            if (v.bound > maxProfit)
                pq.push({v.bound, v});
        }
    }

    return maxProfit;
}

int main() {
    cout << "Enter number of items: ";
    cin >> n;

    cout << "Enter weights and profits:\\n";
    for (int i = 0; i < n; i++)
        cin >> wt[i] >> val[i];

    cout << "Enter knapsack capacity: ";
    cin >> W;

    cout << "Maximum Profit (LC Branch & Bound): "
         << knapsackLC();

    return 0;
}

# --------------------- Program 2: TSP (LC Branch & Bound) ---------------------
#include <bits/stdc++.h>
using namespace std;

#define INF 9999
int n = 4;

int tsp(int graph[][4]) {
    vector<int> perm = {1, 2, 3};
    int min_cost = INF;

    do {
        int cost = graph[0][perm[0]] +
                   graph[perm[0]][perm[1]] +
                   graph[perm[1]][perm[2]] +
                   graph[perm[2]][0];

        min_cost = min(min_cost, cost);
    } while (next_permutation(perm.begin(), perm.end()));

    return min_cost;
}

int main() {
    int graph[4][4] = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };

    cout << "Minimum travelling cost: "
         << tsp(graph);

    return 0;
}
""")

def show_all_practicals():
    print("""===================== ALL PRACTICALS =====================

Practical 1:
- Factorial (Recursion)
- Tower of Hanoi

Practical 2:
- Bubble Sort
- Insertion Sort
- Selection Sort

Practical 3:
- Binary Search
- Merge Sort
- Quick Sort

Practical 4:
- Fractional Knapsack
- Activity Selection
- Job Sequencing with Deadline

Practical 5:
- 0/1 Knapsack (Dynamic Programming)
- Coin Change Problem
- Weighted Job Scheduling

Practical 6:
- Bellman-Ford Algorithm
- Floyd-Warshall Algorithm
- Travelling Salesman Problem (TSP)

Practical 7:
- String Matching (Naïve)
- Subset Sum Problem
- 8-Queens Problem

Practical 8:
- N-Queens Problem
- Graph Coloring
- Hamiltonian Cycle

Practical 9:
- LIFO using Stack
- FIFO using Queue

Practical 10:
- 0/1 Knapsack (Branch & Bound - LC)
- Travelling Salesman Problem (Branch & Bound)

============================================================
""")


