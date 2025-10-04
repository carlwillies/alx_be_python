# programming_paradigm/robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling for:
    - Non-numeric inputs
    - Division by zero
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
