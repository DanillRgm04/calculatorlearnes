def main():
    print("Hello learners!")

def addmultiplenumbers(numbers):
# recibe números y devuelve la suma
    return sum(numbers)

def multiplymultiplenumbers(numbers):
# recibe un número y devuelve la multiplicación
    result = 1
    for n in numbers:
        result *= n
    return result

def isiteven(num):
# verifica si un número es par 
    return isinstance(num, int) and num % 2 == 0

def isitaninteger(num):
# verifica si el número es un entero 
    return isinstance(num, int) or (isinstance(num, float) and num.is_integer())

if __name__ == "__main__":
    main()
