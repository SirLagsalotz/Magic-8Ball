#The magic 8 ball is a fortune-telling ball that is used to make decisions for a yes or no question. 
# Create 30 random responses in a plain text file.  Be sure to include some affirmative, 
# some non-committal and some negative sentences.  The script will prompt the user to ask a question. 
# The script will retrieve the response statements from the file, it will appear to be contemplating 
# the question, then return a randomly selected response to the user.  The use of ASCII art is 
# encouraged to create visual appeal. 
#File I/O, imported modules, error detection as well as command line interface allowing for user input
import time
from ballMod import ball
i= 0
while i < 1 :
    print("\033c")
    question = input('What would you like to ask? : ')
    print("\033c")
    print('You asked : ',question)
    confirm = input ('is that correct? Yes or No? : ')
    if confirm == "No":
        print('Try Again')
    elif confirm == "Yes":
        print('8 Ball Will Think')
        i += 1
    else:
        print('Incorrect answer. Try Again with Yes or No')
    
#waiting
time.sleep(1)
print("\033c")
print('Thinking.')
time.sleep(1)
print("\033c")
print('Thinking..')
time.sleep(1)
print("\033c")
print('Thinking...')
time.sleep(1)
print("\033c")
#8 Ball Results
print('The 8 Ball says...')
print('///////////////////////////////')
print('///////////@@@@@@@@@///////////')
print('//////@@@@@@@@@@@@@@@@@@@//////')
print('////@@@@@@@@@@@@@@@@@@@@@@@////')
print('//@@@@@@@@@         @@@@@@@@@//')
print('@@@@@@@@              @@@@@@@@/')
print('/@@@@@@@               @@@@@@@/')
print('      ',ball.line,'       ')
print('/@@@@@@@               @@@@@@@/')
print('/@@@@@@@@             @@@@@@@@/')
print('//@@@@@@@@@          @@@@@@@@@//')
print('////@@@@@@@@@@@@@@@@@@@@@@@////')
print('//////@@@@@@@@@@@@@@@@@@@//////')
print('///////////@@@@@@@@@///////////')
print('///////////////////////////////')