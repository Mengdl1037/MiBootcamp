# UTF-8
# Author: Liu Mengdi
# Date: 2024-06-20
# Function:

invitees = ['Zhang San', 'Li Si', 'Wang Wu']

for invitee in invitees:
    print('Good morning, %s, would you like to attend a dinner at my home tonight? Waiting for you.' %invitee)
print('\n')

print('Li Si can not take part in the dinner.\n')

invitees.remove('Li Si')

invitees.append('Xiao Mei')

for invitee in invitees:
    print('Good morning, %s, would you like to attend a dinner at my home tonight? Waiting for you.' %invitee)
print('\n')

invitees.insert(0, 'Xiao Hong')
invitees.insert(len(invitees) >> 1, 'Xiao Ming')
invitees.append('Li Hua')

for invitee in invitees:
    print('Good morning, %s, would you like to attend a dinner at my home tonight? Waiting for you.' %invitee)
print('\n')
