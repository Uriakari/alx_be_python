# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Divide numerator by denominator with robust error handling."""
    # Handle non-numeric inputs
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Handle division by zero using try/except (as required)
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # Successful division
    return f"The result of the division is {result}"
