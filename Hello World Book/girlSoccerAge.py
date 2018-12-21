print('What is your gender?')
print('[m]ale or [f]emale')
gender = input('Gender:' )
if gender == 'm':
      print('Sorry, but you are not eligible to play on the team.')
if gender == 'f':
      print('You are eligible to play on the team')
      print('but we need your age to be specific about you.')
      age = int(input('Age:'))
      if age == 10 or age == 11 or age == 12:
            print('Great! You are on the rosters for the team!')
      if age > 12:
            print('Sorry, but you are older than our qualifications.')
      if age < 10:
            print('Sorry, but you are younger than our qualifications.')


