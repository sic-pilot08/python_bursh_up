unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing models: {current_design.title()}")
    completed_models.append(current_design)

for design in completed_models:
    print(f"{design.title()}")