lst=["sda","sdd"]
a=""
s=a.join(lst)
print(s)

dict={}
for i in list(s):
    dict[i]=dict.get(i,0)+1
lst1= list(dict.values())
print(sum(lst1))
print(dict)