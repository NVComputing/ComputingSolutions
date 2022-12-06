th = input()
def check(x):
    for i in range(len(x)-4):
        if len(set(x[i:i+4])) == 4:
            return i+4
print(check(th))
