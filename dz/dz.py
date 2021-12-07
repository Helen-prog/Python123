def elevator(n):
    if n == 0:
        print("Вы в подвале")
        return
    print("->", n)
    elevator(n - 1)
    print(n, end=" ")


n1 = int(input("На каком вы этаже: "))
elevator(n1)
