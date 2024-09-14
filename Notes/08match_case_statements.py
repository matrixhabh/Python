x = int(input("Enter the value of x: "))

match x:
    # if x is 0
    case 0:
        print("x is zero")

    # if x is 4
    case 4 :
        print("x is four")

    case _ if x!=90:
        print(x, "is not ninety")

    case _ if x!=80:
        print(x, "is not eighty")

    case _:
        print(x)