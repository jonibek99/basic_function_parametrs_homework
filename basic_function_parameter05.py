# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.
def count_vowels(a):
    c=0
    for i in a:
        if i in ('a, e, i, o, u, A, E, I, O, U'):
            c+=1
    return c
f=str(input())
print(count_vowels(f))
