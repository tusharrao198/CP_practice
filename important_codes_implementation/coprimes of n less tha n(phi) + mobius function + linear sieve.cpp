int phi(int n) {          // root(n)
    int result = n;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0)
                n /= i;
            result -= result / i;
        }
    }
    if (n > 1)
        result -= result / n;
    return result;
}

void phi_1_to_n(int n) {
    vector<int> phi(n + 1);
    phi[0] = 0;
    phi[1] = 1;
    for (int i = 2; i <= n; i++)
        phi[i] = i;

    for (int i = 2; i <= n; i++) {
        if (phi[i] == i) {
            for (int j = i; j <= n; j += i)
                phi[j] -= phi[j] / i;
        }
    }
}

void mobius(){  // pta nhi kya bala h code tha to idhar daal diya
    bool is_composite[mxn];
    fill(is_composite, is_composite + mxn, false);
    vi primes;
    mob[1] = 1;
    for(int i=2; i<mxn; i++){
        if(!is_composite[i]){
            primes.push_back(i);
            mob[i] = -1;
        }
        for(int j=0; j < primes.size() && i*primes[j] < mxn; ++j){
            is_composite[i * primes[j]] = true;
            if(i%primes[j] == 0){
                mob[i*primes[j]] = 0; break; 
            }
            else mob[i*primes[j]] = mob[i]*mob[primes[j]];
        }
    }
}