print("="*50)
print("Print colour Name:")
print("="*50)
print("\tV -> Violet")
print("\tI -> Indigo")
print("\tB -> Blue")
print("\tG -> Green")
print("\tY -> Yellow")
print("\tO -> Orange")
print("\tR -> Red")
print("="*50)
choice=input("Enter your Choice:")
match(choice):
    case 'V':
        print("V -> Violet")
    case 'I':
        print("I -> Indigo")
    case 'B':
        print("B -> Blue")
    case 'G':
        print("G -> Green")
    case 'Y':
        print("Y -> Yellow")
    case 'O':
        print("O -> Orange")
    case 'R':
        print("R -> Red")
    case _:
        print("Invalid Input")
