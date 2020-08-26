mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

# mcase_frequency == {'a': 17, 'z': 3, 'b': 34}

{v: k for k, v in some_dict.items()}



# set的例子

squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: {1, 4}