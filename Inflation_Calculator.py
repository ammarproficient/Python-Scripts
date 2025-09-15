def inflation_calculation(current_year_cpi, previous_year_cpi):
    # Check if the previous CPI is non-zero to avoid division by zero
    if previous_year_cpi == 0:
        return "Error: Previous year CPI cannot be zero."

    inflation_rate = ((current_year_cpi - previous_year_cpi) / previous_year_cpi) * 100
    return inflation_rate


try:
    current = float(input('Enter current year CPI: '))
    previous = float(input('Enter previous year CPI: '))

    # Check if both values are positive
    if current < 0 or previous < 0:
        print("Error: CPI values cannot be negative.")
    else:
        print(f"Inflation Rate: {inflation_calculation(current, previous)}%")
except ValueError:
    print("Error: Please enter a valid number.")
