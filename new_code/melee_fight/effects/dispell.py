

def dispell_after_counterattack(unit):
    for_delete = []
    for i, effect in enumerate(unit.effects):
        if effect.dispell_after_counterattack:
            for_delete.append(i)
    for_delete.sort(reverse=True)
    for x in for_delete:
        del unit.effects[x]
