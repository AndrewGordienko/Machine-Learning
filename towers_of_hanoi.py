n = 3
pillars = 3
towers = []

for i in range(pillars):
    towers.append([])
for i in range(n):
    towers[0].append(i + 1)

tower_dictionary = {
    "first": 0,
    "second": 1,
    "third": 2
}
def tower(n, first, second, third):
    if n == 1:
        print('{0}->{1}'.format(first, third))

        pillar1 = tower_dictionary.get(first)
        pillar2 = tower_dictionary.get(third)

        towers[pillar2].insert(0, towers[pillar1][0])
        del towers[pillar1][0]
        
        print(towers)
        print("")
    else:
        tower(n-1, first, third, second)
        tower(1, first, second, third)
        tower(n-1, second, first, third)

print(towers)
print("")
tower(n, "first", "second", "third")
