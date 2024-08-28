def show_info(**details):
    for key, value in details.items():
        print(key, ":", value)

show_info(name="Arsh", age=20, occupation="Engineer")
