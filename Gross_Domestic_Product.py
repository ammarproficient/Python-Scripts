def gdp(consumption, investment, govt_spending, exports, imports):

    gross_domestic_product = consumption + investment + govt_spending + (exports - imports)

    return gross_domestic_product


C = 10
I = 3
G = 2
X = 1
M = 0.5

gdp_value = gdp(C, I, G, X, M)

print(f"The GDP is: {gdp_value} trillion dollars")
