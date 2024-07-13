import json

from files import list_files


def save_animals(animals: list) -> None:
    with open(list_files.ANIMALS, "w", encoding="utf-8") as fh:
        animals = [f"{animal}\n" for animal in animals]
        fh.writelines(animals)


def save_log(log: list) -> None:
    with open(list_files.LOG, "w", encoding="utf-8") as fh:
        log = [f"{loging}\n" for loging in log]
        fh.writelines(log)


def save_employees(employees: dict) -> None:
    with open(list_files.EMPLOYEES, "w", encoding="utf-8") as fh:
        json.dump(employees, fh, indent=4)


def save_animal_cureds( animal_cured: list) -> None:
    with open(list_files.PRODUCTS_SOLD, "w", encoding="utf-8") as fh:
        json.dump(animal_cured, fh, indent=4)


def save_using_commands(using_commands: dict) -> None:
    with open(list_files.USING_COMMANDS, "w", encoding="utf-8") as fh:
        json.dump(using_commands, fh, indent=4)


def save_reviews(reviews: list) -> None:
    with open(list_files.REVIEWS, "w", encoding="utf-8") as fh:
        json.dump(reviews, fh, indent=4)