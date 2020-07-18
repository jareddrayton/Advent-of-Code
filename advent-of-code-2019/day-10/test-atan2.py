import math 
vectors = [(0,4), (1,3), (2,2), (3,1), (4,0),
            (3,-1), (2,-2), (1,-3), (0,-4),
            (-1,-3), (-2,-2), (-3,-1), (-4,0),            
            (-3,1),(-2,2),(-1,3),(-0.1, 10)]

for vec in vectors:
    if math.degrees(math.atan2(*vec)) < 0:
        print(math.degrees(math.atan2(*vec))+360)
    else:
        print(math.degrees(math.atan2(*vec)) )# - math.pi))