import day_5_data

from collections import defaultdict, deque


def parse_input(data):
    rules_section, sequence_section = data.split("\n\n")
    
    rules = defaultdict(lambda: {"front": [], "behind": []})
    for rule in rules_section.splitlines():
        head_page, tail_page = map(int, rule.split("|"))
        rules[head_page]["behind"].append(tail_page)
        rules[tail_page]["front"].append(head_page)
    
    sequences = []
    for sequence in sequence_section.splitlines():
        sequences.append(list(map(int, sequence.split(","))))
    
    return rules, sequences


def is_order_valid(rules, sequence):
    original_index = {page: i for i, page in enumerate(sequence)}

    for page in sequence:
        
        for front_page in rules[page]["front"]:
            if front_page in original_index and original_index[front_page] > original_index[page]:
                return False
        
        for behind_page in rules[page]["behind"]:
            if behind_page in original_index and original_index[behind_page] < original_index[page]:
                return False
        
    return True


def correct_sequence(rules, sequence):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for num, rule in rules.items():
        for front in rule['front']:
            graph[front].append(num)
            in_degree[num] += 1
        for behind in rule['behind']:
            graph[num].append(behind)
            in_degree[behind] += 1

    filtered_graph = {num: [] for num in sequence}
    filtered_in_degree = {num: 0 for num in sequence}

    for num in sequence:
        if num in graph:
            for neighbor in graph[num]:
                if neighbor in sequence:
                    filtered_graph[num].append(neighbor)
                    filtered_in_degree[neighbor] += 1

    queue = deque([num for num in sequence if filtered_in_degree[num] == 0])
    sorted_sequence = []

    while queue:
        current = queue.popleft()
        sorted_sequence.append(current)
        for neighbor in filtered_graph[current]:
            filtered_in_degree[neighbor] -= 1
            if filtered_in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_sequence if len(sorted_sequence) == len(sequence) else "Invalid sequence"

        


def find_middle_page(sequence):
    n = len(sequence)
    return sequence[n // 2]


def main(data):
    rules, sequences = parse_input(data)
    
    total = 0
    for sequence in sequences:
        if not is_order_valid(rules, sequence):
            corrected_sequence = correct_sequence(rules, sequence)
            middle_page = find_middle_page(corrected_sequence)
            total += middle_page
    
    return total


print(main(day_5_data.DATA))
