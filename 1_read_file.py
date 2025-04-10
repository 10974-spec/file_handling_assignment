def read_file():
    """Read and display contents of a file with error handling"""
    filename = input("Enter filename to read: ")
    try:
        with open(filename, 'r') as file:
            print("\n=== FILE CONTENT ===")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: '{filename}' not found!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("\n=== FILE READER ===")
    read_file()
