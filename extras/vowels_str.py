import math
vow = ['a','e', 'i', 'o', 'u']

def prime_(s , e):
    lst =[]
    for i in range(s,e+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                lst.append(i)
    return sum(lst)


def single( n):
	sum = 0
	while(n > 0 or sum > 9):
		if(n == 0):
			n = sum
			sum = 0
		sum += n % 10
		n /= 10
	return math.floor(sum)

s = input()
d = {}
index_of_vow = {}
for i in range(len(s)):
    if s[i] in vow:
        num = prime_(1, i*100)
        d[s[i]] = single(num)
        index_of_vow[s[i]] = i

new_str = list(s)
for k  in list(d.keys()):
    new_str[index_of_vow[k]] = str(d[k])

print(''.join(new_str))