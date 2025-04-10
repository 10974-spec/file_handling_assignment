from importlib import import_module

def main():
    while True:
        print("\n" + "="*40)
        print("FILE HANDLING DEMO")
        print("="*40)
        print("1. Read a File")
        print("2. Write to a File")
        print("3. Calculate Average")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        if choice == '1':
            import_module("1_read_file")
        elif choice == '2':
            import_module("2_write_file")
        elif choice == '3':
            import_module("3_calculate_average")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
