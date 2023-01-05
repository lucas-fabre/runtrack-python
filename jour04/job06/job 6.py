def nombres():
    L=[5,10,14,69,72]
    ech= L[0]
    L[0]=L[4]
    L[4]=ech
    print(L)
nombres()