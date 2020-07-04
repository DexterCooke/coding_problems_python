def permutations(str):
    if str == '':
        return ['']
    permutes = []
    for char in str:
        subpermutes = permutations(str.replace(char, '', 1))
        for each in subpermutes:
            permutes.append(char + each)

    return permutes

print(permutations('abc'))