#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # insert(hash_table, key, value)
    # input: weights = [ 1, 2, 3 ], length = 3, limit = 4
    for index in range(0, length):
        hash_table_insert(ht, weights[index], index)

    # It's hashed to places 5th, 7th, 8th and answer should return (2, 0)
    # Each linked pair has a key of its weight and the value is the
    # index of where it was in the original array
    # print("Weight", ht.storage[5].key, ",", "Index", ht.storage[5].value)
    # print("Weight", ht.storage[7].key, ",", "Index", ht.storage[7].value)
    # print("Weight", ht.storage[8].key, ",", "Index", ht.storage[8].value)

    # hash_table_retrieve(hash_table, key)
    print(hash_table_retrieve(ht, 1))

    for index in range(0, length):
        first = 0
        second = 0
        # searching for keys with
        # key = limit-individual weights in the weights array
        retrieved = hash_table_retrieve(ht, (limit - weights[index]))
        print(retrieved)
        # retrieved returns the correct value index for the two values (2,3)
        if retrieved is not None:
            print("Retrieved", retrieved)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


get_indices_of_item_weights([10, 12, 14, 15, 16], 5, 29)
