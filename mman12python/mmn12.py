"""
    Student Name: Naseem Badran
    Student ID: 322726662

    This is a python code for MMN12
"""

def biggest_sum(inner_arr):
    """
        Calculates the largest sum of consecutive positive integers in the given array,
        resetting the sum to 0 whenever a zero is encountered.

        Parameters:
            inner_arr (list of int): A list of positive integers. All elements must be non-negative.

        Returns:
            int: The maximum sum of consecutive positive integers before a zero resets the summation.

        Raises:
            TypeError: If any element in the array is not a positive integer.
    """
    num_sum = 0
    num_max = 0
    arr_len=len(inner_arr)
    if not all(isinstance(x, int) and x > -1 for x in inner_arr):
        raise TypeError("All elements in the array must be positive integers")
    for i in range(0,arr_len,1):
        num_sum = num_sum + inner_arr[i]
        num_max = max(num_sum, num_max)
        if inner_arr[i]==0:
            num_sum=0

    return num_max


def biggest_sum_row(mat):
    """
        Finds the index of the row in a 2D matrix that has the largest sum
        of consecutive positive integers, using the `biggest_sum` function
        to calculate the sum for each row. If an error occurs, returns -1.

        Parameters:
            mat (list of list of int): A 2D list (matrix) where each row is
            a list of integers.

        Returns:
            int: The index of the row with the largest sum of consecutive
            positive integers. Returns -1 if an error occurs.
    """
    try:
        max_sum = -1
        row_index = -1

        for i, row in enumerate(mat):
            row_sum = biggest_sum(row)

            if row_sum > max_sum:
                max_sum = row_sum
                row_index = i

        return row_index
    except Exception:
        return -1


def shift_k_right(l1, k):
    """
        Shifts the elements of a list `k` positions to the right. The last `k` elements
        are moved to the front of the list.

        Parameters:
            l1 (list): The list to be shifted.
            k (int): The number of positions to shift the list to the right.
                     Must be a non-negative integer less than the length of the list.

        Returns:
            list: The list after shifting elements `k` positions to the right.

        Raises:
            IndexError:
                - If the list is empty.
                - If `k` is negative.
                - If `k` is greater than or equal to the length of the list.
    """
    if not l1:
        raise IndexError("Cannot shift an empty list")

    if k < 0:
        raise IndexError("k cannot be negative")

    if k >= len(l1):
        raise IndexError("k cannot be greater than or equal to the length of the list")

    if k == 0:
        return l1

    for _ in range(k):
        last_element = l1[-1]
        for i in range(len(l1) - 1, 0, -1):
            l1[i] = l1[i - 1]
        l1[0] = last_element

    return l1


def shift_right_size(arr1, arr2):
    """
        Determines the number of right shifts required to make `arr1` equal to `arr2`.
        If no such shift exists, returns `None`. If both arrays are empty, returns `0`.

        Parameters:
            arr1 (list): The first list to be compared.
            arr2 (list): The second list to match after right shifts.

        Returns:
            int: The number of right shifts required to make `arr1` equal to `arr2`.
            None: If no amount of shifting can make `arr1` equal to `arr2`, or if
                  the lengths of the arrays are different.
        """
    if len(arr1) == 0 and len(arr2) == 0:
        return 0

    if len(arr1) != len(arr2):
        return None

    for shift in range(len(arr1)):
        match = True
        for i in range(len(arr1)):
            if arr1[(i + shift) % len(arr1)] != arr2[i]:
                match = False
                break
        if match:
            return shift

    return None


def is_perfect(lst):
    """
        Determines if a list is "perfect." A list is considered perfect if:
        1. It contains no negative numbers.
        2. It is a permutation of integers from 0 to n-1.
        3. It forms a single cycle when interpreted as indices pointing to the next element.

        Parameters:
            lst (list of int): The input list to check.

        Returns:
            bool:
                - `True` if the list is perfect.
                - `False` if the list is not a permutation of 0 to n-1 or does not form a single cycle.

        Raises:
            IndexError: If the list contains negative numbers.
    """
    if not lst:
        return True

    n = len(lst)

    if any(num < 0 for num in lst):
        raise IndexError("Negative number found in array.")

    if sorted(lst) != list(range(n)):
        return False

    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            count += 1
            j = i
            while not visited[j]:
                visited[j] = True
                j = lst[j]

    return count == 1

