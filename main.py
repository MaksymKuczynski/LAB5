from src.power_grid import GridManager, ThermalPlant, NuclearPlant, RenewablePlant


def main():
    print("=== Симулятор енергомережі «ЕнергоБаланс» ===")

    # Створення мережі
    grid = GridManager("Київська Енергомережа")

    # Створення станцій
    tpp = ThermalPlant(1, "Трипільська ТЕС", 800, "вугілля")
    npp = NuclearPlant(2, "Рівненська АЕС", 2000, 4)
    solar = RenewablePlant(3, "Сонячна станція Світанок", 150, "сонце")

    # Встановлюємо поточну генерацію
    tpp.current_output = 400
    npp.current_output = 1800
    solar.current_output = 100

    # Додаємо станції в менеджер
    grid.add_plant(tpp)
    grid.add_plant(npp)
    grid.add_plant(solar)

    print(f"\n{grid}")
    print("-" * 50)

    print("\n1. Список усіх станцій:")
    for plant in grid.get_all():
        print(f" - {plant} ({plant.get_info()})")

    print(f"\n2. Загальна потужність мережі: {grid.get_total_capacity()} МВт")
    print(f"3. Поточна генерація мережі: {grid.get_total_output()} МВт")

    print("\n4. Фільтрація (тільки відновлювані станції):")
    for green in grid.filter_by_type(RenewablePlant):
        print(f" - {green}")


if name == "main":
    main()