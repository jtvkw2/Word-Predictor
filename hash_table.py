class HashTable:
    """

    """

    def __init__(self, size=11):
        """

        """
        self.size = size
        self.slots = [None] * self.size

    def put(self, item):
        """
        Place an item in the hash table.
        Return slot number if successful, -1 otherwise (no available slots, table is full)
        """
        hash_value = self.hash_function(item)
        slot_placed = -1
        if self.slots[hash_value] is None or self.slots[hash_value] == item:  # empty slot or slot contains item already
            self.slots[hash_value] = item
            slot_placed = hash_value
        else:
            next_slot = self.rehash(hash_value)
            while self.slots[next_slot] is not None and self.slots[next_slot] != item:
                next_slot = self.rehash(next_slot)
                if next_slot == hash_value:  # we have done a full circle through the hash table
                    # no available slots
                    return slot_placed

            self.slots[next_slot] = item
            slot_placed = next_slot
        return slot_placed

    def get(self, item):
        """
        returns slot position if item in hashtable, -1 otherwise
        """
        start_slot = self.hash_function(item)

        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == item:
                found = True
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True
        if found:
            return position
        return -1

    def remove(self, item):
        """
        Removes item.
        Returns slot position if item in hashtable, -1 otherwise
        """
        start_slot = self.hash_function(item)

        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == item:
                found = True
                self.slots[position] = None
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True
        if found:
            return position
        return -1

    def hash_function(self, item):
        """
        Remainder method
        """
        return item % self.size

    def rehash(self, old_hash):
        """
        Plus 1 rehash for linear probing
        """
        return (old_hash + 1) % self.size
