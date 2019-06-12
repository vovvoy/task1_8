
"""
@Makers
Backstory: Usain Bolt, you, and Aybek
had a race. Surprisingly, Usain bolt won.
You came in 2nd and Aybek came in 3rd :(.
Can you think of a way to write a function 
that given a person's name, returns his/her place?
ALSO
Can you think of a way to write a function 
that given a place, returns his/her name?
WRITE 2 FUNCTIONS
One that converts choice to number
and
One that converts number to choice.
"""
#Make sure to un-comment the code test line
#all the way below when you are done.
#Remember to name your function correctly.
#   WRITE YOUR CODE HERE...



koroche = {'Usein':1,'Me':2, 'Aybek':3}





def choice_to_number(choice):
    return koroche(choice)





"""Convert choice to number."""
# If choice is Usain you should get back 1.



def number_to_choice(number):
    return get_key(koroche, choice)





"""Convert number to choice."""
# if number is 1 then return usain bolt.
#DO NOT remove lines below here,
#this is designed to test your code.



def get_key(koroche, value):
    for k, v in koroche.items():
        if v == value:
            return k



        
def test_choice_to_number():
  assert choice_to_number('Usain') == 1
  assert choice_to_number('Me') == 2
  assert choice_to_number('Aybek') == 3

def test_number_to_choice():
  assert number_to_choice(1) == 'Usain'
  assert number_to_choice(2) == 'Me'
  assert number_to_choice(3) == 'Aybek'

def test_all():
  try:
    test_choice_to_number()
    test_number_to_choice()

  except AssertionError:
    import wrong

  else:
    import success
#test your code by un-commenting the line(s) below
test_all()
                    
