

def run_away(running_unit, intimidating_unit, reason_to_run):
    x_running = running_unit.position[0]
    y_running = running_unit.position[1]
    x_scary = intimidating_unit.position[0]
    y_scary = intimidating_unit.position[1]
    movement = running_unit.speed
    action = "wait"
    while movement > 0 and (x_running > 0 or y_running):
        movement -= 1
        if x_running > 0:
            x_running -= 1
            continue
        if y_running > 0:
            y_running -= 1
        else:
            break
    return (x_running, y_running), action
