import subprocess

# Run the pip list command and capture the output
result = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE, text=True)

# Split the output into lines
packages = result.stdout.split('\n')

# Print the total number of installed packages (excluding the header and footer lines)
total_packages = len(packages) - 3
print(f"Total number of installed packages: {total_packages}")

# Define the output file name
output_file = 'total_packages.txt'

# Write the list of packages to the output file
with open(output_file, 'w') as f:
    for package in packages[2:-1]:  # Skip the header and footer lines
        f.write(package.split()[0] + '\n')

print(f"List of installed packages has been written to {output_file}")



# this below code will print all the packages name with package number

# import subprocess
#
# # Run the pip list command and capture the output
# result = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE, text=True)
#
# # Split the output into lines
# packages = result.stdout.split('\n')
#
# # Print the total number of installed packages (excluding the header lines)
# total_packages = len(packages) - 3
# print(f"Total number of installed packages: {total_packages}")
#
# # Print each package name with its index
# for index, package in enumerate(packages[2:-1], start=1):  # Skip the header and footer lines
#     package_name = package.split()[0]  # Extract the package name
#     print(f"{index}: {package_name}")