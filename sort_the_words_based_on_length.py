def sort(s):
    w=s.split()
    w.sort(key=lambda word:(len(word),word))
    return w
s=input()
sw=sort(s)
print(*sw)