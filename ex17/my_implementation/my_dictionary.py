from dllist import DoubleLinkedList

class Dictionary(object):
    def __init__(self, num_buckets=256):
        self.map = DoubleLinkedList()
        for x in range(0, num_buckets):
            self.map.push(DoubleLinkedList())

    def hash_key(self, key):
        return hash(key) % self.map.count()

    def get_bucket(self, key):
        bucket_id = self.hash_key(key)
        return self.map.get(bucket_id)

    def get_slot(self, key):
        bucket = self.get_bucket(key)

        if bucket:
            slot = bucket.begin
            while slot:
                if key == slot.value[0]:
                    return bucket, slot
                else:
                    slot = slot.next
        return bucket, None

    def get(self, key, default=None):
        bucket, slot = self.get_slot(key)
        return slot and slot.value[1] or default

    def set(self, key, value):
        bucket, slot = self.get_slot(key)
        if slot:
            slot.value = (key, value)
        else:
            bucket.push((key, value))

    def delete(self, key):
        bucket = self.get_bucket(key)
        slot = bucket.begin

        while slot:
            k, v = slot.value
            if key == k:
                bucket.detach_node(slot)
                break

    def print_list(self):
        bucket_node = self.map.begin
        while bucket_node:
            slot_node = bucket_node.value.begin
            while slot_node:
                print(slot_node.value)
                slot_node = slot_node.next
            bucket_node = bucket_node.next
