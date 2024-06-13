from complex_number import ComplexNumber
import logging

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def add(self, num1: ComplexNumber, num2: ComplexNumber) -> ComplexNumber:
        result = ComplexNumber(num1.real + num2.real, num1.imag + num2.imag)
        self.logger.info(f"Adding {num1} and {num2}: {result}")
        return result

    def multiply(self, num1: ComplexNumber, num2: ComplexNumber) -> ComplexNumber:
        real = num1.real * num2.real - num1.imag * num2.imag
        imag = num1.real * num2.imag + num1.imag * num2.real
        result = ComplexNumber(real, imag)
        self.logger.info(f"Multiplying {num1} and {num2}: {result}")
        return result

    def divide(self, num1: ComplexNumber, num2: ComplexNumber) -> ComplexNumber:
        if num2.real == 0 and num2.imag == 0:
            self.logger.error("Attempt to divide by zero")
            raise ValueError("Cannot divide by zero")

        denom = num2.real**2 + num2.imag**2
        real = (num1.real * num2.real + num1.imag * num2.imag) / denom
        imag = (num1.imag * num2.real - num1.real * num2.imag) / denom
        result = ComplexNumber(real, imag)
        self.logger.info(f"Dividing {num1} by {num2}: {result}")
        return result