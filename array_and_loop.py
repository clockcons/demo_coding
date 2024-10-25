def valid_name(name):
    return any([character.isdigit() for character in name])

def valid_age(age):
    if age >= 0 and age <= 100:
        return "ok"
    else:
        return "invalid"

while True:
    name = input("Please input name: ")
    if valid_name(name):
        print("Invalid Name")
        continue
    else:
        retry = input("Retry? ('Yes' or 'No'): ")
        if retry == "No":
            break
        elif retry == "Yes":
            continue
        else:
            print("Invalid Input")
            continue

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
        retry = input("Retry? ('Yes' or 'No'): ")
        if retry == "No":
            break
        elif retry == "Yes":
            continue
        else:
            print("Invalid Input")
            continue
