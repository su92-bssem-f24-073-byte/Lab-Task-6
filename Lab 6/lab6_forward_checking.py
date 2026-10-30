variables = ['WA', 'NT', 'SA']
domains = {v: ['Red', 'Green', 'Blue'] for v in variables}
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA'],
    'SA': ['WA', 'NT']
}
def forward_checking(assignment, domains):
    if len(assignment) == len(variables):
        return assignment
    unassigned = [v for v in variables if v not in assignment][0]
    for value in list(domains[unassigned]):
        new_assignment = assignment.copy()
        new_assignment[unassigned] = value
        new_domains = {v: list(domains[v]) for v in domains}
        new_domains[unassigned] = [value]
        consistent = True
        for neighbor in neighbors[unassigned]:
            if neighbor not in new_assignment:
                if value in new_domains[neighbor]:
                    new_domains[neighbor].remove(value)
                if not new_domains[neighbor]:
                    consistent = False
                    break
        if consistent:
            result = forward_checking(new_assignment, new_domains)
            if result:
                return result
    return None
print("Forward Checking Solution:", forward_checking({}, domains))