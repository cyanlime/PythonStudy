import hashmap

if __name__ == "__main__":
    amap = hashmap.new()
    print amap
    num = hashmap.hash_key(amap, 3)
    print num
    value = hashmap.get_bucket(amap, 3)
    print value

    print hashmap.get_slot(amap, 3)