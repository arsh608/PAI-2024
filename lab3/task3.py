def lists_to_dict(keys, values):
    if len(keys) != len(values):
        print("Error: Both lists must have the same number of elements.")
        return None
    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]

    return result_dict

def write_to_file(filename, dictionary):

    try:
        with open(filename, 'w') as file:
            for key, value in dictionary.items():
                file.write(f"{key}: {value}\n")
        print(f"Dictionary successfully written to {filename}")
    except IOError:
        print(f"Error: An I/O error occurred while writing to the file '{filename}'.")


try:
    keys_input = input("Enter the keys list, separated by commas: ")
    values_input = input("Enter the values list, separated by commas: ")

    keys_list = [key.strip() for key in keys_input.split(',')]
    values_list = [value.strip() for value in values_input.split(',')]

    result_dict = lists_to_dict(keys_list, values_list)

    if result_dict is not None:
        filename = 'task3.txt'

        write_to_file(filename, result_dict)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
