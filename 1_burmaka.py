import os


def main() -> None:
    var_name = "BURMAKA_SURNAME"
    value = os.environ.get(var_name)

    if not value:
        print(f"Змінну середовища {var_name} не знайдено.")
        return

    print(f"{var_name} = {value}")


if __name__ == "__main__":
    main()

