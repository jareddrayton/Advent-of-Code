with open("input.txt", 'r') as f:
    directions = f.readlines()

#print(directions)

x,y = 0,0

dx = {"U": 0, "L": -1, "D": 0, "R": 1}
dy = {"U": 1, "L": 0, "D": -1, "R": 0}

code = [[0,0]]

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

for direction in directions:
    direction = direction.strip()
    i = 0
    #print(code[-1:])
    x , y = code[i]

    for a in direction:
        #print(a)
        
        x +=  dx[a] 
        
        if x > 1:
            x = 1
        elif x < -1:
            x = -1
        
        y +=  dy[a]
        
        if y > 1:
            y = 1
        elif y < -1:
            y = -1
        
    code.append([x,y])
    i +=1 


solution = ''

for digit in code[1:]:

    solution += digit_map[  str(digit[0]) + ',' + str(digit[1])   ]

print("Part One:", solution)

# P2 3m44s4