def mirror_list(mat):
    """
        Checks if a 2D matrix is "mirrored," meaning each row in the matrix reads the
        same forward and backward (palindromic rows). Additionally, the matrix should
        only contain single-letter characters.

        Parameters:
            mat (list of list of str): A 2D list where each sublist represents a row
            in the matrix.

        Returns:
            bool:
                - `True` if all rows in the matrix are mirrored and contain only single-letter characters.
                - `False` if any row is not mirrored.

        Raises:
            TypeError: If the matrix contains non-string elements.
            ValueError: If the matrix contains elements that are not single-letter alphabetical characters.
    """
    if not mat:
        return True

    for row in mat:
        for item in row:
            if not isinstance(item, str):
                raise TypeError("Matrix should only contain single letter characters.")
            if len(item) != 1 or not item.isalpha():
                raise ValueError("Matrix should only contain single letter characters.")

        n = len(row)
        for i in range(n // 2):
            if row[i] != row[n - i - 1]:
                return False

    return True

# Tests for biggest_sum
assert biggest_sum([0, 1, 2, 0, 3, 0]) == 3
assert biggest_sum([0, 5, 0, 10, 0, 15, 0]) == 15
assert biggest_sum([0, 0, 0]) == 0
assert biggest_sum([0, 10, 20, 0]) == 30
assert biggest_sum([0, 1, 2, 3, 4, 0]) == 10
assert biggest_sum([0, 1, 0, 2, 0, 3, 0]) == 3
assert biggest_sum([0, 1, 2, 3, 4, 5, 0]) == 15
assert biggest_sum([0, 0, 0, 0]) == 0
try:
    biggest_sum([0, -1, 0])
    assert False, "Should raise TypeError"
except TypeError:
    pass
try:
    biggest_sum([0, "a", 0])
    assert False, "Should raise TypeError"
except TypeError:
    pass

# Tests for biggest_sum_row
assert biggest_sum_row([[0, 1, 0], [0, 5, 0]]) == 1
assert biggest_sum_row([[0, 1, 0], [0, 2, 3, 0], [0, 1, 0]]) == 1
assert biggest_sum_row([[0, 1, 2, 0], [0, 10, 0], [0, 3, 4, 0]]) == 1
assert biggest_sum_row([[0, 0], [0, 1, 0]]) == 1
assert biggest_sum_row([[0, 1, 2, 0], [0, "a", 0], [0, 3, 0]]) == -1
assert biggest_sum_row([[0, 1, 2, 0], [], [0, 3, 0]]) == 0
assert biggest_sum_row([[0, 1, 2, 3, 4, 0], [0, 5, 0], [0, 3, 0]]) == 0
assert biggest_sum_row([[0, 1, 0], [0, 2, 0], [0, 3, 0]]) == 2
assert biggest_sum_row([[0, 1, 2, 0], [0, 3, 0]]) == 0

# Tests for shift_k_right
assert shift_k_right([1, 2, 3, 4, 5], 1) == [5, 1, 2, 3, 4]
assert shift_k_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
assert shift_k_right([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
assert shift_k_right([1, 2, 3, 4, 5], 4) == [2, 3, 4, 5, 1]
assert shift_k_right([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
try:
    shift_k_right([1, 2, 3], -1)
    assert False, "Should raise IndexError"
except IndexError:
    pass
try:
    shift_k_right([1, 2, 3], 3)
    assert False, "Should raise IndexError"
except IndexError:
    pass
assert shift_k_right([1], 0) == [1]
try:
    shift_k_right([], 1)
    assert False, "Should raise IndexError"
except IndexError:
    pass
assert shift_k_right([1, 2, 3], 2) == [2, 3, 1]

# Tests for shift_right_size
assert shift_right_size([1, 2, 3, 4], [4, 1, 2, 3]) == 3
assert shift_right_size([1, 2, 3, 4], [3, 4, 1, 2]) == 2
assert shift_right_size([1, 2, 3, 4], [2, 3, 4, 1]) == 1
assert shift_right_size([1, 2, 3, 4], [1, 2, 3, 4]) == 0
assert shift_right_size([1, 2, 3], [3, 1, 2]) == 2
assert shift_right_size([1, 2, 3], [1, 3, 2]) is None
assert shift_right_size([1, 2, 3, 4], [4, 3, 2, 1]) is None
assert shift_right_size([], []) == 0
assert shift_right_size([1], [1]) == 0
assert shift_right_size([1], [2]) is None

# Tests for is_perfect
assert is_perfect([2, 0, 3, 4, 1]) == True
assert is_perfect([3, 0, 1, 4, 2]) == True
assert is_perfect([3, 4, 1, 5, 6, 0, 2]) == False
assert is_perfect([]) == True
assert is_perfect([0]) == True
assert is_perfect([1, 0]) == True
try:
    is_perfect([1, -1, 0])
    assert False, "Should raise IndexError"
except IndexError:
    pass
assert is_perfect([2, 3, 1, 4, 2]) == False
assert is_perfect([0, 1, 2, 0]) == False


# Tests for mirror_list
assert mirror_list([["a", "b", "a"], ["b", "c", "b"], ["a", "b", "a"]]) == True
assert mirror_list([["a", "b", "c"], ["d", "e", "d"], ["c", "b", "a"]]) == False
assert mirror_list([["a", "b", "a"], ["b", "x", "b"], ["a", "b", "y"]]) == False
assert mirror_list([["a", "a"], ["a", "a"]]) == True
assert mirror_list([["a"]]) == True
assert mirror_list([]) == True
try:
    mirror_list([["a", 1], ["b", "a"]])
    assert False, "Should raise TypeError"
except TypeError:
    pass
try:
    mirror_list([["ab", "c"], ["d", "e"]])
    assert False, "Should raise ValueError"
except ValueError:
    pass
assert mirror_list([["a", "b", "a"], ["b", "c", "b"], ["a", "b", "a"]]) == True
assert mirror_list([["x", "y", "x"], ["y", "z", "y"], ["x", "y", "x"]]) == True
