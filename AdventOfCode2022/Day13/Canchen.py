import functools
import copy

#type 'end\nend\n' as your last input

input_a = input()
input_b = input()

def compare(a, b):

    for i in range(min(len(a), len(b))):

        one = isinstance(a[i], int)
        two = isinstance(b[i], int)

        if isinstance(a[i], int) and isinstance(b[i], int):
            if a[i] < b[i]:
                return 1
            elif a[i] > b[i]:
                return -1
        elif isinstance(a[i], list) and isinstance(b[i], list):
            if a[i] != b[i]:
                return compare(a[i], b[i])
        elif one != two:
            if isinstance(a[i], int):
                new_a = copy.deepcopy(a[i])
                new_a = [new_a]
                if new_a != b[i]:
                    return compare(new_a, b[i])
            else:
                new_b = copy.deepcopy(b[i])
                new_b = [new_b]
                if a[i] != new_b:
                    return compare(a[i], new_b)
            

    if len(a) < len(b):
        return 1
    else:
        return -1

k = 1
ans = 0
packets = [[[2]], [[6]]]

while input_a != 'end':

    a = []
    b = []
    exec("a = " + input_a)
    exec("b = " + input_b)
    packets.append(a)
    packets.append(b)

    if compare(a, b) == 1:
        ans += k

    k += 1

    input_a = input()
    input_a = input()
    input_b = input()

uwu = sorted(packets, key=functools.cmp_to_key(compare), reverse=True)
#uwu = [str(k) for k in uwu]
a = uwu.index([[2]]) + 1
b = uwu.index([[6]]) + 1

print(ans)
print(a * b)
