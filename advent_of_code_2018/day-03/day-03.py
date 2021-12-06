import numpy as np

with open("day-03-input.txt", 'r') as f:
    claims = f.readlines()

fabric = np.zeros((1000,1000), dtype=int)

def apply_claim(left_edge, top_edge, width, height):
    fabric[top_edge:top_edge + height, left_edge:left_edge + width] += 1

def check_claim(left_edge, top_edge, width, height):
    return np.all(fabric[top_edge:top_edge + height, left_edge:left_edge + width] == 1)

new_claims = []

for claim in claims:
    claim = claim.strip()
    
    ID, claim = claim.split("@ ")
    
    ID = [ID.strip("#")]
    position, size = claim.split(": ")
    position = position.split(",")
    size = size.split("x")
    
    claim = list(map(int, position + size + ID))
    
    new_claims.append(claim)
    apply_claim(*claim[:4])

print("Part One:", np.sum(fabric >= 2))

for claim in new_claims:
    if check_claim(*claim[:4]):
        print("Part Two:", claim[4])
        break