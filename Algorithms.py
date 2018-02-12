# SmallestNumber = []
# x = 12

# while False:
#     for i in range(1, x):
#         if x % i == 0:
#             SmallestNumber.append[x]
#             print SmallestNumber
#         # elif:
#         #     x += 1
            
#         # break

x = 99
beer = 'beer'

while True:
    for i in range(0, x, -1):
        x += 1
        if i % 7 == 0:
            beer == 'Miller'
        elif i % 5 == 0:
            beer == 'Lite beer'
        elif i % 7 == 0 and i % 5 == 0:
            beer == 'Miller Lite'
    print '%s Bottles of %s, take one down, pass it around, %s bottles of %s on the wall' % (x, beer, x-1, beer)
