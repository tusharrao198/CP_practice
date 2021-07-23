#include <numeric>
#include <iostream>
#include <bits/stdc++.h>
#define mod long(1e9+7)

long multiply(long a,long b){
    a%= mod;b%= mod;
    return (a*b)%mod;
}

void inverseModulo(long a,long m,long *x,long *y){ //ax congruent to 1 mod m

    if(!a){
        *x=0;
        *y=1;
        return ;
    }
    long x1,y1;
    inverseModulo(m%a,a,&x1,&y1);
    *x=y1-(m/a)*x1;
    *y=x1;
    return;
}

long moduloDivision(long a,long b,long m){  // (a*(returnValue))mod m congruent to b mod m
    //https://www.geeksforgeeks.org/modular-division/ and https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
    long x,y;
    inverseModulo(b, m, &x, &y);
    x%=m;
    return (x*a)%m;
}

long power(long n,long r){ //calculates (n^r)%mod in logarithmic time
    if(r==0) return 1;
    if(r==1) return n;
    if(r%2){
        auto tmp=power(n, (r-1)/2);
        return multiply(multiply(n,tmp),tmp);
    }
    auto tmp=power(n, r/2);
    return multiply(tmp, tmp);
}
long sumOfAGPSeries(long a,long d,long b,long r,long n){
    if(r==1) return multiply(n, multiply(a, 2)+multiply(n-1, d))/2;
    long left=multiply(multiply(d, r), power(r,n-1)-1);
    left=a+moduloDivision(left,r-1,mod);
    left=multiply(left, b);
    left%=mod;
    long right=multiply(multiply(b, power(r, n)), a+multiply(n-1, d));
    long ans=right-left;
    ans=(ans%mod + mod) % mod;
    return moduloDivision(ans,r-1,mod);

}
signed main(){
    long N=3;
    long ans = 0;
    long bitCountOfN = log2(N) + 1;
    long nearestPowerOfTwo = pow(2, bitCountOfN - 1);
    long startOfGP = 0;
    while (nearestPowerOfTwo) { // iterating over each arithmetico–geometric sequence
        long a, d, b, r, n;
        a = N;
        d = -1;
        b = power(2, startOfGP);
        r = power(2, bitCountOfN);
        n = N - nearestPowerOfTwo + 1;
        ans += sumOfAGPSeries(a, d, b, r, n);
        ans %= mod;
        startOfGP += n * bitCountOfN;
        N = nearestPowerOfTwo - 1;
        nearestPowerOfTwo >>= 1;
        bitCountOfN--;
    }
    std::cout << ans << std::endl;
    return 0;
}
