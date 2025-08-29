def rem(l, word):
    n = []
    for item in l:
        if (item != word):
            n.append(item.replace(word, ""))
    return n

l = ["harry", "rohan", "Manas", "subham", "an"]
print(rem(l, "an"))

def rem(l, word):
    return [item.replace(word, "") for item in l if item != word]

l = ["harry", "rohan", "Manas", "subham", "an"]
print(rem(l, "an"))
