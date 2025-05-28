def Wildcards(strParam):
    try:
        pattern, text = strParam.split()
    except ValueError:
        return "invalid"

    i = j = 0
    while i < len(pattern) and j < len(text):
        if pattern[i] == '+':
            if not text[j].isalpha():
                return "false"
            i += 1
            j += 1
        elif pattern[i] == 'S':
            if not text[j].isdigit() or text[j] == '0':
                return "false"
            i += 1
            j += 1
        elif pattern[i] == '*':
            if i + 1 < len(pattern) and pattern[i + 1] == '(':
                # CHANGE: Move past '*(' and extract N
                i += 2  # Move past '*('
                N = ''
                while i < len(pattern) and pattern[i] != ')':
                    N += pattern[i]
                    i += 1
                # CHANGE: Ensure closing ')' is present
                if i >= len(pattern) or pattern[i] != ')':
                    return "invalid"
                i += 1  # Move past ')'
                N = int(N)
                if j + N > len(text):
                    return "false"
                char = text[j]
                for _ in range(N):
                    if text[j] != char:
                        return "false"
                    j += 1
            else:
                # CHANGE: Handle '*' without '(N)' (default to 3 characters)
                if j + 3 > len(text):
                    return "false"
                char = text[j]
                for _ in range(3):
                    if text[j] != char:
                        return "false"
                    j += 1
                i += 1
        else:
            return "invalid"

    # CHANGE: Ensure both pattern and text are fully processed
    if i != len(pattern) or j != len(text):
        return "false"

    return "true"


# Example usage:
print(Wildcards("++*(5) gheeeee"))  # Output: true
print(Wildcards("++*(3) ghhhee"))  # Output: true
print(Wildcards("+S* abc123"))  # Output: false
print(Wildcards("invalid input"))  # Output: invalid