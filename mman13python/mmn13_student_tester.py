import importlib
MMN = "mmn13"

def run_test (test_name, func_name, *args, expected_return):
    """
    Runs a test for a given function with provided arguments and checks the result.
    Note:
        This tester does not check the time complexity of the answers.
    Parameters:
        test_name (str): Name of the test.
        func_name (str): Name of the function to test.
        *args: Arguments to pass to the function.
        expected_return: The expected return value from the function.

    Returns:
        str: A message indicating the test result.
    """
    try:
        module = importlib.import_module(MMN)
        func = getattr(module, func_name)
        result = func(*args) 
        assert result == expected_return  
        return f'{test_name}: passed \n\targs:{args}, result: {result}'
    except AssertionError as e:
        return f'{test_name}: failed \n\targs:{args}. result: {result} expected result: {expected_return}'
    except ModuleNotFoundError:
        return f'{test_name}: failed \n\t{MMN}.py not found!'
    except AttributeError:
        return f'{test_name}: failed \n\t{func_name} not found in the module!'
    except Exception as e:
        return  f'{test_name}: failed \n\twith error: {type(e).__name__} - {e}, args:{args}.'

print('\n************** mmn 13 **************\n')

print ('****** Question 1 ********\n')
lst1 = [-4, 0, 2, 3, 8, 9]
lst2 = [-4, -2, 1, 3, 5, 10, 12]
lst3 = [1, 4, 5, 10]
lst4 = [1, 2, 9]
lst5 = []


print(run_test("1", "common", lst1, lst2, expected_return=[-4, 3]))
print(run_test("2", "common", lst1, lst3, expected_return=None))
print(run_test("3", "common", lst3, lst2, expected_return=[1, 5, 10]))
print(run_test("4", "common", lst1, lst4, expected_return=[2, 9]))
print(run_test("5", "common", lst1, lst5, expected_return=None))


print ('\n****** Question 2 ********\n')
lst1 = [4, 11, 6, 8, 1, 7, 3]
lst2 = [3, 1, 5, 10,2, 12, 4]
lst3 = [3, 0, 5]
lst4 = [0]
print(run_test("1", "find_median", lst1, 11, expected_return=6))
print(run_test("2", "find_median", lst2, 20, expected_return=4))
print(run_test("3", "find_median", lst3, 5, expected_return=3))
print(run_test("4", "find_median", lst4, 0, expected_return=0))




print ('\n****** Question 3 ********\n')
lst1 = [2, -1, 1, 3, 2, -4, -2, 4, 6, 1, 2]
lst2 = [-2,-1,-4,-3]
lst3 = [-2,1,-4,-3]
lst4 = []
lst5 = [4,3]
lst6 = [2,-1,-4,3]

print(run_test("1", "max_pos_seq", lst1, expected_return=4))
print(run_test("2", "max_pos_seq", lst2, expected_return=0))
print(run_test("3", "max_pos_seq", lst3, expected_return=1))
print(run_test("4", "max_pos_seq", lst4, expected_return=0))
print(run_test("5", "max_pos_seq", lst5, expected_return=2))
print(run_test("6", "max_pos_seq", lst6, expected_return=1))


print ('\n****** Question 4 ********\n')

lst1 = ["abba", "readaer", "abba"] 
lst2 = ["abba"] 
lst3 = ["a", "aca", "aca", "a"]
lst4 = ["a", "ac1", "ac1a", "a"]
lst5 = ["a", "ac1a", "ac1a", "a", "bb"]
lst6 = ["a","","a"]
lst7 = []

print(run_test("1", "is_palindrome", lst1, expected_return=True))
print(run_test("2", "is_palindrome", lst2, expected_return=True))
print(run_test("3", "is_palindrome", lst3, expected_return=True))
print(run_test("4", "is_palindrome", lst4, expected_return=False))
print(run_test("5", "is_palindrome", lst5, expected_return=False))
print(run_test("6", "is_palindrome", lst6, expected_return=True))
print(run_test("7", "is_palindrome", lst7, expected_return=True))