import EX02


def test_already_correct():
    """Test already correct/normalized input."""
    assert EX02.normalize_equation("3x2 + 2x + 1 = 0") == "3x2 + 2x + 1 = 0"


def test_missing_linear_component():
    """Test the case when the linear component is missing."""
    assert EX02.normalize_equation("3x2 + 5 = 0") == "3x2 + 5 = 0"


def test_negative():
    """Check first negative value"""
    assert EX02.normalize_equation('-x2 + 5x + 3 = 0') == 'x2 - 5x - 3 = 0'
    assert EX02.normalize_equation('-5x + 3 = 0') == '5x - 3 = 0'
    assert EX02.normalize_equation('-3 = 0') == '3 = 0'
