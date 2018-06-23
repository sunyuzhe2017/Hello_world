#Ubuntu can't support chinese character！
import easygui as g
import sys

while 1:
    g.msgbox('Hi,Welcome to your first interface game！')

    msg = 'What would you like to learn here？'
    title = 'little game interface!'
    choices = ['Love','Program','OOXX','QinQiShuHua']

    choice = g.choicebox(msg,title,choices)

    # note that we convert choice to string,in case
    # the user cancelled ths choice ,and we got none,
    g.msgbox ('Your choice：'+ str(choice),'result')

    msg = 'Would you like to restart the game？'
    title = 'Please make your chioce'

    if g.ccbox(msg,title): #show aContinuue/Cancel dialog
        pass # user chose Continue
    else:
        sys.exit(0) #user chose Cancel
    
