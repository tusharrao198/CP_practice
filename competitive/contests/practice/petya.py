a = input().lower()
b = input().lower()

lst = sorted([a,b])
if a==b:
    print("0")
else:
    if lst[0]==a:
        print("-1")
    if lst[0]==b:
        print('1')

# approach list sorting is done lexicographically

# https://stackoverflow.com/questions/47478926/definition-of-a-lexicographical-order?noredirect=1&lq=1

