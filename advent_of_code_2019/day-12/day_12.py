
with open("day-12-input-example.txt", 'r') as f:
    coords = f.readlines()


steps = 12
moon_names = ["Io", "Europa", "Ganymede", "Callisto"]
moons = {}


class Moon:
    
    def __init__(self, position, name):
        self.name = name
        self.position = position
        self.velocity = [0, 0, 0]
        self.temp_velocity = None
        
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


    def apply_gravity(self):
        
        self.temp_velocity = []
        for moon in moons.keys():
            if moon != self.name:
                self.temp_velocity.append(list(map(self.calculate_gravity, self.position, moons[moon].position)))
        
        
        #print(self.temp_velocity)
        self.temp_velocity = [[b[i] for b in self.temp_velocity] for i in range(len(self.temp_velocity))]
        self.temp_velocity = [sum(a) for a in self.temp_velocity]
        #print(self.temp_velocity, "hy")

    def apply_velocity(self):
        self.velocity = [0, 0, 0]
        
        self.velocity = [sum(i) for i in zip(self.velocity, self.temp_velocity)] 
        #print(self.velocity,"Vel")
        #print(self.position, "hg")
        self.position = [sum(i) for i in zip(self.position, self.velocity)] 
        #print(self.position, "323")


    def calculate_energy(self):
        self.kinetic_energy = sum(map(abs, self.velocity))
        self.potential_energy = sum(map(abs, self.position))
        self.total_energy = self.kinetic_energy * self.potential_energy


def parse_input(coords): 
    for coord, moon in zip(coords, moon_names):
        coord = coord.strip().split(',')
        moons[moon] = Moon([int("".join([b for b in a if b.isdigit() or b == "-"])) for a in coord], moon )

parse_input(coords)


for i in range(steps):
    print("Step {}".format(i))
    
    for moon in moons.keys():
        print(moons[moon].position)
        moons[moon].apply_gravity()
        moons[moon].apply_velocity()
        moons[moon].calculate_energy()
        print(moons[moon].position)

    print(sum(moons[moon].total_energy for moon in moons.keys()))
