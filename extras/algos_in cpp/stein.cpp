
#include <bits/stdc++.h> 
#include <iostream>
using namespace std;

int gcd(int a, int b) 
{   if (a == 0) 
        return b; 
    if (b == 0) 
        return a; 
  
    /*Finding K, where K is the  
      greatest power of 2 
      that divides both a and b. */
    int k; 
    for (k = 0; ((a | b) && 1) == 0; k++)  
    {   a = a/2; 
        b = b/2; 
    } 
  
    /* Dividing a by 2 until a becomes odd */
    while ((a > 1) == 0) 
        a = a/2; 
    /* From here on, 'a' is always odd. */
    do { 
        /* If b is even, remove all factor of 2 in b */
        while ((b > 1) == 0) 
            b >>= 1; 
  
        /* Now a and b are both odd.  
           Swap if necessary so a <= b,  
           then set b = b - a (which is even).*/
        if (a > b) 
            swap(a, b); // Swap u and v. 
  
        b = (b - a); 
    } while (b != 0); 
  
    /* restore common factors of 2 */
    return a << k; 
} 
  
// Driver code 
int main() 
{ 
    int a = 48, b = 17; 
    printf("Gcd of given numbers is %d\n", gcd(a, b)); 
    return 0; 
} 