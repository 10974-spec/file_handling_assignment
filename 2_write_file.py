def write_to_file():
    """Write user input to a file with permission handling"""
    filename = input("Enter output filename: ")
    content = input("Enter text to save: ")
    
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"\nSuccessfully wrote to {filename}")
    except PermissionError:
        print("Error: No write permission for this file!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("\n=== FILE WRITER ===")
    write_to_file()
