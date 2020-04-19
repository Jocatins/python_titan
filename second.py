def titan_count(dict):
    titans = list(dict.values())
    for titan in set(titans):
        num = titans.count(titan)
        print(f'there are {num} {titan} skills ')

titan_skills = {}

while True:
    titan_name = input('enter a titan name ')
    titan_skill = input('enter a titan skill ')
    titan_skills[titan_name] = titan_skill

    another = input('add another skill? y/n')
    if another == 'n':
        break
    else:
        continue

titan_count(titan_skills)
