import day_5_data

from collections import defaultdict


def parse_input(data):
    rules_section, sequence_section = data.split("\n\n")
    
    rules = []
    for rule in rules_section.splitlines():
        head_page, tail_page = map(int, rule.split("|"))
        rules.append((head_page, tail_page))
    
    sequences = []
    for sequence in sequence_section.splitlines():
        sequences.append(list(map(int, sequence.split(","))))
    
    return rules, sequences


def is_order_valid(rules, sequence):
    original_index = {page: i for i, page in enumerate(sequence)}
    
    for head_page, tail_page in rules:
        if head_page in original_index and tail_page in original_index:
            if original_index[head_page] > original_index[tail_page]:
                return False
    return True


def find_middle_page(sequence):
    n = len(sequence)
    return sequence[n // 2]


def main(data):
    rules, sequences = parse_input(data)
    
    total = 0
    for sequence in sequences:
        if is_order_valid(rules, sequence):
            middle_page = find_middle_page(sequence)
            total += middle_page
    
    return total


print(main(day_5_data.DATA))
