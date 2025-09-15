def import_growth_rate(current_imports, previous_imports):

    igr = ((current_imports - previous_imports) / previous_imports) * 100

    return igr


current = 550
previous = 10

print("Import Growth Rate is:", import_growth_rate(current, previous))
