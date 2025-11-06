itm = input("What is the item ? :").title().strip()


#option 1
'''
if itm == "Apple":
    print("Fruit")
elif itm == "Banana":
    print("Fruit")
elif itm == "Mango":
    print("Fruit")
elif itm == "Rose":
    print("Flower")
elif itm == "Lily":
    print("Flower")
elif itm == "Potato":
    print("Vegetable")
elif itm == "Tomato":
    print("Vegetable")
else:
    print("Item not listed, please add the item")
'''

#option 2
'''
if itm == "Apple" or itm == "Banana" or itm == "Mango":
    print("Fruit")
elif itm == "Rose" or itm == "Lily":
    print("Flower")
elif itm == "Potato" or itm == "Tomato":
    print("Vegetable")
else:
    print("Item not listed, please add the item")
'''

#option 3
'''
match itm:
    case "Apple":
        print("Fruit")
    case "Banana":
        print("Fruit")
    case "Mango":
        print("Fruit")
    case "Rose":
        print("Flower")
    case "Lily":
        print("Flower")
    case "Potato":
        print("Vegetable")
    case "Tomato":
        print("Vegetable")
    case _:
        print("Item not listed, please add the item")    
'''

#option 4
match itm:
    case "Apple" | "Banana" | "Mango":
        print("Fruit")
    case "Rose" | "Lily":
        print("Flower")
    case "Potato" | "Tomato":
        print("Vegetable")
    case _:
        print("Item not listed, please add the item")    
