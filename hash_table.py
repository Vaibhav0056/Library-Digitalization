from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        self.collision_type = collision_type
        self.params = params
        self.num_elements = 0

        if self.collision_type == "Double":
            self.z1, self.z2, self.c2, self.table_size = params
        else:
            # For Chain and Linear
            self.z, self.table_size = params
        
        if self.collision_type == "Chain":
            self.table = [[] for _ in range(self.table_size)]
        else:
            self.table = [None] * self.table_size

    def _char_to_int(self, char):
        if 'a' <= char <= 'z':
            return ord(char) - ord('a')
        elif 'A' <= char <= 'Z':
            return ord(char) - ord('A') + 26
        return 0

    def _poly_hash(self, key, z):
        hash_val = 0
        power_of_z = 1
        for char in key:
            hash_val += self._char_to_int(char) * power_of_z
            power_of_z *= z
        return hash_val

    def _hash1(self, key):
        z = self.z1 if self.collision_type == "Double" else self.z
        return self._poly_hash(key, z) % self.table_size

    def _hash2(self, key):
        poly_hash = self._poly_hash(key, self.z2)
        return self.c2 - (poly_hash % self.c2)

    def get_slot(self, key):
        return self._hash1(key)

    def get_load(self):
        if self.table_size == 0:
            return 0
        return self.num_elements / self.table_size

    def insert(self, x):
        pass
    
    def find(self, key):
        pass
    
    def __str__(self):
        pass

class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
    
    def insert(self, key):
        if self.find(key):
            return

        initial_slot = self.get_slot(key)

        if self.collision_type == "Chain":
            self.table[initial_slot].append(key)
            self.num_elements += 1
            return

        i = 0
        while i < self.table_size:
            slot = 0
            if self.collision_type == "Linear":
                slot = (initial_slot + i) % self.table_size
            else:  # Double
                step = self._hash2(key)
                slot = (initial_slot + i * step) % self.table_size

            if self.table[slot] is None:
                self.table[slot] = key
                self.num_elements += 1
                return
            i += 1
    
    def find(self, key):
        initial_slot = self.get_slot(key)

        if self.collision_type == "Chain":
            return key in self.table[initial_slot]

        i = 0
        while i < self.table_size:
            slot = 0
            if self.collision_type == "Linear":
                slot = (initial_slot + i) % self.table_size
            else:  # Double
                step = self._hash2(key)
                slot = (initial_slot + i * step) % self.table_size
            
            if self.table[slot] is None:
                return False
            if self.table[slot] == key:
                return True
            i += 1
        return False
    
    def __str__(self):
        result = []
        for slot_content in self.table:
            if self.collision_type == "Chain":
                if not slot_content:
                    result.append("(EMPTY)")
                else:
                    result.append("; ".join(map(str, slot_content)))
            else:
                if slot_content is None:
                    result.append("(EMPTY)")
                else:
                    result.append(str(slot_content))
        return " | ".join(result)

class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
    
    def insert(self, x):
        key, value = x
        if self.find(key) is not None:
            return

        initial_slot = self.get_slot(key)

        if self.collision_type == "Chain":
            self.table[initial_slot].append((key, value))
            self.num_elements += 1
            return
        
        i = 0
        while i < self.table_size:
            slot = 0
            if self.collision_type == "Linear":
                slot = (initial_slot + i) % self.table_size
            else:  # Double
                step = self._hash2(key)
                slot = (initial_slot + i * step) % self.table_size

            if self.table[slot] is None:
                self.table[slot] = (key, value)
                self.num_elements += 1
                return
            i += 1
    
    def find(self, key):
        initial_slot = self.get_slot(key)

        if self.collision_type == "Chain":
            for k, v in self.table[initial_slot]:
                if k == key:
                    return v
            return None

        i = 0
        while i < self.table_size:
            slot = 0
            if self.collision_type == "Linear":
                slot = (initial_slot + i) % self.table_size
            else:  # Double
                step = self._hash2(key)
                slot = (initial_slot + i * step) % self.table_size

            if self.table[slot] is None:
                return None
            if self.table[slot][0] == key:
                return self.table[slot][1]
            i += 1
        return None
    
    def __str__(self):
        result = []
        for slot_content in self.table:
            if self.collision_type == "Chain":
                if not slot_content:
                    result.append("(EMPTY)")
                else:
                    formatted_entries = [f"({k}, {v})" for k, v in slot_content]
                    result.append("; ".join(formatted_entries))
            else:
                if slot_content is None:
                    result.append("(EMPTY)")
                else:
                    k, v = slot_content
                    result.append(f"({k}, {v})")
        return " | ".join(result)