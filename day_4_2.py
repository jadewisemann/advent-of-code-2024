from itertools import product

import day_4_data
raw_data = day_4_data.DATA


def find_matches(graph, target_words):
    
    return sum(
        (
            "".join([graph[i-di][j-di] for di in [-1, 0, 1]]) in target_words
            and "".join([graph[i-di][j-dj] for di, dj in   [[-1, 1],[0,0], [1, -1]]]) in target_words
        )
        for i, j in product( range(1, len(graph) - 1), range(1, len(graph[0]) - 1) )
    )
    
    # return sum(
    #     (
    #         graph[i-1][j-1] + graph[i][j] + graph[i+1][j+1] in target_words
    #         and graph[i-1][j+1] + graph[i][j] + graph[i+1][j-1] in target_words
    #     )
    #     for i, j in product(range(1, len(graph) - 1), range(1, len(graph[0]) - 1))
    # )


result = find_matches(raw_data.strip().splitlines(), ["MAS", "SAM"]) 

print(result)

