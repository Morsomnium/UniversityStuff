"""Test for EX02."""
import EX02


def test_already_correct():
    """Test already correct/normalized input."""
    assert EX02.normalize_equation("3x2 + 2x + 1 = 0") == "3x2 + 2x + 1 = 0"


def test_missing_linear_component():
    """Test the case when the linear component is missing."""
    assert EX02.normalize_equation("3x2 + 5 = 0") == "3x2 + 5 = 0"


def test_space():
    """Check for whitespace."""
    assert EX02.normalize_equation('4x2+11x-4=0') == '4x2 + 11x - 4 = 0'


def test_neg_sq():
    """Check for negative value."""
    assert EX02.normalize_equation('-x2 + 5x + 3 = 0') == 'x2 - 5x - 3 = 0'


def test_neg_lin():
    """Check for negative value."""
    assert EX02.normalize_equation('-5x + 3 = 0') == '5x - 3 = 0'


def test_neg_f():
    """Check for negative value."""
    assert EX02.normalize_equation('-3 = 0') == '3 = 0'


def test_one_mult_sq():
    """Clear 1 multiplier."""
    assert EX02.normalize_equation("1x2 + 5x + 3") == "x2 + 5x + 3 = 0"


def test_one_mult_lin():
    """Clear 1 multiplier."""
    assert EX02.normalize_equation("1x + 3") == "x + 3 = 0"


def test_one_mult_f():
    """Clear 1 multiplier."""
    assert EX02.normalize_equation("13") == "13 = 0"


def test_zero_mult_sq():
    """Clear 0 multiplier."""
    assert EX02.normalize_equation("0x2 + 5x + 3") == "5x + 3 = 0"


def test_zero_mult_lin():
    """Clear 0 multiplier."""
    assert EX02.normalize_equation("x2 + 0x + 3") == "x2 + 3 = 0"


def test_zero_mult_f():
    """Clear 0 multiplier."""
    assert EX02.normalize_equation("x2 + 5x + 0") == "x2 + 5x = 0"


def test_sign_del_sq():
    """Remove + sign in the beginning."""
    assert EX02.normalize_equation("+x2 + 5x + 3") == "x2 + 5x + 3 = 0"


def test_sign_del_lin():
    """Remove + sign in the beginning."""
    assert EX02.normalize_equation("+ 5x + 3") == "5x + 3 = 0"


def test_sign_del_f():
    """Remove + sign in the beginning."""
    assert EX02.normalize_equation("+ 3") == "3 = 0"


def test_side_swap():
    """Check for side swap case."""
    assert EX02.normalize_equation('0 = x2 - 3x - 4') == 'x2 - 3x - 4 = 0'


def test_right_zero():
    """Test for right-sided 0x2."""
    assert EX02.normalize_equation('0 = 0x2 + 4x + 1') == '4x + 1 = 0'


def test_plus_1x2_r():
    """Test +1x2 right."""
    assert EX02.normalize_equation('0 = +1x2 - 3 +4x') == 'x2 + 4x - 3 = 0'


def test_min_1x2_r():
    """Test -1x2 right."""
    assert EX02.normalize_equation('0 = -1x2 - 3 +4x') == 'x2 - 4x + 3 = 0'


def test_x_1():
    """Text."""
    assert EX02.normalize_equation('x1 - 3 + 4x2 = 0') == '4x2 + x - 3 = 0'
