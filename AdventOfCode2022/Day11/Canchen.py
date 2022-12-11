NUM_MONKEYS = 8
part_one = False

monkeys = []
mod = 1

class Monkey():

    def __init__(self, items, mult, add, power, test, true, false):
        self.items = items
        self.mult = mult
        self.add = add
        self.power = power
        self.test = test
        self.true = true
        self.false = false
        self.items_thrown = 0
    
    def throw_items(self):
        for i in range(len(self.items)):
            k = self.items.pop(0)
            k *= self.mult
            k += self.add
            k = pow(k, self.power)
            if part_one:
                k = k // 3
            else:
                k %= mod

            if k % self.test == 0:
                monkeys[self.true].items.append(k)
            else:
                monkeys[self.false].items.append(k)

            self.items_thrown += 1

for k in range(NUM_MONKEYS):

    cur_line = input()

    cur_line = input() #starting items
    cur_line = cur_line.lstrip()
    cur_line = cur_line[len("Starting items: "):]
    items = cur_line.split(',')
    items = [int(i) for i in items]

    cur_line = input() #operation
    cur_line = cur_line.lstrip()
    x = cur_line.split(' ')
    add = 0
    mult = 1
    power = 1
    if x[4] == '*':
        if str.isdigit(x[5]):
            mult = int(x[5])
        else:
            power = 2 #jank but hopefully it works
    else:
        add = int(x[5])

    cur_line = input() #test
    cur_line = cur_line.lstrip()
    x = cur_line.split(' ')
    test = int(x[3])

    cur_line = input() #true
    cur_line = cur_line.lstrip()
    x = cur_line.split(' ')
    true = int(x[5])

    cur_line = input() #false
    cur_line = cur_line.lstrip()
    x = cur_line.split(' ')
    false = int(x[5])

    cur_line = input() #get empty line

    monkeys.append(Monkey(items, mult, add, power, test, true, false))

for m in monkeys:
    mod *= m.test

t = 10000
if part_one:
    t = 20

for i in range(10000):
    for k in range(len(monkeys)):
        monkeys[k].throw_items()

thrown = []
for m in monkeys:
    thrown.append(m.items_thrown)
thrown.sort()
print(thrown[-1] * thrown[-2])
