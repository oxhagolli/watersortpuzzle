
class Glass:
    def __init__(self, colors=[]):
        self.colors = colors
        self.size = len(colors)

    def peek(self):
        if self.is_empty():
            return None
        return self.colors[0]

    def can_move(self, to):
        if (self.is_single() and to.is_empty()) or self.is_empty() or to.is_full():
            return False
        return to.is_empty() or to.peek() == self.peek()

    def pop(self, to):
        if self.can_move(to):
            if not to.is_full():
                self.size -= 1
                to.add(self.colors.pop(0))
            self.pop(to)

    def add(self, item):
        self.size += 1
        self.colors.insert(0, item)

    def is_single(self):
        return len(set(self.colors)) == 1

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == 4

    def is_complete(self):
        return (self.size == 4 and self.is_single()) or self.size == 0

    def __repr__(self) -> str:
        return str(self.colors)

    def __str__(self) -> str:
        return str(self.colors)


def start_state():
    return [
        Glass([1, 2, 3, 4]),
        Glass([5, 6, 1, 7]),
        Glass([8, 4, 6, 9]),
        Glass([9, 5, 7, 9]),
        Glass([10, 2, 9, 1]),
        Glass([3, 11, 8, 12]),
        Glass([4, 12, 11, 5]),
        Glass([1, 6, 4, 5]),
        Glass([11, 3, 11, 12]),
        Glass([6, 8, 7, 10]),
        Glass([12, 2, 11, 10]),
        Glass([2, 8, 10, 3]),
        Glass(),
        Glass()
    ]

def test():
    return [Glass([1, 1, 1, 1]), Glass()]

def copystate(state):
    res = []
    for i in state:
        res.append(Glass(i.colors))
    return res

def copypath(path):
    res = []
    for i in path:
        res.append(i[:])
    return res


def is_solved(state):
    for vial in state:
        if not vial.is_complete():
            return False
    return True

def backtrack(state, previous=[]):
    if is_solved(state):
        return True, previous
    for i, item in enumerate(state):
        if not item.is_complete():
            all_complete = False
        else:
            continue
        for j, other in enumerate(state):
            if i == j or (len(previous) > 0 and previous[-1] == [j, i]):
                continue
            if item.can_move(other):
                cpy = copystate(state)
                cpy[i].pop(cpy[j])
                prv = copypath(previous)
                prv.append([i, j])
                res = backtrack(cpy, prv)
                if res[0]:
                    return res
                
    if all_complete:
        return True, previous
    return False, previous
        
print(backtrack(test()))
