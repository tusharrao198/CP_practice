int Solution::pow(int x, int n, int d) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    if (n == 0){
        return 1 % d;
    } 

    long long res = 1;
    while(n > 0){
        if(n&1) res = (res*x)%d;
        x = (x*x) % d;
        n >>= 1;
    }

    // long long ans = res % d;
    if (ans<0) {
        return (ans + d) %d;
    }
    return ans;



}
