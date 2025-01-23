"""The goal of this exercise is to write a program to help plan a cozy tea party"""

__author__: str = "730678501"


def main_planner(guests: int) -> None:
    """entrypoint of program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    return None


def tea_bags(people: int) -> int:
    """calculates number of tea bags needed per number of guests attending"""
    return 2 * people


def treats(people: int) -> int:
    """calculates number of treates based on number of teas"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """computes cost of tea bags and treats combined"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
