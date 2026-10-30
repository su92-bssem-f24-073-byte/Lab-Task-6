variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V']
colors = ['Red', 'Green', 'Blue']
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}
def is_valid(var, color, assignment):
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def map_coloring(assignment={}):
    if len(assignment) == len(variables):
        return assignment
    unassigned = [v for v in variables if v not in assignment][0]   
    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color
            result = map_coloring(assignment)
            if result:
                return result
            assignment.pop(unassigned)           
    return None
print("Map Coloring Solution:", map_coloring())