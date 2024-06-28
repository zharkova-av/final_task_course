import csv
from collections import Counter


def read_file(filename: str) -> list[dict]:
    """Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """
    result: list[dict] = []
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            if i > 0:
                (
                    area_id,
                    house_address,
                    floor_count,
                    heating_house_type,
                    heating_value,
                    area_residential,
                    population,
                ) = line
                result.append(
                    {
                        "area_id": area_id,
                        "house_address": house_address,
                        "floor_count": int(floor_count),
                        "heating_house_type": heating_house_type,
                        "heating_value": float(heating_value),
                        "area_residential": float(area_residential),
                        "population": int(population),
                    },
                )
    return result


def classify_house(floor_count: int) -> str:
    """Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", "Среднеэтажный" или "Многоэтажный".
    """
    zero_floor = 0
    first_floor = 1
    fifth_floor = 5
    six_floor = 6
    sixteenth_floor = 16

    if not isinstance(floor_count, int):
        type_error_message = "floor_count must be integer"
        raise TypeError(type_error_message)
    if floor_count <= zero_floor:
        value_error_message = "floor_count must be > 0"
        raise ValueError(value_error_message)
    if first_floor <= floor_count <= fifth_floor:
        return "Малоэтажный"
    if six_floor <= floor_count <= sixteenth_floor:
        return "Среднеэтажный"
    return "Многоэтажный"


def get_classify_houses(houses: list[dict]) -> list[str]:
    """Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    classified_houses: list[str] = [classify_house(house["floor_count"]) for house in houses]
    return classified_houses


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    return dict(Counter(categories))


def min_area_residential(houses: list[dict]) -> str:
    """Находит адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.
    """
    house_min = houses[0]
    min_avg_area_per_population = float(house_min["area_residential"]) / float(house_min["population"])
    for house in houses:
        avg_area_per_population = float(house["area_residential"]) / float(house["population"])
        if avg_area_per_population < min_avg_area_per_population:
            house_min = house
            min_avg_area_per_population = avg_area_per_population
    return house_min["house_address"]
