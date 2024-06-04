class City:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def update_connections(self, connection):
        self.connections.append(connection)


def parse_input():
    with open("input.txt", "r") as fh:
        lines = [line for line in fh.readlines()]
    graph = {}
    for line in lines:
        line = line.split()
        start, end, distance = line[::2]
        print(start, end, distance)
        if start not in graph.keys():
            graph[start] = City(start)
        graph[start].update_connections((end, int(distance)))
        if end not in graph.keys():
            graph[end] = City(end)
        graph[end].update_connections((start, int(distance)))
    return graph


new = parse_input()


def find_route(city, visited, reverse):
    if not visited:
        visited = set()
        visited.add(city)

    nearest = sorted(new[city].connections, key=lambda x: x[1], reverse=reverse)
    nearest = [x for x in nearest if x[0] not in visited]
    if not nearest:
        return []
    visited.add(nearest[0][0])
    return [nearest[0]] + find_route(nearest[0][0], visited, reverse)


dist = []
for key in new.keys():
    dist.append(sum([x[1] for x in find_route(key, None, False)]))
    # print(find_shortest(key, None))
print(min(dist))

dist_2 = []
for key in new.keys():
    dist_2.append(sum([x[1] for x in find_route(key, None, True)]))
    # print(find_shortest(key, None))

print(max(dist_2))
