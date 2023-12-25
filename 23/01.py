def opposite_сolors(color):
    r, g, b = map(int, color.split())
    return f'{255 - r} {255 - g} {255 - b}'


print(opposite_сolors('244 11 120'))
