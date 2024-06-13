/* Input
9
a b
b c
d c
d e 
f c 
g e 
a d 
h g
i h
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

grid mkuf(ll n){
  grid uf(2, vi(n+1, 1));
  fir(n+1) uf[0][i]=i;
  return uf;
}

ll ufgp(grid &uf, ll n){
  ll pr=n;
  while(pr-uf[0][pr]){
    pr=uf[0][pr];
  }
  while(n-pr){
    ll nx=uf[0][n];
    uf[0][n]=pr;
    n=nx;
  }
  return pr;
}

void ufnu(grid &uf, ll a, ll b){
    uf[1][ufgp(uf, a)]+=uf[1][ufgp(uf, b)];
    uf[0][ufgp(uf, b)]=ufgp(uf, a);
    return;
}

void solve(){
  ll n; cin>>n;
  auto uf = mkuf(n);
  char p, q;
  while(cin>>p>>q){
    ufnu(uf, p-'a'+1, q-'a'+1);
  }
  for(int i=1; i<=n; i++){
    if(ufgp(uf, i) != ufgp(uf, 1)){
      cout<<"false\n";
      return;
    }
  }
  cout<<"true\n";
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; //cin>>tt;
  while(tt--) solve();
}

