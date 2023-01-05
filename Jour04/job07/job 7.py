def nombres():
    dups=set()
    L=[8,24,48,2,16]
    for i in L:
        if L.count(i%3):
            dups.add(i%3)
    print(dups)
nombres()