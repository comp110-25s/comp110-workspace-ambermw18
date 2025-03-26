def count_regs(coi: str, counties: list) -> int:
    """count # of people from list in the county"""
    idx: int = 0  # Current index
    total: int = 0  # Total count of that county
    while idx < len(counties):
        if counties[idx] == coi:
            total += 1
        idx += 1
    return total


def hehe(n: int) -> int:
    return 0


print(count_regs("Orange", ["Wake", "Orange", "Orange", "Durham"]))

ice_cream: dict[str, float] = {
    "chocolate": 2.70,
    "cherry": 5,
    "vanilla": 3.50,
}

print(ice_cream["pecan"])
