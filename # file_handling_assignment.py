# file_handling_assignment.py

def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line with a number: 42\n")
            file.write("This is the third line with a string: 'hello'\n")
        print("File created successfully!")
    except PermissionError:
        print("Permission denied to create the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This is the fourth line appended.\n")
            file.write("This is the fifth line appended with a number: 100\n")
            file.write("This is the sixth line appended with a string: 'world'\n")
        print("File updated successfully!")
    except PermissionError:
        print("Permission denied to update the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    create_file()
    read_file()
    append_to_file()

if __name__ == "__main__":
    main()