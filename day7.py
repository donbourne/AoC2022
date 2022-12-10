class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent_dir):
        self.name = name
        self.parent_dir = parent_dir
        self.child_dirs = set()
        self.files = set()
        self.size = 0

    def add_size(self, size):
        self.size += size
        if self.parent_dir is not None:
            self.parent_dir.add_size(size)

    def add_child_dir(self, dir):
        self.child_dirs.add(dir)

    def add_file(self, file):
        self.files.add(file)
        self.add_size(file.size)

    def get_children(self):
        children = list()
        children.extend(self.child_dirs)
        for child_dir in self.child_dirs:
            children.extend(child_dir.get_children())
        return children

    def __str__(self):
        return f'{self.name}:{str(self.size)}'

    def __repr__(self):
        return self.__str__()

class Shell:

    def __init__(self):
        self.root_dir = Directory("ROOT", None)
        self.current_dir = self.root_dir

    def cd(self, dir_name):
        child_dirs = self.current_dir.child_dirs
        for child_dir in child_dirs:
            if child_dir.name == dir_name:
                self.current_dir = child_dir
                return
        raise(f'invalid directory name for cd: {dir_name}')

    def parse(self, line):
        if line.startswith("$ cd /"):
            pass
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            self.current_dir.add_child_dir(Directory(line.split(" ")[1], self.current_dir))
        elif line[0].isdigit():
            size, name = line.split(" ")
            self.current_dir.add_file(File(name, int(size)))
        elif line.startswith("$ cd .."):
            self.current_dir = self.current_dir.parent_dir
        elif line.startswith("$ cd "):
            self.cd(line.split(" ")[2])

    def get_all_dirs(self):
        dirs = list()
        dirs.append(self.root_dir)
        dirs.extend(self.root_dir.get_children())
        return dirs


shell = Shell()
with open("day7.txt", "rt") as f:
    for line in f:
        shell.parse(line.strip())
dirs = shell.get_all_dirs()

# problem 1
size_sum = 0
for dir in dirs:
    if dir.size <= 100000:
        size_sum += dir.size
print(size_sum)

# problem 2
free_space   = 70000000 - shell.root_dir.size
needed_space = 30000000 - free_space
min_size = 99999999
for dir in dirs:
    if dir.size > needed_space:
        if dir.size < min_size:
            min_size = dir.size
print(min_size)

