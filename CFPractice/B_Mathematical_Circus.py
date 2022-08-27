import sys
inp = sys.stdin.readline

def count4Divisibiles( arr , n ):
     
    # Create a frequency array to count
    # occurrences of all remainders when
    # divided by 4
    freq = [0, 0, 0, 0]
     
    # Count occurrences of all remainders
    for i in range(n):
        freq[arr[i] % 4]+=1
         
    #If both pairs are divisible by '4'
    ans = freq[0] * (freq[0] - 1) / 2
     
    # If both pairs are 2 modulo 4
    ans += freq[2] * (freq[2] - 1) / 2
     
    # If one of them is equal
    # to 1 modulo 4 and the
    # other is equal to 3
    # modulo 4
    ans += freq[1] * freq[3]
     
    return int(ans)


for _ in range(int(inp())):
    n= int(inp())
    n, a, b = map(int, inp().split())
    arr=list(map(int, inp().split()))
    
    ans = []
    for i in range(n):
        print(ans[i], end= " ")
    print()