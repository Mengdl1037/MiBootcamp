from die import Die

die_with_6_sides = Die(6)
print("Rolling a 6-sided die 10 times:")
for i in range(1, 11):
    die_with_6_sides.roll_die()
print('\n')

print("Rolling a 10-sided die 10 times:")
die_with_6_sides = Die(10)
for i in range(1, 11):
    die_with_6_sides.roll_die()
print('\n')

print("Rolling a 20-sided die 10 times:")
die_with_6_sides = Die(20)
for i in range(1, 11):
    die_with_6_sides.roll_die()
print('\n')
