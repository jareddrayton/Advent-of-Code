import math 
vectors = [(2,2), (2,-2), (-2,-2), (-2,2)]

for vec in vectors:
    print(math.degrees(math.atan2(*vec[::-1]))) # - math.pi))
