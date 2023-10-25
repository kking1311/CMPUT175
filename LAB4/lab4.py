#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program: use one list together with a variable containing the current index to enable both the back button.It will   just display the URL address of the current page that the user is on.
# Author: Kanishk Ashra
# Collaborators/references: University of Alberta
#----------------------------------------------------

def getAction():
    '''
    Write docstring to describe function
    Inputs: No inputs
    Returns: string
    '''
    # TO DO: delete pass and write your code here
    possibleActions=['=','<','>','q']
    action=input("Enter = to enter a URL, < to go back, > to go forward, q to quit:")
    if action in possibleActions:
        return str(action)
    return False


def goToNewSite(current, pages):
    '''
    Prompts the user to enter a new website address, adds it to the list of webpages, and updates the index.
    Inputs: int (current index), list (webpages)
    Returns: int (updated index)
    '''
    new_site = input("URL: ")
    pages.append(new_site)
    return len(pages) - 1

def goBack(current, pages):
    '''
    Navigates back to the previous webpage in the history.
    Inputs: int (current index), list (webpages)
    Returns: int (updated index)
    '''
    if current > 0:
        return current - 1
    else:
        print("Cannot go back.")
        return current

def goForward(current, pages):
    '''
    Navigates forward to the next webpage in the history.
    Inputs: int (current index), list (webpages)
    Returns: int (updated index)
    '''
    if current < len(pages) - 1:
        return current + 1
    else:
        print("Cannot go forward.")
        return current


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    index = 0
    quit = True
    while quit:
        print('\nCurrently viewing', websites[index])
        action = getAction()
        if action == '=':
            index = goToNewSite(index, websites)
        elif action == '<':
            index = goBack(index, websites)
        elif action == '>':
            index = goForward(index, websites)
        elif action == 'q':
            quit=False
            break 
        else:
            print("Wrong input. Please enter a correct action")
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    