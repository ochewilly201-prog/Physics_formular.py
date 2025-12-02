def show_menu():
    """Displays the menu of physics formulas."""
    print("\nWelcome to the Physics Calculator")
    print("\nSelect a Physics Formula:")
    print("1. Speed = Distance/Time")
    print("2. Force = Mass * Acceleration")
    print("3. Work done = Force * Distance")
    print("4. Pressure = Force/Area")
    print("5. Density = Mass/Volume")


def calculate(choice):
    """Performs the calculation based on the user's choice."""
    if choice == "1":
        # Speed = Distance / Time
        d = float(input("Enter Distance (m): "))
        t = float(input("Enter time (s): "))
        print(f"Speed = {d / t} m/s")

    elif choice == "2":
        # Force = Mass * Acceleration
        m = float(input("Enter Mass (kg): "))
        a = float(input("Enter Acceleration (m/s^2): "))
        print(f"Force = {m * a} N")

    elif choice == "3":
        # Work done = Force * Distance
        f = float(input("Enter Force (N): "))
        d = float(input("Enter Distance (m): "))
        print(f"Work done = {f * d} J")

    elif choice == "4":
        # Pressure = Force / Area
        f = float(input("Enter Force (N): "))
        a = float(input("Enter Area (m^2): "))
        print(f"Pressure = {f / a} Pa")

    elif choice == "5":
        # Density = Mass / Volume
        m = float(input("Enter Mass (kg): "))
        v = float(input("Enter Volume (m^3): "))
        print(f"Density = {m / v} kg/m^3")

    else:
        print("Invalid choice! Please enter a number from 1 to 5 or 'q' to quit.")


# --- Corrected main function and execution block ---

def main():
    """Main function to run the calculator loop."""
    while True:
        show_menu()
        choice = input("Enter choice (1-5) or 'q' to quit: ")

        if choice.lower() == "q":
            print("Goodbye!")
            break  # C. ONLY break when the user quits

        # C. Call the calculate function for any other valid choice
        calculate(choice)


# B. Corrected standard execution block (double underscores)
if __name__ == "__main__":
    main()