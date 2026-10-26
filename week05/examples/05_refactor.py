def contribution_margin(price, variable_cost):
    return price - variable_cost

def break_even_units(fixed_cost, margin):
    return fixed_cost / margin

margin = contribution_margin(250, 150)
print(f"Break-even units: {break_even_units(5000, margin):.0f}")
