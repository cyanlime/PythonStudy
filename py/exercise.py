# def get_slot(aMap, key, default=None):
 

#     for i, kv in enumerate(aMap):
#         k, v = kv
#         if key == k:
#             return i, k, v
#     return -1, k, default

# if __name__ == '__main__':
#     a = [{"NY": "New York"}, {"FL": "florida"}, {"WashingtonDC": "WDC"}]
#     #dic = get_slot([{"NY": "New York"}, {"FL": "florida"}, {"WashingtonDC": "WDC"}], 4)
#     num = get_slot([a[0], a[1], a[2]], 1)

array = [('a', 1), ('b', 2), ('c', 3)]


for i, kv in enumerate(array):
    print kv

e = list(enumerate(array))

#kv = (0, 'a')
(k, v) = kv
print 'k is %s and v is %s' % (k, v)

hash(123)