

def letter(unit):
    if unit.color != "Бесцветный":
        return unit.color[0]
    else:
        return "*"


def get_grid(unit1, unit2):
    grid = []
    for x in range(10):
        grid.append("."*12)
    for num, pos in {letter(unit1): unit1.position,
                     letter(unit2): unit2.position}.items():
        x = pos[0]
        y = pos[1]
        grid[x] = f"{grid[x][:y]}{num}{grid[x][y+1:]}"

    wide_grid = []
    for row in grid:
        new_row = ""
        for x in row:
            new_row += f" {x} "
        wide_grid.append(new_row)

    return wide_grid
