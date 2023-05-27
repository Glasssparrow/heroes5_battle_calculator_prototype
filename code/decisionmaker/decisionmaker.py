from code.common import sign


def choose_tactics(unit1, unit2):
    unit1.tactic = "berserk"
    unit2.tactic = "berserk"


class Command:

    def __init__(self, move, action):
        self.move = move
        self.action = action


def decision_maker(active, passive):

    if active.tactic == "berserk":
        command = berserk(active, passive)
    else:
        command = Command(0, "wait")
    return command


def berserk(active, passive):
    if abs(passive.position - active.position) > active.speed + 1:
        command = Command(
            sign(passive.position - active.position)*active.speed,
            "wait")
    else:
        command = Command(
            sign(passive.position - active.position) *
            (abs(passive.position - active.position)-1),
            "melee_attack")
    return command
