# main.py - TUI version
# A terminal-based interface for the Infinity Approximator

import sys
from modules import series_approximations

def main():
    print("Infinity Approximator - TUI Version")
    print("Choose a function to approximate:")
    print("1. e (Euler's Number)")
    print("2. π (Pi)")
    print("3. sin(x)")
    print("4. ln(1 + x)")

    choice = input("Enter your choice (1-4): ")
    terms = int(input("Enter number of terms: "))

    if choice == '1':
        print("Approximation of e:", series_approximations.e_approx(terms))
    elif choice == '2':
        print("Approximation of pi:", series_approximations.pi_approx(terms))
    elif choice == '3':
        x = float(input("Enter value of x in radians: "))
        print("Approximation of sin(x):", series_approximations.sin_approx(x, terms))
    elif choice == '4':
        x = float(input("Enter value of x (x > -1): "))
        print("Approximation of ln(1 + x):", series_approximations.ln1p_approx(x, terms))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
