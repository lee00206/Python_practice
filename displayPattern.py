def displayPattern(n):
    for i in range(1, n+1):
        print("   "*(n-i), end = ' ')
        for j in range(i, 0, -1):
            print(format(j, "^2d"), end = ' ')
        print()
