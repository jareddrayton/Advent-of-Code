import itertools

with open("2.txt", 'r') as f:
    program_new = f.readline().split(",")

program = [int(module.strip()) for module in program_new]

# Replace the values specified
program[1], program[2] = 12, 2

#######################################################################
# opcode 1 - add
# adds together numbers read from two positions, and stores the result in a third position
# the three integers immediately after the opcode tell you these three positions 
# the first two indicate the positions from which you should read the input files 
# the third indicates the position at which the output should be stored
def add(a, b, m):
    program[m] = program[a] + program[b]

# opcode 2 - multiply
# same functionality as 1 but multiplies instead of adds
def multiply(a, b, m):
    program[m] = program[a] * program[b]

# opcode 3
# takes a single integer as input and saves it to the position given by its only parameter. 
# For example, the instruction 3,50 would take an input value and store it at address 50.
def 


# opcode 4

# opcode 99 - halt
######################################################################

# Use a dictionary as a switch for the opcode functions
opcode_dict = {
                1: add,
                2: multiply,
            }

def run():
    instruction_pointer = 0
    while program[instruction_pointer] != 99:
        opcode_dict[program[instruction_pointer]](program[instruction_pointer+1], 
                                                            program[instruction_pointer+2], 
                                                            program[instruction_pointer+3])
        # Move along pointer after executing opcode
        instruction_pointer += 4

run()

print("Part One:", program[0])

for perm in itertools.permutations([x for x in range(0, 101)], 2):
    program = [int(module.strip()) for module in program_new]
    program[1], program[2] = perm
    run()
    if program[0] == 19690720:
        print("Part Two:", perm)
        break