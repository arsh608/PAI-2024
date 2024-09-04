def save(filename, dictionary):
    try:
        jstring = str(dictionary).replace("'", '"')
        with open(filename, 'w') as file:
            file.write(jstring)
        print(f"Dictionary successfully saved to {filename}.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def load(filename):
    try:
        with open(filename, 'r') as file:
            jstring = file.read()
            dictionary = eval(jstring.replace('"', "'"))
        return dictionary

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def find_max(dictionary):
    if not dictionary:
        print("No data to process.")
        return

    max_age = -1
    person_mage = None
    count = {}

    for name, age in dictionary.items():
        if age > max_age:
            max_age = age
            person_mage = name
        if age in count:
            count[age].append(name)
        else:
            count[age] = [name]

    print(f"Person with the maximum age: {person_mage} ({max_age} years)")

    same_age = count.get(max_age, [])
    if len(same_age) > 1:
        print(f"People with the same age ({max_age} years): {', '.join(same_age)}")

dictionary = {'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23}
filename = 'task5.json'

save(filename, dictionary)
loaded_dict = load(filename)
find_max(loaded_dict)
