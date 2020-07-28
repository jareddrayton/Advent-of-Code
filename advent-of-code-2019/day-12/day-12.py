import itertools

with open("day-12-input.txt", 'r') as f:
    coords = f.readlines()


steps = 5
moon_names = ["Io", "Europa", "Ganymede", "Callisto"]
moons = {}


class Moon:
    
    def __init__(self, position, name):
        self.name = name
        self.position = position
        self.x_velocity = 0
        self.y_velocity = 0
        self.z_velocity = 0
    
    def apply_gravity(self, moons):

        for moon in moons.keys():
            if moon != self.name:
                print(moons[moon].position)
                if self.position[0] < moons[moon].position[0]:



    def apply_velocity():
        pass
    

    # calculate the velocity by applying gravity.
    # only apply velocity to position once all velocity has been checked.


def parse_input(coords):
    print(coords)
    for coord, moon in zip(coords, moon_names):
        coord = coord.strip().split(',')
        moons[moon] = Moon([int("".join([b for b in a if b.isdigit() == True or b == "-"])) for a in coord], moon )

parse_input(coords)


print(moons)

print(moons["Io"].position)
print(moons["Io"].name)

print(list(itertools.combinations(moons.keys(), 2)))

for i in range(steps):
    for moon in moons.keys():
        moons[moon].apply_gravity(moons)