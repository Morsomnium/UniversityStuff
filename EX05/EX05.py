"""Test for EX02."""
import EX02


def test_already_correct():
    """Test already correct/normalized input."""
    assert EX02.normalize_equation("3x2 + 2x + 1 = 0") == "3x2 + 2x + 1 = 0"


def test_missing_linear_component():
    """Test the case when the linear component is missing."""
    assert EX02.normalize_equation("3x2 + 5 = 0") == "3x2 + 5 = 0"


def test_neg_x2():
    """Check x2 negative value."""
    assert EX02.normalize_equation('-x2 + 5x + 3 = 0') == 'x2 - 5x - 3 = 0'


def test_neg_x():
    """Check linear negative value."""
    assert EX02.normalize_equation('-5x + 3 = 0') == '5x - 3 = 0'


def test_neg_f():
    """Check free negative value."""
    assert EX02.normalize_equation('-3 = 0') == '3 = 0'


def test_one_mult_x2():
    """Clear 1 multiplier."""
    assert EX02.normalize_equation("1x2 + 5x + 3") == "x2 + 5x + 3 = 0"


def test_one_mult_x():
    """Clear 1 multiplier."""
    assert EX02.normalize_equation("1x + 3") == "x + 3 = 0"


def test_one_mult_f():
    """Clear 1 multiplier."""
    assert EX02.normalize_equation("13") == "13 = 0"


def test_zero_mult():
    """Clear 0 multiplier."""
    assert EX02.normalize_equation("0x2 + 5x + 3") == "5x + 3 = 0"
    assert EX02.normalize_equation("x2 + 0x + 3") == "x2 + 3 = 0"
    assert EX02.normalize_equation("x2 + 5x + 0") == "x2 + 5x = 0"


def test_sign_del():
    """Remove + sign in the beginning."""
    assert EX02.normalize_equation("+x2 + 5x + 3") == "x2 + 5x + 3 = 0"
    assert EX02.normalize_equation("+ 5x + 3") == "5x + 3 = 0"
    assert EX02.normalize_equation("+ 3") == "3 = 0"
