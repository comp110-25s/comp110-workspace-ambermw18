"""Some practice with dictionary functions"""

__author__: str = "730678501"


def invert(inputs: dict[str, str]) -> dict[str, str]:
    """A function that reverses the keys and values of a dictionary"""
    inverted_inputs = {}
    for key in inputs:
        value = inputs[key]
        if value in inverted_inputs:
            raise KeyError("Duplicate found, cannot invert dictionary!")
        inverted_inputs[value] = key
    return inverted_inputs


def count(values: list[str]) -> dict[str, int]:
    """Takes a list and puts it into a dictionary based on count"""
    final = {}
    for item in values:
        if item in final:
            final[item] += 1
        else:
            final[item] = 1
    return final


def favorite_color(assignments: dict[str, str]) -> str:
    """Returns most popular favorite color from dictionary"""
    color_counts = {}
    for name in assignments:
        color = assignments[name]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    max_count = 0
    result = ""
    for color in color_counts:
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            result = color
    return result


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins strings into a dictionary"""
    bins = {}
    for word in words:
        length = len(word)
        if length not in bins:
            bins[length] = set()
        bins[length].add(word)
    return bins
