import math
import json
import os

# =================== CONFIG ====================
HISTORY_FILE = "math_history.json"
MAX_HISTORY = 20
# =============== MATH FUNCTIONS =================

def add(a,b): return a + b
def subtract(a,b): return a - b
def multiply(a, b): return a * b

def divide(a,b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    return a / b

def power(a, b): return a ** b

def square_root(a):
    if a < 0:
        print("Error: Cannot take the square root of a negative number!")
        return None
    return math.sqrt(a)

# =========== HISTORY =========================
history = []                

def load_history():
    """Load history from the file when program starts"""
    global history
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                history = json.load(f)
        except:
            history = []

def save_history():
    """Save history to file"""
    try:
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f, indent=2)
    except:
        pass # Silently fail if can't save (e.g. permission issue)

def add_to_history(operation, a, b=None, result=None):
    """Add a calculation to history (keeps only last MAX_HISTORY entries)"""
    if b is not None:
        entry = f"{a} {operation} {b} = {result}"
    else:
        entry = f"{operation} ({a}) = {result}"

    history.append(entry)
    if len(history) > MAX_HISTORY:
        history.pop(0)  

def show_history():
    """Display calculation history"""
    print("\n" + "="*50)
    print("\n        CALCULATION HISTORY ")
    print("="*50)
    if not history:
        print("No calculation yet.")
    else:
        for i, entry in enumerate(history, 1):
            print(f"{i:2d}. {entry}")

    print("="*40)
    print(f"Total entries: {len(history)} / {MAX_HISTORY}")

def clear_history():
    global history
    history.clear()
    save_history()
    print("History has been cleared.")


# ============ MAIN PROGRAM ===================
def main():
    load_history()          # Load previous history
    print("=== Personal Math Helper===\n")

    while True:
        print("1. Add           2. Subtract     3.Multiply")
        print("4. Divide        5. Power a^b    6. Square Root")
        print("7. Show History  8. Clear History    9. Quit")
       

        choice = input("Choose an option (1-9): ").strip()

        if choice == "9":
            print("Goodbye! History has been saved.")
            break

        try:
            if choice in ["1", "2", "3", "4", "5"]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    result = add(a, b)
                elif choice == "2":
                    result = subtract(a, b)
                elif choice == "3":
                    result = multiply(a, b)
                elif choice == "4":
                    result = divide(a, b)
                    if result is None: continue
                elif choice == "5":
                    result = power(a, b)
        
                print(f"Result: {result}\n")
                add_to_history(["+", "-", "*", "/", "^"][int(choice)-1], a, b, result)


            elif choice == "6":
                a = float(input("Enter number: "))
                result = square_root(a)
                if result is not None:
                    print(f"Result: {result}")
                    add_to_history("√", a, result=result)
    
            elif choice == "7":
                show_history() 
            elif choice == "8":
                clear_history()
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter valid numbers!")

# Run the program
if __name__ == "__main__":
    main()
