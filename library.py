import dynamic_hash_table as dht

class DigitalLibrary:
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    def __init__(self, book_titles, texts):
        self.books = {}
        self.keyword_index = {}
        
        for title, text in zip(book_titles, texts):
            sorted_text = self._merge_sort(list(text))
            
            unique_words = []
            if sorted_text:
                unique_words.append(sorted_text[0])
                for i in range(1, len(sorted_text)):
                    if sorted_text[i] != sorted_text[i-1]:
                        unique_words.append(sorted_text[i])

            self.books[title] = unique_words
            
            for word in unique_words:
                if word not in self.keyword_index:
                    self.keyword_index[word] = []
                self.keyword_index[word].append(title)

    def _merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L, R = arr[:mid], arr[mid:]
            self._merge_sort(L)
            self._merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        return arr

    def distinct_words(self, book_title):
        return self.books.get(book_title, [])
    
    def count_distinct_words(self, book_title):
        return len(self.books.get(book_title, []))
    
    def search_keyword(self, keyword):
        return self.keyword_index.get(keyword, [])
    
    def print_books(self):
        for title in sorted(self.books.keys()):
            words = self.books[title]
            print(f"{title}: {' '.join(words)}")

class JGBLibrary(DigitalLibrary):
    def __init__(self, name, params):
        self.name = name
        self.params = params
        self.books = {} 
        self.collision_type = ""
        
        if name == "Jobs": self.collision_type = "Chain"
        elif name == "Gates": self.collision_type = "Linear"
        elif name == "Bezos": self.collision_type = "Double"
        
        self.keyword_index = dht.DynamicHashMap(self.collision_type, self.params)
    
    def add_book(self, book_title, text):
        if book_title in self.books:
            return
            
        book_ht = dht.DynamicHashSet(self.collision_type, self.params)
        self.books[book_title] = book_ht
        
        unique_words_in_book = []
        for word in text:
            if not book_ht.find(word):
                unique_words_in_book.append(word)
            book_ht.insert(word)

        for word in unique_words_in_book:
            found_list = self.keyword_index.find(word)
            if found_list is None:
                self.keyword_index.insert((word, [book_title]))
            else:
                if book_title not in found_list:
                    found_list.append(book_title)
    
    def distinct_words(self, book_title):
        book_ht = self.books.get(book_title)
        if not book_ht:
            return []
        
        words = []
        for slot in book_ht.table:
            if book_ht.collision_type == "Chain":
                words.extend(slot)
            elif slot is not None:
                words.append(slot)
        return words
    
    def count_distinct_words(self, book_title):
        book_ht = self.books.get(book_title)
        return book_ht.num_elements if book_ht else 0
    
    def search_keyword(self, keyword):
        result = self.keyword_index.find(keyword)
        return result if result is not None else []
    
    def print_books(self):
        for title in sorted(self.books.keys()):
            hashtable = self.books[title]
            print(f"{title}: {str(hashtable)}")
