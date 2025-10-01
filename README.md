📖 Background

The IITD Library, which houses thousands of rare books, is being digitized to make resources more accessible and searchable. To achieve this, the library requires:
A compressed dictionary per book containing only its words.


A search system to find relevant books containing a given keyword.

To implement this, we use two different approaches:

Musk’s Method (Sorting with MergeSort)

Jobs/Gates/Bezos’ Method (Hash Tables with different collision handling techniques)

⚙️ Implementation
1. Hash Tables

We implement custom hash tables without using Python’s inbuilt dict or set.
HashSet → Stores unique keys.
HashMap → Stores (key, value) pairs.
Collision Handling Methods:
Jobs → Chaining
Gates → Linear Probing
Bezos → Double Hashing

2. Hash Functions

Primary Hash Function → Polynomial Accumulation Hash with modulus compression.
Secondary Hash Function (Double Hashing only) → Uses different parameters (z2, c2) for step size.
3. Dynamic Resizing
If load factor ≥ 0.5, the table size doubles (to the next prime).
Elements are rehashed into the new table.

🏛 Digital Library Classes

Abstract Class: DigitalLibrary
Defines the core methods required by all libraries:

distinct_words(book_title)

count_distinct_words(book_title)

search_keyword(keyword)

print_books()

MuskLibrary (Sorting-based)

Uses MergeSort to extract distinct words.

Words are stored in lexicographically sorted order.

All books and texts are provided at initialization.

JGBLibrary (Hashing-based)

Uses a chosen hash table implementation (Jobs/Gates/Bezos).

Books are added one at a time.

Words stored in the order they appear in the hash table.
