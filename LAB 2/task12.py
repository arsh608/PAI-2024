def lists_to_dict(keys, values):
    if len(keys) != len(values):
        print("Error: Both lists must have the same number of elements.")
        return None

    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]

    return result_dict


# Example usage
keys_list = ["name", "age", "city"]
values_list = ["Arsh", 20, "karachi"]
result = lists_to_dict(keys_list, values_list)
print(result)
