"""Recursion."""


def staircase_combinations(n, temp_dict={0:1, 1:1, 2:2}):
    """Recursion."""
    if n in temp_dict:
        return temp_dict[n]
    else:
        temp_dict[n] = staircase_combinations(n-1, temp_dict) + staircase_combinations(n-2, temp_dict) + staircase_combinations(n-3, temp_dict)
        return staircase_combinations(n-1, temp_dict) + staircase_combinations(n-2, temp_dict) + staircase_combinations(n-3, temp_dict)

