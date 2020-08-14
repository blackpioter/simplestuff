#!/usr/local/bin/python3

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


def items(guests):
    allItems = {}
    for guestName, guestItems in guests.items():
        for guestItem in guestItems.keys():
            allItems.setdefault(guestItem, 0)
    return allItems


print('Number of things being brought:')
for item in items(allGuests):
    print('%-3s  %-16s  %-16s' % (' - ', str(item).title(), str(totalBrought(allGuests, item))))
