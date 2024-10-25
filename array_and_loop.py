def valid_name(name):
    return any([character.isdigit() for character in name])

def valid_age(age):
    if age >= 0 and age <= 100:
        return "ok"
    else:
        return "invalid"

while True:
    while True:
        name = input("Please input name: ")
        if valid_name(name):
            print("Invalid Name")
        else:
            break
    while True:
        try:
            age = int(input("Please input age: "))
            if valid_age(age) == "invalid":
                print("Invalid Age")
                continue
        except ValueError:
            print("Age must be a number")
            continue
        else:
            break
    entry = input("Would you want to input another entry? ('Yes' or 'No'): ")
    if entry == "Yes":
        continue
    elif entry == "No":
        break
    else:
        print("Invalid Input")
