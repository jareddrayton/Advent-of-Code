class Wire:
    def __init__(self, name, circuit, operation=None, children=None, parents=None):
        self.name = name
        self.circuit = circuit
        self.operation = operation
        self.parents = []
        if parents:
            self.parents += parents
        self.children = [children]

        self.value = None

        if operation:
            self.check_valid_operation()

    def execute_operation(self, operation):
        match operation:
            case x, "AND", y:
                self.value = x & y
            case x, "OR", y:
                self.value = x | y
            case x, "LSHIFT", y:
                self.value = x << y
            case x, "RSHIFT", y:
                self.value = x >> y
            case "NOT", x:
                self.value = 65535 - x
            case x:
                self.value = x[0]

        self.try_upstream()

    def check_valid_operation(self):
        if not self.operation:
            return None

        wires = []

        for x in self.operation:
            if x.islower():
                wires.append(self.circuit[x].value)
            elif x.isdigit():
                wires.append(int(x))
            else:
                wires.append(x)

        match wires:
            case [int(), str(), int()]:
                self.execute_operation(wires)
            case [str(), int()]:
                self.execute_operation(wires)
            case [int()]:
                self.execute_operation(wires)

        return wires

    def try_upstream(self):
        for child in self.children:
            if child in self.circuit.keys() and not self.circuit[child].value:
                self.circuit[child].check_valid_operation()

    def reset_value(self):
        self.value = None


def build_circuit():
    circuit = {}
    with open("input.txt", "r") as fh:
        instructions = fh.readlines()

    for instruction in instructions:
        instruction = instruction.strip().split()
        identifier = instruction[-1]
        operation = instruction[:-2]

        parents = [x for x in operation if x.islower()]

        for parent in parents:
            if parent not in circuit.keys():
                circuit[parent] = Wire(parent, circuit, children=identifier)
                circuit[parent].check_valid_operation()
            else:
                circuit[parent].children += [identifier]
                circuit[parent].check_valid_operation()

        if identifier not in circuit.keys():
            circuit[identifier] = Wire(
                identifier, circuit, operation=operation, parents=parents
            )
        else:
            circuit[identifier].operation = operation
            circuit[identifier].parents += parents
            circuit[identifier].check_valid_operation()

    return circuit


def part_1(circuit):
    return circuit["a"].value


def part_2(circuit):
    for wire in circuit.values():
        wire.reset_value()

    circuit["b"].operation = ["46065"]
    for wires in circuit.values():
        wires.check_valid_operation()
    return circuit["a"].value


if __name__ == "__main__":
    circuit = build_circuit()
    print("Part 1:", part_1(circuit))
    print("Part 2:", part_2(circuit))
