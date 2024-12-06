arr = [10, 5, 15, 20]

try:
    divisor = int(input("Enter an integer divisor: "))
    for i in range(len(arr)):
        print(f"Result of {arr[i]} / {divisor} = {arr[i] / divisor}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
except NameError:
    print("Error: Undefined variable or invalid name used.")
except TypeError:
    print("Error: Incompatible types encountered.")
except IndexError:
    print("Error: Index out of bounds.")
except AttributeError:
    print("Error: Invalid attribute reference.")
except FileNotFoundError:
    print("Error: File not found (though unrelated in this context).")
else:
    print("Division performed successfully!")
finally:
    print("Execution completed.")
