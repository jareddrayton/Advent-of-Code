b = "RULLDDRRRUUU"

a = ["R" * i + "U" * i if i % 2 == 1 else "L" * i + "D" * i for i in range(600)] 

print(len(a))

a = "".join(a)

#print(a)
print(len(a))
#325489

dx = {"U": 0, "L": -1, "D":  0, "R": 1}
dy = {"U": 1, "L":  0, "D": -1, "R": 0}

x,y = 0,0

store = {}

for i in range(1,325489+1):
    
    x += dx[a[i]]
    y += dy[a[i]]
    store[i] = (x,y)
    
x1,x2 = store[325489]

print(store[12])

print(abs(0-x1)+abs(0-x2)) 




