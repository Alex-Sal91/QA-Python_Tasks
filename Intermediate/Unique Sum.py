# Given 3 integer values, return their sum.
# If one value is the same as another value, they do not count towards the sum.
# Aka only return the sum of unique numbers given.

def unique_sum(n1, n2, n3):
    if n1 == n2 and n1 == n3:
        return 0
    elif n1 == n2:
        return n1 * n3
    elif n2 == n3:
        return n1 * n2
    elif n3 == n1:
        return n2 * n3
    else:
        return n1*n2*n3

print(unique_sum(5,7,4))