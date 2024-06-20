import webbrowser
import re

try:
    # Ensure the correct path to the text file is provided
    with open('links.txt') as f:
        lines = f.readlines()
        for line in lines:
            # Find all substrings that start with 'https' and are followed by non-whitespace characters
            links = re.findall(r'https://[^\s]+', line)
            for link in links:
                print(link)
                # The following code will open all the links from your text file
                webbrowser.open(link)
except FileNotFoundError:
    print("The file 'links.txt' was not found.")
