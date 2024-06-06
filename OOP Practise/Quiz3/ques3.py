class Calculation:
    def calculation(self, number1, number2):
        try:
            result = number1 / number2
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

# Example usage
calc = Calculation()

# Test cases
result1 = calc.calculation(10, 2)  # Should return 5.0
result2 = calc.calculation(10, 0)  # Should handle division by zero

print(f"Result of 10 / 2: {result1}")
print(f"Result of 10 / 0: {result2}")
