# include<bits/stdc++.h>
using
namespace
std;
vector < int > adj[5001];
bool
vis[5001];
bool
dfs(int
s, int
e)
{
if (s == e)
return true;
vis[s] = 1;
for (auto x: adj[s])
    {
    if (!vis[x])
    if (dfs(x, e))
    return true;
}
return false;

}
int
main()
{

int
n;
cin >> n;
vector < int > members;
for (int i=0;i < n;i++)
    {
        int
    x;
    cin >> x;
    members.push_back(x);
    }
    int
    e;
    cin >> e;
    for (int i=0;i < e;i++)
        {
            int
        x, y;
        cin >> x >> y;
        adj[x].push_back(y);
        }
        int
        n1, n2;
        cin >> n1 >> n2;
        if (dfs(n1, n2))
            {
                cout << "1";
            }
            else cout << "0";

            }