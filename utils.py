
def cmp(x: int, y: int) -> int:
    if x != y:
        if x < y:
            return -1
        return 1
    return 0
