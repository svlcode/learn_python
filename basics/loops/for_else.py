names = ["Vio", "Alina", "Andrei", "Lucian", "Claudia"]

for name in names:
    if name.startswith("T"):
        print("found")
        break
else:  # else clause executes if the for loops completes without hitting the break statement
    print("not found")
