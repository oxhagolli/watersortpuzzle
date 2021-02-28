
class Vial:
    def __init__(self, water=[]):
        self.water = water
    def __repr__(self):
        return str(self.water)
    def __eq__(self, o: object):
        return str(self.water) == str(o.water)
    def __str__(self):
        return str(self.water)
    def size(self):
        return len(self.water)

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == 4

    def is_complete(self):
        return self.is_empty() or (self.is_full() and len(set(self.water)) == 1)
    
    def drop(self, to):
        el = self.top()
        while self.top() == el and to.size() < 4:
            self.water.pop(0)
            to.water.insert(0, el)

    def top(self):
        if not self.is_empty():
            return self.water[0]
        else:
            return 0

    def top_depth(self):
        el = self.top()
        counter = 1
        while counter < self.size() and el == self.water[counter]:
            counter += 1
        return counter
    
    def can_move(self, to):
        if not self.is_empty():
            if to.is_empty():
                return True
            elif self.top_depth() > 4 - to.size():
                return False
            elif not to.is_full() and to.top() == self.top():
                return True
        return False


def start_state():
    return [
        Vial([1, 2, 3, 4]),
        Vial([5, 6, 1, 7]),
        Vial([8, 4, 6, 9]),
        Vial([9, 5, 7, 9]),
        Vial([10, 2, 9, 1]),
        Vial([3, 11, 8, 12]),
        Vial([4, 12, 11, 5]),
        Vial([1, 6, 4, 5]),
        Vial([11, 3, 11, 12]),
        Vial([6, 8, 7, 10]),
        Vial([12, 2, 7, 10]),
        Vial([2, 8, 10, 3]),
        Vial(),
        Vial()
    ]

def test():
    return [Vial([3, 3, 3, 4]), Vial([5, 6, 1, 7]), Vial([4, 4, 6, 9]), Vial([9, 5, 7, 9]), Vial([9, 1]), Vial([8, 8, 8, 12]), Vial([12, 12, 11, 5]), Vial([6, 6, 4, 5]), Vial([11, 11, 11, 12]), Vial([10, 10]), Vial([7, 7, 10]), Vial([2, 8, 10, 3]), Vial([1, 1]), Vial([2, 2, 2])]

def test2():
    return [Vial([1, 2, 1, 2]), Vial([2, 1, 2, 1]), Vial()]


state = test2()

def copystate(state):
    res = []
    for i in state:
        res.append(Vial(i.water[:]))
    return res

def copypath(path):
    res = []
    for i in path:
        res.append(i[:])
    return res


def draw(state):

    # O, LG, C, B, LP, G, P, R, Y, LB, BR, GR
    d = {
        1: "#FF930F",
        2: "#63FF0F",
        3: "#0FFFF7",
        4: "#1C0FFF",
        5: "#FF0FF5",
        6: "#188126",
        7: "#551881",
        8: "#F8E612",
        9: "#F0001A",
        10: "#45A3E8",
        11: "#9C3F26",
        12: "#A6A6A6",
    }

    with Image.new("RGB", (900, 250)) as img:
        for i, vile in enumerate(state):
            for j, box in enumerate(vile.water[::-1]):
                x = 50 + 50 * i + 5 * i
                y = 250 - j * 50
                dr = ImageDraw.Draw(img)
                dr.rectangle([(x, y), (x+50, y-50)], fill=d[box])
        img.show()
    time.sleep(1)


def is_solved(state):
    for vial in state:
        if not vial.is_complete():
            return False
    return True

def backtrack(state, path=[]):
    # Check success
    if is_solved(state):
        return True, path

    # Enumerate possibilties
    possibilities = []
    for i, item in enumerate(state):
        for j, other in enumerate(state):
            if i == j or [j, i, state] in path:
                continue
            if item.can_move(other):
                cstate = copystate(state)
                cstate[i].drop(cstate[j])
                cpath = copypath(path)
                cpath.append([i, j, cstate])
                possibilities.append(cpath)
    for poss in possibilities:
        res = backtrack(poss[-1][2], poss)
        if res[0]:
            return res
    return False, []


print(backtrack(start_state()))