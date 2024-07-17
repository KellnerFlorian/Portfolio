# import the regular expressions library
import re

# assume someone gives you his/her name
name = input("What is your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")
