with open("3.txt", "r") as f:
    a,b = f.readlines()

a = a.split(",")
b = b.split(",")

DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

def walk_fun(steps):
    
    x_coord, y_coord = 0, 0
    length = 0
    ans = {}

    for step in steps:
        step = step.strip()
        direction = step[0]
        distance = int(step[1:])
        for _ in range(distance):
            x_coord += DX[direction]
            y_coord += DY[direction]
            length +=1
            
            if (x_coord, y_coord) not in ans:
                ans[x_coord, y_coord] = length

    return ans

A = walk_fun(a)
B = walk_fun(b)

both = set(A.keys())&set(B.keys())
ans = min([A[p]+B[p] for p in both])
print(ans)