const int N = 2e5 + 5;
const int Q = 2e5 + 5;
const int M = 1e6 + 5;
const int SZ = sqrt(N) + 1;
 
struct data
{
    int l, r, idx;
}qr[Q];
 
ll n, q, a[N];
ll freq[M];
ll counter[N]={0};
ll ans[Q];
ll cur_max=0;
 
bool comp(struct data &d1, struct data &d2){
    int b1 = d1.l / SZ;
    int b2 = d2.l / SZ;
    if(b1 != b2)
        return b1 < b2;
    else
        return d1.r < d2.r;
}
 
void add(int x){    
    int x_freq = freq[x];
    counter[x_freq]--;
    freq[x]++;
    counter[freq[x]]++;
    cur_max = max(cur_max,freq[x]);
}
 
void remove(int x){   
    counter[freq[x]]--;
    freq[x]--;
    counter[freq[x]]++;
    while(counter[cur_max]==0){
        cur_max--;
    }
}
 
void mo(){
    sort(qr + 1, qr + q + 1, comp);
    int l = 1, r = 0;
    for(int i=1;i<=q;i++)
    {   
        while(l < qr[i].l) remove(a[l++]);
        while(l > qr[i].l) add(a[--l]);
        while(r < qr[i].r) add(a[++r]);
        while(r > qr[i].r) remove(a[r--]);
        ans[qr[i].idx] = cur_max;
    }
}

void solve(){
    for(int i=1;i<=q;i++)
        {
            cin>>qr[i].l>>qr[i].r;
            qr[i].l++; qr[i].r++;
            qr[i].idx=i;
        }
        mo()
    }
}