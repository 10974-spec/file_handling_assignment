def calculate_average():
    """Calculate average from numbers in a file"""
    filename = input("Enter numbers filename: ")
    
    try:
        with open(filename, 'r') as file:
            numbers = []
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Ignoring non-number: {line.strip()}")
            
            if not numbers:
                raise ValueError("No valid numbers found!")
            
            avg = sum(numbers) / len(numbers)
            print(f"\nAverage: {avg:.2f}")
            
    except FileNotFoundError:
        print(f"Error: '{filename}' not found!")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("\n=== NUMBER AVERAGE CALCULATOR ===")
    calculate_average()
