from canvasapi import Canvas
from art import tprint
import settings
import getpass

def main():
    try: 
        instance = 'https://ubc.instructure.com'
        
        if settings.TOKEN:
            token = settings.TOKEN   
        else:
            token = getpass.getpass('Please input your Canvas API Token')
            
        
        canvas = Canvas(instance, token)

        user = canvas.get_user('self')

        tprint('Hey ' + user.name.split(' ')[0], font="Larry 3D")
        
        print("If you're seeing your name print out in text art you've set everything up correctly!")
    except Exception as e:
        print('Whoops, something went wrong. Check your setup has been done correctly.') # only worry about this if it prints below
        print('\nERROR:')
        print(str(e))

if __name__ == "__main__":
    main()