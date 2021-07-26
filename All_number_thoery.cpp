ll mod = 1e9 + 7;

const int mxn = 1e6 + 7;

vl fact(mxn,0), in (mxn, 0);

ll gcd(ll a, ll b){
    if(b==0) return a;
    return gcd(b, a%b);
}

ll lcm(ll a, ll b){
    return (a*b)/(gcd(a,b));
}

ll mpow(ll base, ll exp){
    ll res = 1;
    while(exp > 0){
        if(exp&1) res = (res*base)%mod;
        base = (base*base) % mod;
        exp >>= 1;
    }
    return res;
}

ll inv(ll v){
    if(v<=1) return v;
    return (inv(mod%v) * (mod - mod/v)) % mod
}

void calc_fact(){
    fact[0] = 1;
    fact[1] = 1;
    in[1] = 1;
    for(ll i=2; i<mxn; i++){
        fact[i] = (fact[i-1] * i)%mod;
        in[i] = (in[i-1] * mpow(i, mod - 2)) %mod;
        // in[i] = (in[i-1] * inv(i) %mod
    }
}

void ncr(ll n, ll r){
    ll ans = fact[n]);
    ans = (ans * in[r])%mod;
    ans = (ans * in[n-r])%mod;
    return ans;
}

ll spf[mxn];

void calc_spf(){
    for(int i=1; i<mxn; i+=2) spf[i] = i;
    for(int i=2; i<mxn; i+=2) spf[i] = 2;

    for(int i = 3; i*i < mxn ; i+=2){
        if(spf[i]==i){
            for(int j = i*i; j<mxn; j+=i){
                spf[j] = min(spf[j], i);
            }
        }
    }
}

vector<ll> calc_primes(ll n){
    vector<ll> p;
    while(n%2 == 0){
        p.push_back(2ll);
        n/=2;
    }
    for(int i=3; i*i <= n; i+=2){
        while(n%i == 0){
            p.push_back(i);
            n/=i;
        }
    }
    if(n > 1) p.push_back(n);

    return p;
}


