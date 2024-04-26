def multiplication(start, end) :
    for i in range(1, 10):
        for j in range(start, end + 1):
            if j <= 5:
                print(f"{j} x {i} = {i * j:2d}", end="      ")
            else:
                print(f"{j} x {i} = {i * j:2d}", end="      ")
        print()

multiplication(2, 5)
print()
multiplication(6, 9)
