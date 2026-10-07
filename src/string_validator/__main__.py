from .validator import Validator, ValidationError

def main():
    text = input("Введіть строку: ")
    validator = Validator()
    if validator.validate(text):
        print("Строка валідна")

if __name__ == "__main__":
    main()