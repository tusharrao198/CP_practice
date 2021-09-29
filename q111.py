debts = [
    ["Aman", "Bhim", "2"],
    ["Bhim", "Aman", "2"],
    ["Chintu", "Aman", "5"],
    ["Bhim", "Chintu", "7"],
    ["Aman", "Bhim", "4"],
    ["Aman", "Chintu", "4"],
]

lst = []
m = {}

for i in range(len(debts)):
    m[debts[i][0]] = m.get(debts[i][0], 0) - int(debts[i][2])
    m[debts[i][1]] = m.get(debts[i][1], 0) + int(debts[i][2])

for k, v in m.items():
    lst.append([v, k])
lst.sort(key=lambda x: -x[0])

print(m)
print(lst)
