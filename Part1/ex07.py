ages = {'Hans': 24, 'Prag': 23, 'Bunyod': 18}

print(ages)  # {'Hans': 24, 'Prag': 23, 'Bunyod': 18}

print(ages['Hans'])  # → 24

ages['Prag'] = 30

print(ages['Prag'])  # → 30

del ages['Bunyod']

print(ages)  # {'Hans': 24, 'Prag': 30}