try:
    with open("Demo.txt") as file:
        print(file.read())
finally:
    file.close()