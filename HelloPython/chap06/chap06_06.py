# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

candidates = ['jen', 'sarah', 'edward', 'phil', 'zhang', 'li', 'wang', 'zhao']

for candidate in candidates:
    if candidate in set(favorite_languages.keys()):
        print(f"Thank you for taking the poll, {candidate.title()}!")
    else:
        print(f"{candidate.title()}, \
              what's your favorite programming language? Thank you very much!")