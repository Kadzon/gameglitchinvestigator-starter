import pytest
from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score


# ===== check_guess Tests =====

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    # Fixed bug: should say "Go LOWER!" not "Go HIGHER!"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    # Fixed bug: should say "Go HIGHER!" not "Go LOWER!"
    assert message == "📈 Go HIGHER!"


def test_check_guess_with_string_secret():
    # Test the TypeError exception handler for string secret
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_check_guess_string_secret_too_low():
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_check_guess_string_secret_win():
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"
    assert message == "🎉 Correct!"


# ===== parse_guess Tests =====

def test_parse_guess_valid_integer():
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None


def test_parse_guess_valid_float():
    ok, value, error = parse_guess("42.5")
    assert ok is True
    assert value == 42
    assert error is None


def test_parse_guess_empty_string():
    ok, value, error = parse_guess("")
    assert ok is False
    assert value is None
    assert error == "Enter a guess."


def test_parse_guess_none():
    ok, value, error = parse_guess(None)
    assert ok is False
    assert value is None
    assert error == "Enter a guess."


def test_parse_guess_not_a_number():
    ok, value, error = parse_guess("abc")
    assert ok is False
    assert value is None
    assert error == "That is not a number."


def test_parse_guess_negative_number():
    # Fixed bug: should reject negative numbers
    ok, value, error = parse_guess("-5")
    assert ok is False
    assert value is None
    assert error == "Guess must be a positive number."


def test_parse_guess_zero():
    # Fixed bug: should reject zero
    ok, value, error = parse_guess("0")
    assert ok is False
    assert value is None
    assert error == "Guess must be a positive number."


def test_parse_guess_negative_float():
    ok, value, error = parse_guess("-3.5")
    assert ok is False
    assert value is None
    assert error == "Guess must be a positive number."


# ===== get_range_for_difficulty Tests =====

def test_easy_difficulty_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_normal_difficulty_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50


def test_hard_difficulty_range():
    # Fixed bug: Hard should be harder than Normal
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100
    # Verify Hard is harder than Normal
    _, normal_high = get_range_for_difficulty("Normal")
    assert high > normal_high


def test_difficulty_range_invalid():
    # Should default to Normal range for invalid difficulty
    low, high = get_range_for_difficulty("Impossible")
    assert low == 1
    assert high == 100


def test_difficulty_ranges_are_progressive():
    # Easy < Normal < Hard
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    assert easy_high < normal_high
    assert normal_high < hard_high


# ===== update_score Tests =====

def test_update_score_win():
    score = update_score(0, "Win", 1)
    # 100 - 10 * (attempt_number + 1) = 100 - 10 * 2 = 80
    assert score == 80


def test_update_score_win_many_attempts():
    # Minimum points should be 10
    score = update_score(0, "Win", 50)
    assert score >= 10


def test_update_score_too_high_even_attempt():
    score = update_score(0, "Too High", 2)
    assert score == 5


def test_update_score_too_high_odd_attempt():
    score = update_score(0, "Too High", 1)
    assert score == -5


def test_update_score_too_low():
    score = update_score(0, "Too Low", 1)
    assert score == -5


def test_update_score_accumulates():
    # Score should accumulate
    score = 100
    score = update_score(score, "Too High", 2)
    assert score == 105
    score = update_score(score, "Too Low", 3)
    assert score == 100
