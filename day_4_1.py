from itertools import product

import day_4_data
raw_data = day_4_data.DATA


def find_matches(graph, target_word):
    DIRS = [(0, 1), (1, 1), (1, 0), (1, -1)]
    ans = 0
    
    for starting_i, starting_j, (di, dj, *_) in product(range(len(graph)), range(len(graph[0])), DIRS):
        current_i, current_j, char_index = starting_i, starting_j, 0
        
        while(
            0 <= current_i < len(graph)
            and 0 <= current_j < len(graph[current_i])
            and char_index < len(target_word)
            and graph[current_i][current_j] == target_word[char_index]
        ):
            current_i += di
            current_j += dj
            char_index += 1
        
        ans += char_index == len(target_word)
        
    return ans



result = sum(
    find_matches(raw_data.strip().splitlines(), word) 
    for word in ["XMAS", "SAMX"]
)

print(result)