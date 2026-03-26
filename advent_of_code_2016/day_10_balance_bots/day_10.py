from collections import deque
from math import prod


class Bot:
    def __init__(self, id):
        self.id = id
        self.microchips: list[int] = []
        self.relationships: list[tuple] = []

    def add_relationship(self, relationship: tuple[str, str, str]):
        self.relationships.append(relationship)

    def add_microchip(self, microchip: int):
        self.microchips.append(microchip)

    def execute(self) -> list[str] | None:
        if len(self.microchips) == 2 and len(self.relationships) == 2:
            instructions: list = []
            for type, entity, id in self.relationships:
                if type == "low":
                    value = min(self.microchips)
                if type == "high":
                    value = max(self.microchips)
                instructions.append(f"value {value} goes to {entity} {id}")
            return instructions
        return None


class Bin:
    def __init__(self, id):
        self.id = id
        self.microchips: list = []

    def add_microchip(self, microchip: int):
        self.microchips.append(microchip)


def parse_value(instruction: str, factory: dict[str, Bot | Bin]):
    _, value, _, _, type, id = instruction.split()
    value, id = int(value), int(id)
    match type:
        case "bot":
            if f"bot_{id}" not in factory:
                factory[f"bot_{id}"] = Bot(id)
            factory[f"bot_{id}"].add_microchip(value)
            return factory[f"bot_{id}"].execute()
        case "output":
            if f"output_{id}" not in factory:
                factory[f"output_{id}"] = Bin(id)
            factory[f"output_{id}"].add_microchip(value)


def parse_gives(instruction: str, factory: dict[str, Bot | Bin]):
    _, bot, _, type_1, _, entity_1, id_1, _, type_2, _, entity_2, id_2 = (
        instruction.split()
    )
    if f"bot_{bot}" not in factory:
        factory[f"bot_{bot}"] = Bot(bot)
    for type, entity, id in [(type_1, entity_1, id_1), (type_2, entity_2, id_2)]:
        factory[f"bot_{bot}"].add_relationship((type, entity, id))
    return factory[f"bot_{bot}"].execute()


def execute_instructions(instructions: deque[str], factory: dict[str, Bot | Bin]):
    if not instructions:
        return factory

    instruction = instructions.popleft()

    if instruction.startswith("value"):
        new_instructions = parse_value(instruction, factory)
    if instruction.startswith("bot"):
        new_instructions = parse_gives(instruction, factory)

    if new_instructions:
        instructions.extendleft(new_instructions)

    return execute_instructions(instructions, factory)

def part_1(factory: dict[str, Bot | Bin]):
    for entity in factory.values():
        if {61, 17} == set(entity.microchips):
            return entity.id
def part_2(factory: dict[str, Bot | Bin]):
    chips = []
    for entity in factory.values():
        if isinstance(entity, Bin) and entity.id in [0, 1, 2]:
            chips.append(entity.microchips[0])
    return prod(chips)

if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        instructions = deque([instruction.strip() for instruction in fh.readlines()])

    factory: dict[str, Bot | Bin] = {}
    factory = execute_instructions(instructions, factory)
    print("Part 1:", part_1(factory))
    print("Part 2:", part_2(factory))
    