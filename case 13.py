h=int(input())
for i in range (2, int(h/2)):
    if h % i == 0:
        print("no")
        break
else:
    print("yes")
