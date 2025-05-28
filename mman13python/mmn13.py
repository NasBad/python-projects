"""
    Student Name: Naseem Badran
    Student ID: 322726662

    This is a python code for MMN13
"""

# Q1
def common(lst1, lst2):
    """
    Finds and returns a sorted list of unique elements that are common to two input lists.
    If there are no common elements, returns None.

    Args:
        lst1 (list): The first list of elements.
        lst2 (list): The second list of elements.

    Returns:
        list or None: A sorted list of unique common elements, or None if no common elements exist.
    """
    common_elements = []

    for num in lst1:
        if num in lst2:
            if num not in common_elements:
                common_elements.append(num)

    common_elements.sort()

    if len(common_elements) == 0:
        return None

    return common_elements

# Q2
def find_median(lst, m):
    """
    Calculates the median of a list using the Quickselect algorithm.

    Args:
        lst (list): The list of numbers to find the median of.
        m (int): Placeholder parameter (not used in the implementation).

    Returns:
        int or float: The median value of the list.
    """
    def partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def quickselect(arr, low, high, k):
        if low == high:
            return arr[low]

        pivot_index = partition(arr, low, high)

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quickselect(arr, low, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, high, k)

    n = len(lst)
    median_index = n // 2
    return quickselect(lst, 0, n - 1, median_index)

# Q3
def max_pos_seq(lst):
    """
    Finds the length of the longest contiguous subsequence of positive numbers in a list using recursion.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The length of the longest contiguous subsequence of positive numbers.
    """
    def helper(lst, current_len, max_len):
        if not lst:
            return max_len
        if lst[0] > 0:
            return helper(lst[1:], current_len + 1, max(max_len, current_len + 1))
        else:
            return helper(lst[1:], 0, max_len)

    return helper(lst, 0, 0)

# Q4
def is_palindrome(lst):
    """
    Determines if a list of strings is a palindrome and if each string within the list is also a palindrome.

    Args:
        lst (list): A list of strings to be checked.

    Returns:
        bool: True if the list and each string in it are palindromes; otherwise, False.
    """
    def is_string_palindrome(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and is_string_palindrome(s[1:-1])

    if len(lst) <= 1:
        return True

    return lst[0] == lst[-1] and is_string_palindrome(lst[0]) and is_string_palindrome(lst[-1]) and is_palindrome(
        lst[1:-1])
