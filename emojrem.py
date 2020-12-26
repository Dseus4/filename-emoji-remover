import os

def main():
    dir = input("enter directory: ")
    for file_name in os.listdir(dir):
        edited = False
        edit_name = file_name
        for char in edit_name:
            if char > '\uffff':
                edit_name = edit_name.replace(char,'')
                edited = True
        if edited:
            os.rename(f'{dir}\\{file_name}', f'{dir}\\{edit_name}')
    print("renaming complete")


def __main__():
    main()
__main__()