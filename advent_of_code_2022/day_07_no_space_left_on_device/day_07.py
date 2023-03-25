import secrets


class Directory:
    def __init__(self, parent, name):
        self.name = name
        self.parent_directory_id = parent
        self.files = {}
        self.directories = {}
        self.size = None
        self.total_size = None

    def directory_size(self):
        if self.files:
            self.size = sum([x for x in self.files.values()])
        else:
            self.size = 0

    def __str__(self):
        fl = "\n".join([" {}".format(x) for x in self.files.keys()])
        dl = "\n".join(["  {}".format(x) for x in self.directories.keys()])
        template = f"{self.name}\n{dl}\n{fl} "

        return template


class FileSystem:
    def __init__(self, commands=None):

        self.file_system = {}
        self.root_id = None
        self.current_directory_id = None
        self.total_disk_space = 70000000
        self.initialise_file_system()

        if commands:
            self.parse_output(commands)

        self.calculate_size(self.root_id)
        self.calculate_total_size()

    @property
    def current_directory(self):
        return self.file_system[self.current_directory_id]

    def initialise_file_system(self):
        self.root_id = self.create_directory("/")
        self.current_directory_id = self.root_id

    def parse_output(self, commands):
        ls_commands = []
        for command in commands:
            command = command.strip()
            print(command)
            if command.startswith("$") and ls_commands:
                self._ls(ls_commands)
                ls_commands = []

            if command.startswith("$ cd"):
                self._cd(command.split()[-1])
            elif command.startswith("$ ls"):
                continue
            else:
                ls_commands.append(command)
        self._ls(ls_commands)

    def _cd(self, argument):
        print("argument", argument)
        print("current", self.current_directory.name)
        if argument == "..":
            self.move_up()
        elif argument == "/":
            self.current_directory_id = self.root_id
        else:
            self.move_down(argument)
        print("new", self.current_directory.name)
        print()

    def _ls(self, listing: list[str]):
        "Take the output of an ls command and update the file system"

        files = []
        directories = []
        for line in listing:
            line = line.strip()
            if line.startswith("dir"):
                directories.append(line.split()[1])
            else:
                files.append(line)

        for directory in directories:
            if directory not in self.current_directory.directories.keys():
                self.current_directory.directories[directory] = self.create_directory(directory)
        for file in files:
            file_size, file_name = file.split()
            if file_name not in self.current_directory.files.keys():
                self.current_directory.files[file_name] = int(file_size)

    def create_directory(self, name):
        id = self.generate_unique_id()
        self.file_system[id] = Directory(self.current_directory_id, name)
        return id

    def generate_unique_id(self):
        is_unique = False
        while is_unique is False:
            id = secrets.token_hex(5)
            if id not in self.file_system.keys():
                is_unique = True
        return id

    def move_up(self):
        self.current_directory_id = self.current_directory.parent_directory_id

    def move_down(self, directory):
        if directory in self.current_directory.directories.keys():
            self.current_directory_id = self.current_directory.directories[directory]

    def calculate_size(self, id):
        "run the directory_size method on all directories"
        for directory in self.list_child_directories(id):
            self.file_system[directory].directory_size()

    def list_child_directories(self, id):
        "return all the child directories"
        ids = []

        if self.file_system[id].directories:
            for directory in self.file_system[id].directories.values():
                ids += self.list_child_directories(directory)
        return ids + [id]

    def calculate_total_size(self):
        "calculate the total size for every directory."
        for directory in self.file_system.keys():
            total = 0
            directories = self.list_child_directories(directory)
            for child_directory in directories:
                total += self.file_system[child_directory].size
            self.file_system[directory].total_size = total

    def find_directory_max_size(self, limit):
        "Look for direcories that have a total_size under a certain limit"
        total = 0
        for directory in self.file_system.keys():
            if self.file_system[directory].total_size <= limit:
                total += self.file_system[directory].total_size
        return total

    def find_directory_to_delete(self, threshold):

        total_used = self.file_system[self.root_id].total_size
        free_space = self.total_disk_space - total_used

        new_size = total_used
        for directory in self.file_system.keys():
            candidate = self.file_system[directory].total_size
            if free_space + candidate >= threshold and candidate < new_size:
                new_size = candidate
        return new_size

    def directory_listing(self, id=None, level=0):
        "Print a recursive directory listing"
        if not id:
            id = self.root_id

        if self.file_system[id].directories:
            for directory, new_id in self.file_system[id].directories.items():
                print(level * " ", directory, level)
                self.directory_listing(new_id, level + 1)
        if self.file_system[id].files:
            for file, size in self.file_system[id].files.items():
                print(level * "  ", file, size, level)

    def __str__(self):
        lines = []
        for key, dir_ob in self.file_system.items():
            line = f"k={key}, pk={dir_ob.parent_directory_id}, dir={dir_ob.name}, child_dirs={dir_ob.directories.keys()} files={dir_ob.files.keys()}, size={dir_ob.size}, total_size={dir_ob.total_size}"
            lines.append(line)
        return "\n".join(lines)


with open("input.txt", "r") as fh:
    commands = [command.strip() for command in fh.readlines()]


def total_size_of_files():
    total_size = 0
    for command in commands:
        size = command.strip().split()[0]
        if size.isdigit():
            total_size += int(size)
    return total_size


fs = FileSystem(commands)

print()
print("Print total file size", total_size_of_files())
print(fs.file_system[fs.root_id].total_size, total_size_of_files())
print(fs.file_system[fs.root_id].total_size - total_size_of_files())

print()
print("Part A:", fs.find_directory_max_size(100000))
print("Part B:", fs.find_directory_to_delete(30000000))
