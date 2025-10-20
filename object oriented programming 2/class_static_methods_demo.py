class Calculator:
    calculation_type="Arithmetic operations"
    @classmethod
    def multiply(cls,a,b):
        print(f"calculation_type:{cls.calculation_type}")
        return a*b
    @staticmethod
    def add(a,b):
        return a+b