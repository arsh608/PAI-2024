file_name = r'task6.txt'

def write_question_to_file() -> None:

    try:
        with open(file_name, 'w') as file:
            user_input = input('Enter a sentence: ')
            if user_input.endswith('?'):
                file.write(user_input)
                print('Write successful')
            else:
                print('Input is not a question (no question mark at the end).')

    except FileNotFoundError:
        print('Error: The file does not exist.')
    except IOError:
        print('Error: Could not read/write to the file.')
    except Exception as e:
        print(f'Unexpected error occurred: {e}')

write_question_to_file()
