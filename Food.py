class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return self.name + ': <' +srt(self.value)\
                + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    """names, values. calories list of same lenghtself.
        name a list of strings
        values and calories lists of numbers
        returns list of Foods """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i],values[i],calories[i]))
    return menu

def greedy(items maxCost, keyFunction):
    """Assume items a list, maxCost >= 0,
        keyFunction maps element of tiems to numbers"""
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

        return (result, totalValue)

def testGreedy(items, constrainst, keyFunction):
    taken, val = greedy(items, constrainst, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ',item)

def testGreedy(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods,maxUnits, Food.density)

names_list = []
for i in range(0,10)
    name = strings(input('Please enter a food name: '))
    names_list.append(name)
