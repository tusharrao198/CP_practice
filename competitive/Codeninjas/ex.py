"""
Choosing the right candidate
Send Feedback
The king is looking for chief advisor. The judges panel, consists of judges from region's supreme court. There are M candidates, labelled from 1 to M. Each of the judge will select exactly one candidate. The judge will publish its own rank-list of candidates, that is a permutation of labels 1 to M. The candidate with most number of selections is the winner. If two or more candidates are selected by most number of judges, then the candidate with smallest label is preferred.
For example, let's say there are four candidates and one of the judges rank-list is: 2, 1, 4, 3. This means the judge has selected candidate with label 2. If the candidate with label 2 gives up the candidacy, then candidate with label 1 will be selected by this particular judge.
You are given rank-list of each judge and your task is to find the winner candidate's label. You have another task. You are given a label K. You have to find minimum number of candidates, who have to give up candidacy, so that candidate with label K wins.
Input Format:
The first line of input contains integers N (1 <= N <= 100), M (1 <= M <= 15) and K (1 <= K <= M). Each of the following N lines contain rank-list of each judge, which is a permutation of first M natural numbers.
Constraints:
Time Limit: 3 seconds
Output Format:
Print the winner candidate's label in first line. In the next line, print the minimum number of candidates, who have to give up candidacy, so that candidate with label K wins.
Sample Input 1:
3 4 1
3 4 1 2
4 2 3 1
3 4 2 1
Sample Output 1:
3
3
Explanation:
If neither of the candidates give up their candidacy, then label 3 candidate will win. To make label 4 candidate win, all the other candidates have to give up their candidacy. 
"""

N, M, K = list(map(int, input().split()))


lst_x =[]
for i in range(N):
    dict={}
    lst = list(map(int, input().split()))
    lst_x.append(lst)
print(lst_x)
lst11=[]
for j in lst_x:
    dict={}
    for k in range(len(lst_x)):
        dict[j[k]] = dict.get(j[k],0)+1
    lst11.append(dict)
print(lst11)