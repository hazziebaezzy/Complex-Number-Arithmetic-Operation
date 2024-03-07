from Complex_class import Complex  # Importing the Complex class from the Complex_class.py (add new file)

if __name__ == "__main__":
    # Input for first complex number
    a_str, b_str = input().split()  # Prompt user to input the first complex number as a string, then split it into real and imaginary parts
    a = float(a_str)  # Convert the real part of the first complex number to a floating-point number
    b = float(b_str)  # Convert the imaginary part of the first complex number to a floating-point number
    c1 = Complex(a, b)  # Create a Complex object with the specified real and imaginary parts
    
    # Input for second complex number
    c_str, d_str = input().split()  # Prompt user to input the second complex number as a string, then split it into real and imaginary parts
    c = float(c_str)  # Convert the real part of the second complex number to a floating-point number
    d = float(d_str)  # Convert the imaginary part of the second complex number to a floating-point number
    c2 = Complex(c, d)  # Create a Complex object with the specified real and imaginary parts
    
    # Print results of operations between the two complex numbers
    # Print the result of adding the two complex numbers
    resultsum = c1 +  c2
    print(f"({c1}) + ({c2}) = {resultsum}")
    
    # Print the result of subtracting the second complex number from the first
    resultdiff = c1 - c2
    print(f"({c1}) - ({c2}) = {resultdiff}")
    
    # Print the result of multiplying the two complex numbers
    resultproduct = c1 * c2
    print(f"({c1}) * ({c2}) = {c1 * c2}")
    
    try:
        # Print the result of dividing the first complex number by the second
        resultdiv = c1 / c2
        print(f"({c1}) / ({c2}) = {resultdiv}")
    except ZeroDivisionError as e:
        print("Error.", e)
        
    # Print the absolute value (magnitude) of the first complex number
    absolutevalue = c1.abs()
    print(f"|({c1})| = {absolutevalue}")