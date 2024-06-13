/* 
Input, starts with number of nodes and edges, then all edges.
---
9 10
a b 7
b c 3
d c 4
d e 1
f c 6
g e 3
a d 5
h g 8
i h 9
c h 14
---
*/
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using vi = vector<ll>;
using pii = pair<ll, ll>;
using grid = vector<vi>;

#define sz(_O) _O.size()
#define fix(_O) cout<<setprecision(_O)<<fixed
#define fir(_O) for(int i=0; i<_O; ++i)
#define fjr(_O) for(int j=0; j<_O; ++j)

ll const inf = 2e9;
ll const mod = 998244353;

vector<vector<pii>> mkwgph(ll cn, ll ce){
  vector<vector<pii>> edg(cn+1, vector<pii>(0));

  char fr, to; ll wt;
  fir(ce){
    cin>>fr>>to>>wt;
    edg[fr-'a'+1].push_back({to-'a'+1, wt});
    edg[to-'a'+1].push_back({fr-'a'+1, wt});
  }
  return edg; 
}

vi sssd(vector<vector<pii>> &edg, ll sn){ //dijkstras' alg
  vi ssd(edg.size(), LLONG_MAX), vis(edg.size(), 0);
  priority_queue<pii> cll;
  ssd[sn]=0; cll.push({0, sn});

  while(!cll.empty()){
    auto [wt0, at]=cll.top(); cll.pop(); vis[at]=1;
    if(-wt0>ssd[at]) continue;
    for(auto [to, wt]: edg[at]){
      ll d=wt+ssd[at];
      if(d<ssd[to]){
        ssd[to]=d;
        cll.push({-d, to});
      }
    }
  }
  return ssd;
}

void solve(){
  char start = 'a', end = 'i';
  ll n, m; cin>>n>>m;
  auto edg = mkwgph(n, m);
  vi distances = sssd(edg, start-'a'+1);
  cout<<distances[end-'a'+1]<<endl;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}

