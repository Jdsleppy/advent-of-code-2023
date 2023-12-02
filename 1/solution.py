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


replacements = {
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


def replace_spelled_out_digits(line: str) -> str:
    while True:
        spelled_out_digit_indices = [
            (spelled_out, line.find(spelled_out)) for spelled_out in replacements.keys()
        ]

        first_spelled_out_digit_index = min(
            (
                (spelled_out, i)
                for spelled_out, i in spelled_out_digit_indices
                if i >= 0  # words not found have i = -1
            ),
            key=lambda so_i: so_i[1],  # compare by found index
            default=None,
        )

        if first_spelled_out_digit_index is None:
            break

        line = line.replace(
            first_spelled_out_digit_index[0],
            str(replacements[first_spelled_out_digit_index[0]]),
            1,
        )

    return line


def get_codes2(lines: list[str]) -> Iterable[int]:
    for line in lines:
        line = replace_spelled_out_digits(line)
        ints = [char for char in line if char.isdigit()]
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
