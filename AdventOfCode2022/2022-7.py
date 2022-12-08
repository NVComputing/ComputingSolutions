cur_line = input()

class Directory():

    def __init__(self) -> None:
        self.size = 0
        self.name = ''
        self.contains = []
        self.parent = None

    def total_size(self) -> int:
        x = self.size
        for d in self.contains:
            x += d.total_size()
        return x

    def part1(self) -> int:
        ans = 0
        if self.total_size() < 100000:
            ans += self.total_size()
        for d in self.contains:
            ans += d.part1()
        return ans

directories = Directory()

cur_dir = directories
listing = False

while cur_line != '':

    x = cur_line.split(' ')

    if x[0] == '$':
        listing = False
        if x[1] == 'cd':
            if x[2] == '..':
                cur_dir = cur_dir.parent
            elif x[2] == '/':
                cur_dir = directories
            else:
                for d in cur_dir.contains:
                    if d.name == x[2]:
                        cur_dir = d
                        break

    if listing:
        if x[0] == 'dir':
            new_dir = Directory()
            new_dir.parent = cur_dir
            new_dir.name = x[1]
            cur_dir.contains.append(new_dir)
        else:
            cur_dir.size += int(x[0])
    
    if x[0] == '$' and x[1] == 'ls':
        listing = True

    cur_line = input()

print(directories.part1())

available_space = 70000000 - directories.total_size()
to_delete = 30000000 - available_space

smol = 70000000

def part2(directory):
    global smol
    if directory.total_size() > to_delete:
        smol = min(smol, directory.total_size())
    for d in directory.contains:
        part2(d)
part2(directories)

print(smol)