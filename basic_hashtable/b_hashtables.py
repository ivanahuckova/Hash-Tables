

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# '''
class BasicHashTable:
    def __init__(self, capacity):
        # max length of hash table
        self.capacity = capacity
        # underlying data sructure
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF


# '''
# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    position = hash(key) % hash_table.capacity
    if hash_table.storage[position]:
        print("WARNING: key " + key +
              " is already in the hash table and will be overwritten")
    hash_table.storage[position] = Pair(key, value)

# '''
# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
    position = hash(key) % hash_table.capacity
    if hash_table.storage[position]:
        hash_table.storage[position] = None
    else:
        print("WARNING: key " + key +
              " is not in the hashtable and therefore couldn't be removed")
        return None


# '''
# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
