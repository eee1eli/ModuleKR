def is_non_decreasing(values: list[int]) -> bool:
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))


def main() -> None:
    
    RESET = "\033[0m"
    RED = "\033[31m"
    BLUE = "\033[34m"

    
    arr = [2, 9, 12, 13, 15, 12, 2, 0, 6, 6, 3, 2]

    print(f"Масив {BLUE}{len(arr)}{RESET} елементів:")
    print(RED + " ".join(map(str, arr)) + RESET)

    raw = input(f"Введіть номера елемента масиву: {RED}").strip()
    print(RESET, end="")
    try:
        idx = int(raw)
    except ValueError:
        print("Помилка: потрібно ввести ціле число.")
        return

    if idx < 0 or idx >= len(arr):
        print(f"Помилка: номер повинен бути в межах 0..{len(arr) - 1}.")
        return

    part = arr[: idx + 1]
    print(f"Масив {BLUE}{idx}{RESET} елементів:")
    print(RED + " ".join(map(str, part)) + RESET)

    if is_non_decreasing(part):
        print("Упорядковано за зростанням")
    else:
        print("НЕ упорядковано за зростанням")


if __name__ == "__main__":
    main()

