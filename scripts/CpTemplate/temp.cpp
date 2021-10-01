#include <bits/stdc++.h>


#define ll long  long
#define ld long double
#define mod 1000000007
#define inf LLONG_MAX
#define pb push_back
#define ff first
#define ss second
#define all(x) x.begin(),x.end()
#define FOR(i, a, b)    for(int i=a; i<b; i++)
#define FORrev(i,a,b)  for(int i= a-1; i>=b; i--)
#define vll vector <ll> 
#define pll pair<ll, ll> 
#define vpll vector <pll>
#define input(a,n) FOR(i,0,n) cin>>a[i]
#define mems(x, y) memset(x, y, sizeof(x))
#define ThisIsDragonDen ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);

using namespace std;

//------------------------------------


const int MAX_N = 200000;
int test;

void solve(){
    // cout.precision(10);
    // cout << fixed;
    // priority_queue <int, vector<int>, greater<int> > pq;

    ll n;
    cin >> n;



}
int main(){
    ThisIsDragonDen
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin); 
        freopen("output.txt", "w", stdout); 
    #else
        //online submission
    #endif
    clock_t tStart = clock();
    test = 1;
    cin >> test;
    FOR(i,1,test + 1){  
        solve();
    }
    cerr << "Completed in: "<< (double)((clock() - tStart)*1000)/CLOCKS_PER_SEC<<" ms"<< endl;
    return 0;
}
/*
    When nothing works, use Brute Force
    author: DragonDen
*/
