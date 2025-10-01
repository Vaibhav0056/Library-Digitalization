from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        old_table = self.table
        
        self.table_size = get_next_size()
        self.num_elements = 0
        if self.collision_type == "Chain":
            self.table = [[] for _ in range(self.table_size)]
        else:
            self.table = [None] * self.table_size
        
        if self.collision_type == "Chain":
            for bucket in old_table:
                for key in bucket:
                    self.insert(key)
        else:
            for key in old_table:
                if key is not None:
                    self.insert(key)
        
    def insert(self, x):
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        old_table = self.table

        self.table_size = get_next_size()
        self.num_elements = 0
        if self.collision_type == "Chain":
            self.table = [[] for _ in range(self.table_size)]
        else:
            self.table = [None] * self.table_size

        if self.collision_type == "Chain":
            for bucket in old_table:
                for item in bucket:
                    self.insert(item)
        else:
            for item in old_table:
                if item is not None:
                    self.insert(item)
        
    def insert(self, x):
        super().insert(x)
        
        if self.get_load() >= 0.5:
            self.rehash()