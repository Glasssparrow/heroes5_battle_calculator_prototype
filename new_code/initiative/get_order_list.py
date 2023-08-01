

def get_order_list(unit1, unit2):
    for unit in [unit1, unit2]:
        if unit.initiative_position < 0:
            unit.initiative_position = 0

    fast_unit, slow_unit = unit1, unit2
    if fast_unit.initiative < slow_unit.initiative:
        fast_unit, slow_unit = slow_unit, fast_unit
    # Вычисляем "время" через которое юниты получат ход
    time_fast = (1-fast_unit.initiative_position)/fast_unit.initiative
    time_slow = (1-slow_unit.initiative_position)/slow_unit.initiative
    if time_fast < time_slow:
        turn_of_the_fast_unit = True
        time_until_turn = time_fast
    else:
        turn_of_the_fast_unit = False
        time_until_turn = time_slow
    # Вычисляем время прохождения полного круга
    step_fast = 1 / fast_unit.initiative
    step_slow = 1 / slow_unit.initiative

    order = {
        time_fast: fast_unit.color,
        time_slow: slow_unit.color
    }
    for x in range(5):
        order[time_fast+x*step_fast] = fast_unit.color
        order[time_slow+x*step_slow] = slow_unit.color
    sorted_items = sorted(order.items(), reverse=True)
    while (len(sorted_items) > 4 and
           sorted_items[0][1] == sorted_items[1][1] == slow_unit.color):
        del order[sorted_items[0][0]]
        del sorted_items[0]

    result = []
    for v in sorted_items:
        result.append(v[1])

    if turn_of_the_fast_unit:
        fast_unit.initiative_position = 0
        slow_unit.initiative_position += time_until_turn * slow_unit.initiative
    else:
        slow_unit.initiative_position = 0
        fast_unit.initiative_position += time_until_turn * fast_unit.initiative

    return result


def get_unit_types_for_order_list(order_list, unit1, unit2):
    unit_types = []
    for color in order_list:
        if color == unit1.color:
            unit_types.append(unit1.name)
        else:
            unit_types.append(unit2.name)
    return unit_types
