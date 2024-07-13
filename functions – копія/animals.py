def show_animals(animals: list) -> None:
    delimeter = "-" * 28
    template = "|{:<5}|{:<20}|"
    print(delimeter)
    print(template.format("№", "Назва товару"))
    print(delimeter)
    for i, product in enumerate(animals, start=1):
        print(template.format(i, product))
    print(delimeter)


def add_animals(animals: list) -> list:
        animal = input("Введіть ім'я тварини для додавання до списку: ")
        if animal not in animals:
            animal.append
            print(f"Тварина під назвою '{animal}' додана до списку")
            input("\nНатисніть Enter для продовження ")
        else:
            print("Така тваринка вже є під такою назвою у списку")
            input("\nНатисніть Enter для продовження ")


def animal_cured(animals: list) -> list:
        animal = input("Введіть ім'я тварини яку вилікували")
        if animal in animals:
            animals.remove(animal)
            print(f"Тваринa під назвою '{animal}' вилікувано")
            animal_cured.append(animal)


def animal_cureds(animals: list) -> list:
        for animals in animal_cured:
            print(animal_cured)


def palindrome(animals: list):
        palin_animals = [animal for animal in animals if animal.lower() == animal[::-1].lower()]
        input(f"\nУ списку з продуктами є такі слова-паліндроми: {palin_animals}\n")
