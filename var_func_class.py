import pandas as pd
import types

# Get all attributes of the numpy module
all_attributes = dir(pd)

# Separate attributes into variables, classes, and functions
variables = []
classes = []
functions = []

for attr in all_attributes:
    attribute = getattr(pd, attr)
    if isinstance(attribute, types.BuiltinFunctionType) or isinstance(attribute, types.FunctionType):
        functions.append(attr)
    elif isinstance(attribute, type):
        classes.append(attr)
    else:
        variables.append(attr)

# Combine the lists into a formatted string
output = []

output.append("VARIABLES:\n\n\n")
output.extend([f"{variable}\n" for variable in variables])

output.append("\nFUNCTIONS:\n\n\n")
output.extend([f"{function}\n" for function in functions])

output.append("\nCLASSES:\n\n\n")
output.extend([f"{cls}\n" for cls in classes])


# Write the formatted string to a file
output_string = "".join(output)
filename = 'pandas_attributes.txt'
with open(filename, 'w') as f:
    f.write(output_string)

print(f"The list of Pandas attributes has been saved to {filename}.")