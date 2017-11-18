def new(num_buckets=256):
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap, key):
    return hash(key) % len(aMap)

def get_bucket(aMap, key):
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]

def get_slot(aMap, key, default=None):
    bucket = get_bucket(aMap, key)
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v  
    return -1, key, default

def get(aMap, key, default=None):
    i, k, v = get_slot(aMap, key, default=default)
    return v

def set2(aMap, key, value):
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)
    if i>=0:
        bucket[i] = (key, value)
    else:
        bucket.append((key, value))

def delete(aMap, key):
    bucket = get_bucket(aMap, key)
    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

def list2(aMap):
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k, v

if __name__ == "__main__":
    states = new()
    set2(states, 'Oregon', 'OR')
    set2(states, 'Florida', 'FL')
    set2(states, 'California', 'CA')
    set2(states, 'New York', 'NY')
    set2(states, 'Michigan', 'MI')

    # create a basic set of states and some cities in them
    cities = new()
    set2(cities, 'CA', 'San Francisco')
    set2(cities, 'MI', 'Detroit')
    set2(cities, 'FL', 'Jacksonville')

    # add some more cities
    set2(cities, 'NY', 'New York')
    set2(cities, 'OR', 'Portland')


    # print out some cities
    print '-' * 10
    print "NY State has: %s" % get(cities, 'NY')
    print "OR State has: %s" % get(cities, 'OR')

    # print some states
    print '-' * 10
    print "Michigan's abbreviation is: %s" % get(states, 'Michigan')
    print "Florida's abbreviation is: %s" % get(states, 'Florida')

    # do it by using the state then cities dict
    print '-' * 10
    print "Michigan has: %s" % get(cities, get(states, 'Michigan'))
    print "Florida has: %s" % get(cities, get(states, 'Florida'))

    # print every state abbreviation
    print '-' * 10
    list2(states)

    # print every city in state
    print '-' * 10
    list2(cities)

    print '-' * 10
    state = get(states, 'Texas')

    if not state:
        print "Sorry, no Texas."

    # default values using ||= with the nil result
    # can you do this on one line?
    city = get(cities, 'TX', 'Does Not Exist')
    print "The city for the state 'TX' is: %s" % city