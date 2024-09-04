try:
    find= str(input("Enter the word to find: "))
    replace= str(input("Enter the word to replace with: "))
    with open('example.txt', 'r') as file:
        content = file.read()
        if find in content:
            content= content.replace(find, replace)
            file.close()
            with open('example.txt','w') as file:
                file.write(content)
        else:
            print("Word not found")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
