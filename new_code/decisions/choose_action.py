

def choose_action(active, passive):
    if active.tactic == "berserk":
        move_to, action = berserk(active, passive)
    else:
        move_to, action = dummy(active, passive)
    return move_to, action


def berserk(active, passive):
    ax = active.position[0]
    ay = active.position[1]
    px = passive.position[0]
    py = passive.position[1]
    movement = active.speed
    action = "wait"
    while movement > 0 or (-1 > ax-px > 1 and -1 > ay-py > 1):
        movement -= 1
        if ax-px > 1:
            ax -= 1
            continue
        elif ax-px < -1:
            ax += 1
            continue
        if ay-py > 1:
            ay -= 1
        elif ay-py < -1:
            ay += 1
        elif -1 <= ax-px <= 1 and -1 <= ay-py <= 1:
            action = "strike"
            break
    if -1 <= ax - px <= 1 and -1 <= ay - py <= 1:
        action = "strike"
    return (ax, ay), action


def dummy(active, passive):
    x = active.position[0]
    y = active.position[1]
    action = "wait"
    return (x, y), action
