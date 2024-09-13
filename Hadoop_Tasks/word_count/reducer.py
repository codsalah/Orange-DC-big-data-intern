#!/usr/bin/env python3
import sys


# for the shuffle(sort) phase 
# cat input.txt | python3 mapper.py | sort


current_word = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f'{current_word}\t{current_count}')
        current_word = word
        current_count = count

if current_word:
    print(f'{current_word}\t{current_count}')
