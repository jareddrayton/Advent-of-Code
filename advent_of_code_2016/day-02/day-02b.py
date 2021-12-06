with open("input.txt", 'r') as f:
    directions = f.readlines()

dx = {"U": 0, "L": -1, "D":  0, "R": 1}
dy = {"U": 1, "L":  0, "D": -1, "R": 0}

code = [[3,1]]

keypad = [
     [0,  0,   0,   0,   0,   0,  0],
     [0,  0,   0,   1,   0,   0,  0],
     [0,  0,   2,   3,   4,   0,  0],
     [0,  5,   6,   7,   8,   9,  0],
     [0,  0,  'A', 'B', 'C',  0,  0],
     [0,  0,   0,  'D',  0,   0,  0],
     [0,  0,   0,   0,   0,   0,  0],
    ]

def translate(y,x,a=3,b=1):
    return x-b, (y-a)*-1

def translate_back(y,x,a=3,b=1):
    return (x*-1)+2, y+b


assert translate(2,0,2,0) == (0, 0)
assert translate_back(0,0,2,0) == (2, 0)
assert translate(3,0,2,0) == (0,-1)
assert translate_back(0,-1,2,0) == (3,0)
assert translate(3,3,2,0) == (3,-1)

assert translate(3,1) == (0,0)
assert translate(2,2) == (1,1)

i = 0

for direction in directions:
    direction = direction.strip()
    
    x,y = code[i]

    x,y = translate(x,y)

    for step in direction:
        a,b = translate_back(x + dx[step], y + dy[step])

        if keypad[a][b] == 0:
            pass
        else:
            x += dx[step]           
            y += dy[step]

    x,y = translate_back(x,y)
    code.append([x,y])
    x,y = translate(x,y)
    
    i += 1 

for press in code:
    i,j = press
    print(keypad[i][j])