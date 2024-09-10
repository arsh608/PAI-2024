file_name = r'task7.txt'

try:
    with open(file_name, 'r+') as file:
        content = file.read()
        print('Current file content:', content)

        while True:
            word_to_replace = input('Enter the word you want to replace: ')
            if word_to_replace in content:
                break
            else:
                print(f"'{word_to_replace}' not found in the file. Please try again.")

        old_text = input('Enter the text to replace: ')
        new_text = input('Enter the replacement text: ')

        content = content.replace(word_to_replace, word_to_replace.replace(old_text, new_text))

        file.seek(0)
        file.write(content)
        file.truncate()
        print('Replacement successful.')

except FileNotFoundError:
    print('Error: The file does not exist.')
except IOError:
    print('Error: Could not read or write to the file.')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
