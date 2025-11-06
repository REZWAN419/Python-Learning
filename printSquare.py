#print square with # using nested for loop

def print_square(height,width):
    for column in range(height):
        for row in range(width):
            print("#", end="")
        print()


print_square(4,3)
