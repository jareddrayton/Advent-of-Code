import itertools

with open("day-12-input-example.txt", 'r') as f:
    coords = f.readlines()


steps = 9
moon_names = ["Io", "Europa", "Ganymede", "Callisto"]
moons = {}


class Moon:
    
    def __init__(self, position, name):
        self.name = name
        self.position = position
        self.velocity = [0, 0, 0]
        self.kinetic_energy = 0
        self.potential_energy = 0
        self.total_energy = 0


    def calculate_gravity(self, x_1, x_2):
        if x_1 < x_2:
            return 1
        elif x_1 == x_2:
            return 0
        elif x_1 > x_2:
            return -1


    def apply_gravity(self, moons):
        for moon in moons.keys():
            if moon != self.name:
                self.temp_velocity = list(map(self.calculate_gravity, self.position, moons[moon].position))
                self.apply_velocity(self.temp_velocity)


    def apply_velocity(self, x_velocity):
        self.velocity = [sum(i) for i in zip(self.velocity, x_velocity)] 


    def calculate_potential_energy(self):
        self.potential_energy = sum(map(abs, self.position))
        print(self.potential_energy)


    def calculate_kinetic_energy(self):
        self.kinetic_energy = sum(map(abs, self.velocity))
        print(self.kinetic_energy)


    def calculate_total_energy(self):
        self.calculate_potential_energy()
        self.calculate_kinetic_energy()
        self.total_energy = self.kinetic_energy * self.potential_energy


def parse_input(coords):
    for coord, moon in zip(coords, moon_names):
        coord = coord.strip().split(',')
        moons[moon] = Moon([int("".join([b for b in a if b.isdigit() == True or b == "-"])) for a in coord], moon )

parse_input(coords)



for i in range(steps):
    for moon in moons.keys():
        moons[moon].apply_gravity(moons)
        moons[moon].calculate_total_energy()

print(sum(moons[moon].total_energy for moon in moons.keys()))

for moon in moons.keys():
    print(moons[moon].position, moons[moon].name)