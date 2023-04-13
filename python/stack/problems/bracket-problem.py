"""
[{}]    - valid
(()())  - valid
{]      - invalid
[()]))()- invalid
"""


def is_bracket_string_valid(bracket_prob):
    bracket_problem = bracket_prob
    bracket_queue = []
    reverse_bracket = {
        "}": "{",
        "]": "[",
        ")": "(",
    }

    for bracket in bracket_problem:
        if bracket in reverse_bracket.values():
            bracket_queue.append(bracket)
        elif len(bracket_queue) == 0  or reverse_bracket[bracket] != bracket_queue[-1]:
            return False
        else:
            bracket_queue.pop()
    return len(bracket_queue) == 0


if __name__ == "__main__":
    r = is_bracket_string_valid("[()]))()")  # returns False
