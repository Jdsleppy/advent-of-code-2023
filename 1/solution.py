from typing import Iterable


def get_lines() -> list[str]:
    with open("input.txt") as f:
        return [line.strip() for line in f if line]


def get_codes(lines: list[str]) -> Iterable[int]:
    for line in lines:
        ints = [char for char in line if char.isdigit()]
        yield int(f"{ints[0]}{ints[-1]}")


def main1():
    lines = get_lines()
    codes = get_codes(lines)
    answer = sum(codes)
    print(f"The answer to part 1 is {answer}")


digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_digits(line: str) -> list[int]:
    digits_and_indices: list[tuple[int, int]] = []

    for spelled_out, as_int in digits.items():
        search_position = 0
        while True:
            found_index = line.find(spelled_out, search_position)
            if found_index == -1:
                break
            digits_and_indices.append((as_int, found_index))
            search_position = found_index + 1

    for as_int in digits.values():
        as_str = str(as_int)
        search_position = 0
        while True:
            found_index = line.find(as_str, search_position)
            if found_index == -1:
                break
            digits_and_indices.append((as_int, found_index))
            search_position = found_index + 1

    return [
        digit for digit, _ in sorted(digits_and_indices, key=lambda d_and_i: d_and_i[1])
    ]


def get_codes2(lines: list[str]) -> Iterable[int]:
    for line in lines:
        ints = get_digits(line)
        code = int(f"{ints[0]}{ints[-1]}")
        yield code


def main2():
    lines = get_lines()
    codes = list(get_codes2(lines))
    answer = sum(codes)
    print(f"The answer to part 2 is {answer}")


if __name__ == "__main__":
    main1()
    main2()
