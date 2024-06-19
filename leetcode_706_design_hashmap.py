# pylint disable=all


class MyHashMap:
    """Design a HashMap without using any built-in hash table libraries."""

    def __init__(self) -> None:
        """Initialize the object with an empty map."""
        self.map = {}

    def put(self, key: int, value: int) -> None:
        """Insert a (key, value) pair into the HashMap.
        If the key already exists in the map,
        update the corresponding value.
        """
        self.map[key] = value

    def get(self, key: int) -> int:
        """Return the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key.
        """
        return self.map.get(key, -1)

    def remove(self, key: int) -> None:
        """Remove the key and its corresponding value
        if the map contains the mapping for the key.
        """
        if key in self.map:
            del self.map[key]

    def contains_key(self, key: int) -> bool:
        """Return a boolean telling whether the key is contained in the map."""
        return key in self.map

    def size(self) -> int:
        """Return the size of the map."""
        return len(self.map)

    def print_map(self) -> None:
        """Print the map."""
        for key, value in self.map.items():
            print(f"|{key}:{value}|")


if __name__ == "__main__":
    m: MyHashMap = MyHashMap()
    print(f"size = {m.size()}")  # should print size = 0

    m.put(0, 1)
    print(f"size = {m.size()}")  # should print size = 1

    m.put(0, 0)
    print(f"size = {m.size()}")  # should print size = 1

    print(f"get {m.get(0)}")  # should print get 0

    m.put(1, 1)
    m.put(2, 2)
    print(f"size = {m.size()}")  # should print size = 3

    print(f"3 in m? {m.contains_key(3)}")  # should print 3 in m? False
    print(f"2 in m? {m.contains_key(2)}")  # should print 2 in m? True

    m.put(3, 3)
    m.put(4, 4)
    m.put(5, 5)
    m.put(6, 6)
    print(f"size = {m.size()}")  # should print size = 7

    m.print_map()
