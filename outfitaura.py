## Outfit Aura
## Brigid O'Hara
## 25 Jan (9,10) 

# Color variables
happy = 'blue, pink and yellow'
happy2 = 'pink, royal blue, and orange'
calm = 'green, gray, and pink'
calm2 = 'brown, scarlet, and green'
sad = 'gray, blue, and red'
sad2= 'black, indigo, and gray'


# Start
print('Hey! Dress your mood with Outfit Aura. \n')

name = input('What is your name: ')
print('\n        Welcome, ' + name + '!! \n ')


# Q1 Aura Scale - 

mood1 = int(input('Feel and resonate with your aura. \n '
                 'On a Scale of 1-10: \n  '
                 'How do you feel today? '))

if mood1 >= 6:
        print('\nThat is great, ' + name + ' ! Show others how bright the day can '
              'be by wearing ' + happy + ' colors! \n')
                
elif mood1 == 5:
        print('\nNot knowing how you feel is ALWAYS okay! Wear ' + calm +
              ' to stay smooth!\n ')
elif mood1 <= 4:
        print('\nPretend dress up is soooo 3rd grade.'
              'Wear ' + sad + ' and accept your gloom. \n' )
else:
        print('unavailiable.')



# Q2 Change Aura Scale Input or Color Output
switch = input('Auras are meant to change. Try something different? ' )

if switch == 'yes':
        print('\nHow do you want to feel today? Scale of 1-10')
        mood2 = int(input(' '))

        if mood2 >= 6:
                print('\nTotally, ' + name + '! Wear' + happy + 'colors! \n')
                
        elif mood2 == 5:
                print('\n Wear ' + calm + 'and try your very best today.\n ')
                
        elif mood2 <= 4:
                print('\nHow you feel is how you feel!'
                      ' Wear ' + sad + ' and find comfort in these colors.\n' )
  
        else:
                print(unavailable)

                
else:
        
        newcolors = input('Glad you like how you feel! Change colors?' )

        if newcolors == 'yes':
                if mood1 >= 6:
                        print('\nYou know what you like, ' + name + '! Wear ' + happy2 + ' colors instead! \n')
                
                elif mood1 == 5:
                        print('\nWear ' + calm2 + 'to stay grounded.\n ')
                        
                elif mood1 <= 4:
                        print('\nHow you feel is how you feel!'
                                ' Wear ' + sad2 + ' colors. \n' )
  
                else:
                         print('goodbye')
                         
                


                
              

## simplify lines - if user only wants to change color (newcolors), can statement be sent back to mood1 input and conditions?
                         ## no copied conditions

##Add variables - practice pulling from a file
##Option to be given more or less than 3 colors
## Option to switch out color
                         ## happy.replace(1) 
##Add better descriptions
##Different color combos per number/emotion - updates upon change in color quanity

                 
                 





