# Name: Derek J. Russell
# Course: Uber Career Prep
# HW Assignment 1: Arrays & Strings (Part 2)
# Date: March 21st, 2021


def isStringPermutation(s1: str, s2: str) -> bool:
    """
    Implement the function isStringPermutation() that takes two Strings
    as parameters and returns a Boolean denoting whether the first
    string is a permutation of the second string.
    """

    """
    Get lengths of both strings. If the length of both strings
    is not the same, then they cannot be Permutation.
    """
    if len(s1) != len(s2):
        return False

    # Sort both strings.
    temp1 = sorted(s1)
    s1 = " ".join(temp1)
    temp2 = sorted(s2)
    s2 = " ".join(temp2)

    # Compare the sorted strings.
    for j in range(0, len(s1), 1):
        if s1[j] != s2[j]:
            return False
    return True


# Driver Code
if __name__ == '__main__':
    s1, s2 = "asdf", "fsda"
    s3, s4 = "asdf", "fsa"
    s5, s6 = "asdf", "fsax"

    if isStringPermutation(s1, s2):
        print("True")
    else:
        print("False")

    if isStringPermutation(s3, s4):
        print("True")
    else:
        print("False")

    if isStringPermutation(s5, s6):
        print("True")
    else:
        print("False")