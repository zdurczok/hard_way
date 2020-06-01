from dllist import DoubleLinkedList # so we can use dllist and it's methods

class Dictionary(object):
    def __init__(self, num_buckets=256): # set number of bucktes to 256 ( 2 ** 8)
        """Initializes a Map with the given number of buckets."""
        self.map = DoubleLinkedList() # self.map is DoubleLinkedList() with it's methods
        for i in range(0, num_buckets):
            self.map.push(DoubleLinkedList()) # now the parent map-dllist contains 256 child dllists

    def hash_key(self, key):
        """Given a key this will create a number and then convert it to
        an index for the aMap's buckets."""
        return hash(key) % self.map.count() # create an index for a key  - try print(states.hash_key('NY')) in test_dictionary.py

    def get_bucket(self, key):
        """Given a key, find the bucket where it would go."""
        bucket_id = self.hash_key(key) # get the index of the bucket we want to access
        return self.map.get(bucket_id) # get the bucket (parent dllist) at the given id (created with hash_key)

    def get_slot(self, key, default=None):
        """
        Returns either the bucket and node for a slot, or None, None
        """
        bucket = self.get_bucket(key) # find a bucket (get the index of a bucket)

        if bucket: # if bucket exists
            node = bucket.begin # set node to the begin of the parent dllist
            i = 0 # what for?

            while node: # traverse the parent dllist
                if key == node.value[0]: # if key equals key stored in a node
                    return bucket, node # return dllist and key-value pair (node)
                else: # if not, go further
                    node = node.next
                    i += 1

        # fall through for both if and while above
        return bucket, None

    def get(self, key, default=None):
        """Gets the value in a bucket for a given key, or the default."""
        bucket, node = self.get_slot(key, default=default) # get the right bucket (parent dllist) and the right node (key-value pair)
        return node and node.value[1] or node # return key-value pair

    def set(self, key, value):
        """Sets the key to the value, replacing any existing value."""
        bucket, slot = self.get_slot(key) # find a bucket and a slot at/inside this bucket

        if slot:
            # the key exists, replace it
            slot.value = (key, value)
        else:
            # the key does not, append to create it
            bucket.push((key, value))

    def delete(self, key):
        """Deletes the given key from the Map."""
        bucket = self.get_bucket(key) # find a bucket (get the index of a bucket)
        node = bucket.begin # we need to go through buckets

        while node: # traverse the parent dllist
            k, v = node.value # key-value pair set to the value of te node, key-value pair of the node
            if key == k: # if key matches node's key
                bucket.detach_node(node) # detach the node from the parent dllist
                break #stop

    def list(self):
        """Prints out what's in the Map."""
        bucket_node = self.map.begin # start at the beginning of the parent dllist
        while bucket_node: # traverse the parent dllist
            slot_node = bucket_node.value.begin # we need to access a child dllist
            while slot_node: # traverse a child dllist
                print(slot_node.value) # prints the key-value pair stored inside a slot, which is a node of a child dllist
                slot_node = slot_node.next # go further inside a child dllist
            bucket_node = bucket_node.next # go further inside the parent dllist
