// You have a positive integer m and a non - negative integer s.Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s.The required numbers should be non - negative integers written in the decimal base without leading zeroes.

// Input

// The single line of the input contains a pair of integers m,
// s(1 ≤ m ≤ 100, 0 ≤ s ≤ 900) — the length and the sum of the digits of the required numbers.Output

// In the output print the pair of the required non
// - negative integer numbers — first the minimum possible number,
// then — the maximum possible number.If no numbers satisfying conditions required exist, print the pair of numbers “- 1 - 1” (without the quotes).

// Examples

// Input 1 2 15 Output 1 69 96

// Input 2 3 0 Output 2 -
// 1 - 1

#include<bits/stdc++.h>
                                                                                               using namespace std;

void number (int m, int s)
{
  int sum = s;
  string mini = "", maxi = "";

  if ((m != -1 and s == 0) or s > 9 * m)
    {
      cout << "-1 -1";
      return;
    }

  for (int i = 0; i < m; i++)
    {
      int x = min (9, s);
      maxi += to_string (x);

      s = s - x;
      // cout << maxi << s << endl;
    }
    // cout << mini << " - " << sum << endl;
    for (int i = 0; i < m - 1; i++)
    {
      int x = min (9, sum);
      mini += to_string (x);

      sum -= x;
      
    }
    // cout << mini << " " << sum << endl;
    mini = to_string(sum) + mini;
    // cout << "--------------"<< endl;
    cout << mini << " " << sum << endl;

    cout << mini << " " << maxi;

    return;

}

int main ()
{

  int m, s;
  cin >> m >> s;

  number (m, s);

  return 0;
}