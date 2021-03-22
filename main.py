# Name Derek J. Russell
# Course: Uber Career Prep
# HW Assignment 1: Arrays & Strings (Part 2)
# Date March 21st, 2021

# Time Complexity: O(n^2)

def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    """
     Implement the function pairsThatEqualSum() that takes an array of
     integers and a target integer and returns an array of pairs (i.e.,
     an array of tuples) where each pair contains two numbers from the
     input array and the sum of each pair equals the target integer.
    """
    """
     The 1st for-loop loops for each index of inputArray. The 2nd for-loop 
     loops for index from i+1 to end of inputArray. Next, it checks the sum 
     of elements at indexes (k, j) matches the sum. After that, it adds the 
     values at indexes k and j to answer. Lastly, it returns the answer. 
    """
    answer = []

    for k in range(len(inputArray)):
        for j in range(k + 1, len(inputArray)):
            if inputArray[k] + inputArray[j] == targetSum:
                answer.append((inputArray[k], inputArray[j]))
    return answer


# Driver Code - (Testing).
print(pairsThatEqualSum([1, 2, 3, 4, 5], 5))
print(pairsThatEqualSum([1, 2, 3, 4, 5], 1))
print(pairsThatEqualSum([1, 2, 3, 4, 5], 7))
