from complex_number import ComplexNumber
from operations import Calculator
from logger import setup_logger

def main():
    setup_logger()

    num1 = ComplexNumber(3, 2)
    num2 = ComplexNumber(1, 7)

    calculator = Calculator()

    print("Addition:", calculator.add(num1, num2))
    print("Multiplication:", calculator.multiply(num1, num2))
    print("Division:", calculator.divide(num1, num2))

if __name__ == "__main__":
    main()