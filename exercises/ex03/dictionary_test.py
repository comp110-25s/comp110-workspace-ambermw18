"""Test file for dictionary functions"""

__author__: str = "730678501"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


# tests for invert function
def test_invert1() -> None:
    """Testing first use case for invert"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert2() -> None:
    """Testing second use case for invert"""
    assert invert(
        {
            "apple": "cat",
        }
    ) == {"cat": "apple"}


def test_invert3() -> None:
    """Testing edge case for invert"""
    assert invert({}) == {}


def test_invert4() -> None:
    """Testing duplicate values to raise a KeyError"""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


# tests for count function
def test_count1() -> None:
    """Testing first use case for count"""
    assert count(["apple", "banana", "apple", "orange", "banana", "apple"]) == {
        "apple": 3,
        "banana": 2,
        "orange": 1,
    }


def test_count2() -> None:
    """Testing second use case for count"""
    assert count(["apple"]) == {"apple": 1}


def test_count3() -> None:
    """Testing edge case for count"""
    assert count([]) == {}


# tests for favorite_color function
def test_favorite_color1() -> None:
    """Testing first use case for favorite_color"""
    assignments = {"Amber": "pink", "Olivia": "blue", "Tayla": "pink", "Niki": "red"}
    assert favorite_color(assignments) == "pink"


def test_favorite_color2() -> None:
    """Testing second use case for favorite_color"""
    assignments = {
        "Nicole": "purple",
        "Gabby": "purple",
        "Lydia": "blue",
        "Amber": "pink",
        "Ella": "pink",
        "Bailey": "blue",
    }
    assert favorite_color(assignments) == "purple"


def test_favorite_color3() -> None:
    """Testing edge case for favorite_color"""
    assignments = {"Amber": "pink"}
    assert favorite_color(assignments) == "pink"


# tests for bin_len function
def test_bin_len1() -> None:
    """Testing base case for bin_len"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len2() -> None:
    """Testing second base case for bin_len"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len3() -> None:
    """Testing edge case for bin_len"""
    assert bin_len([]) == {}
