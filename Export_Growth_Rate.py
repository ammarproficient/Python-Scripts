def export_growth_rate(current_export, previous_export):

    egr = ((current_export - previous_export) / previous_export) * 100

    return egr


current = 550
previous = 10

print("Import Growth Rate is:", export_growth_rate(current, previous))
