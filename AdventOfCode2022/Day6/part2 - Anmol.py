th = input()

def check(x):
    for i in range(len(x)-14):
        if len(set(x[i:i+14])) == 14:
            return i+14
print(check(th))
