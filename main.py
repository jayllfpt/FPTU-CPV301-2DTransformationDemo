import functions as f


def checkRec():
    return (f.Ax, f.Ay, f.Bx, f.By) != (-1, -1, -1, -1)


def createMenu():
    print("Pick an option: ")
    print("1. Draw a rectangle")
    if checkRec():
        print("Rectangle: (", f.Ax, ",", f.Ay, ") and (", f.Bx, ",", f.By, ").")
        print("2. Translation transformation")
        print("3. Rotation transformation")
        print("4. Scaling transformation")
    print("0. Exit")
    option = -1
    while option < 0 or option > 4:
        if checkRec():
            option = int(input("Your option(0 - 4): "))
        else:
            option = int(input("Your option(0 - 1): "))
            if option > 1:
                option = -1
    return option


while True:
    option = createMenu()
    Ax, Ay, Bx, By = -1, -1, -1, -1
    if option == 1:
        f.Ax, f.Ay, f.Bx, f.By = f.function2()
    if option == 2:
        _ = f.function3(f.Ax, f.Ay, f.Bx, f.By)
    if option == 3:
        _ = f.function4(f.Ax, f.Ay, f.Bx, f.By)
    if option == 4:
        _ = f.function5(f.Ax, f.Ay, f.Bx, f.By)
    if option == 0:
        break
