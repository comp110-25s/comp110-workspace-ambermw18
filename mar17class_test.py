"""Test functions in feb7class module."""

from mar17class import count_regs, hehe


def test_hehe() -> None:
    # other code can be here!
    assert hehe(5) == 0


def test_count_regs_use1() -> None:
    """Testing use case"""
    assert count_regs("Orange", ["Wake", "Orange", "Orange", "Durham"]) == 2


def test_count_regs_empty() -> None:
    """Testing edge case"""
    assert count_regs("Orange", []) == 0


def test_count_regs_mutate() -> None:
    """Test if count_regs mutates list."""
    cs: list[str] = ["Orange", "Wake", "Lee"]
    count_regs("Orange", cs)
    assert cs == ["Orange", "Wake", "Lee"]
