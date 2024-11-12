alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def score(name):
    acc = 0
    for letter in list(name):
        acc += (alphabet.index(letter)+1)
    return acc

def main():
    with open('0022_names.txt') as file:
        content = file.read()
    names = content.replace('"', '').split(',')
    names.sort()

    acc = 0
    for i, name in enumerate(names):
        acc += ((i+1)*score(name.lower()))
    return acc