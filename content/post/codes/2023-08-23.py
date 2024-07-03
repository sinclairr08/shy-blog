# case 1
v1 = 3
l1 = [v1]
l1[0] += 1
print(v1)

# case 2
v2 = "3"
l2 = [v2]
l2[0] += "1"
print(v2)


# case 3
class val:
    def __init__(self, i) -> None:
        self.i = i

v3 = val(3)
l3 = [v3]
l3[0].i += 1
print(v3.i)

# case 4
v4 = [3]
l4 = [v4]
l4[0].append(1)
print(v4)
