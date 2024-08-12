import os

def create_file():
    filename = input("Enter the name of the file to create: ")
    if os.path.exists(filename):
        print("File already exists.")
    else:
        with open(filename, "w") as file:
            print(f"File '{filename}' created successfully.")

def write_to_file():
    filename = input("Enter the name of the file to write to: ")
    if not os.path.exists(filename):
        print("File does not exist. Please create the file first.")
    else:
        content = input("Enter the content to write to the file:\n")
        with open(filename, "a") as file:
            file.write(content + "\n")
        print(f"Content written to '{filename}' successfully.")

def read_file():
    filename = input("Enter the name of the file to read: ")
    if not os.path.exists(filename):
        print("File does not exist.")
    else:
        with open(filename, "r") as file:
            content = file.read()
            print(f"Content of '{filename}':\n{content}")

def rename_file():
    old_name = input("Enter the current name of the file: ")
    if not os.path.exists(old_name):
        print("File does not exist.")
    else:
        new_name = input("Enter the new name for the file: ")
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}' successfully.")

def delete_file():
    filename = input("Enter the name of the file to delete: ")
    if not os.path.exists(filename):
        print("File does not exist.")
    else:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")

def list_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    if files:
        print("Files in the current directory:")
        for f in files:
            print(f"- {f}")
    else:
        print("No files found in the current directory.")

def menu():
    while True:
        print("\nFile Management Menu:")
        print("1. Create File")
        print("2. Write to File")
        print("3. Read File")
        print("4. Rename File")
        print("5. Delete File")
        print("6. List Files")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            create_file()
        elif choice == '2':
            write_to_file()
        elif choice == '3':
            read_file()
        elif choice == '4':
            rename_file()
        elif choice == '5':
            delete_file()
        elif choice == '6':
            list_files()
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    menu()
