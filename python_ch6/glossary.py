glossary = {
    'variable': 'A reserved memory location to store values.',
    'string': 'A series of characters enclosed in quotes.',
    'list': 'A collection of items in a particular order.',
    'loop': 'A block of code that repeats a specified number of times or until a condition is met.',
    'dictionary': 'A collection of key-value pairs.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")