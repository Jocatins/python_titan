def titan_intro(dict):
    for key,val in dict.items():
        print(f'I am a {key}, and I possess {val} skill')



titan_skills = {}

while True:
    titan_name = input('enter a titan name ')
    titan_skill = input('enter a skill of the titan ')
    titan_skills[titan_name] = titan_skill

    theother = input ('any other ?(yes/no)')
    if theother == 'yes':
        continue
    else:
        break

titan_intro(titan_skills)









# age = int(input ('enter your age '))
#
# if age < 10:
#     print('you are an old man')
# elif age <40:
#     print ('you are young ')
# else:
#     print('you are an ancestor')

# titans = ['joca','khamen','owes','nico']

# for titan in titans:
#     print (titan)

# for titan in titans[0:3] :
#     print (titan)
# for titan in titans:
#     if titan == 'owes':
#         print(f'{titan} - he is a gypsy')
#         break
#     else:
#         print(titan)
# age = 20
# num = 0
# while num < age:
#     if num == 0:
#         num += 1
#         continue
#     if num % 3 == 0:
#         print(num)
#     if num > 10:
#         break
#     num += 1
# for n in range (0,20,5):
#     print(n)

# def area (radius):
#     print(3.142 * radius * radius)
#
#
# radius = int(input ('enter a radius '))
# length = int(input('enter a length'))
#
# area(radius)
