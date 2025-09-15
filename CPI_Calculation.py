def cpi_calculation(current_year, base_year):
    cpi = (current_year / base_year) * 100
    return cpi


def check_cpi(cpi):
    if cpi > 100:
        return "Positive CPI: Inflation has occurred."
    elif cpi < 100:
        return "Negative CPI: Deflation has occurred."
    else:
        return "No change in CPI."


# Getting inputs from the user
base = float(input('Enter base year value: '))
current = float(input('Enter current year value: '))

# Calculating CPI
total_cpi = cpi_calculation(current, base)

# Displaying the result and checking for positive or negative change
print(f'Total CPI is {total_cpi}')
print(check_cpi(total_cpi))
