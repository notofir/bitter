import random

TOTAL = 1000000
RANGE = 100


def main():
    accumulative_count = 0
    with open("binary.bin", "w") as file:
        while accumulative_count < TOTAL:
            count = random.randrange(min((RANGE, TOTAL - accumulative_count)) + 1)
            file.write(count * str(random.randrange(2)))
            accumulative_count += count


if __name__ == "__main__":
    main()
