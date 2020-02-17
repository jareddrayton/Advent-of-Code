with open("input.txt", 'r') as f:
    directions = f.readlines()

#print(directions)

x,y = 0,0

dx = {"U": 0, "L": -1, "D": 0, "R": 1}
dy = {"U": 1, "L": 0, "D": -1, "R": 0}




code = [[2,0]]

digit_map = {"-1,1": '1', 
             "0,1": '2', 
             "1,1": '3',
             "-1,0": '4',
             "0,0": '5',
             "1,0": '6',    
             "-1,-1": '7',
             "0,-1": '8',
             "1,-1": '9',             
             }


keypad = [
     [0,   0,   1,   0,   0],
     [0,   2,   3,   4,   0],
     [5,   6,   7,   4,   0],
     [0, 'A', 'B', 'C',   0],
     [0,   0, 'D',   0,   0],
    ]

print(keypad[2][0])

for direction in directions:
    direction = direction.strip()
    
    i = 0

    x , y = code[i]

    for a in direction:

        if keypad[x + dx[a]][y] == 0:
            pass        

        x +=  dx[a] 

        
    code.append([x,y])
    i +=1 


solution = ''

for digit in code[1:]:

    solution += digit_map[  str(digit[0]) + ',' + str(digit[1])   ]

print("Part One:", solution)

# P2 3m44s4
# P2 12m17s9