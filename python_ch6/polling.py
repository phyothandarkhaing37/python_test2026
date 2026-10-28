favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_to_poll = ['jen', 'alex', 'sarah', 'michael', 'phil', 'david']

for name in people_to_poll:
    if name in favorite_languages:
        print(f"Thank you for responding, {name.title()}!")
    else:
        print(f"Hi {name.title()}, please take our favorite languages poll!")