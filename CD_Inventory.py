#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# MStallworth, 2020-Sep-1, added code to CD class, loading and saving inventory
# MStallworth, 2020-Sep-1, added code to main body and various menu functions under IO class
# MStallworth, 2020-Sep-2, added __str__ function to CD class and fixed docstrings
# MStallworth, 2020-Sep-2, added structured error handling where applicable
# MStallworth, 2020-Sep-2, fixed function for adding CD 
# MStallworth, 2020-Sep-2, tested code and all functions
#------------------------------------------#

# -- DATA -- #
import pickle
strFileName = 'cdInventory.dat'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODone Add Code to the CD class
    
    # -- Fields -- #
    
    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        # -- Attributes -- #
        self.__cd_id = int(cd_id)
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
    
    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = value
    @property 
    def cd_title(self):
        return self.__cd_title.title()
    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = value
    @property
    def cd_artist(self):
        return self.__cd_artist.title()
    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = value

    
    # -- Methods -- #
    def __str__(self):
        return f'{self.cd_id}\t{self.cd_title} (by:{self.cd_artist})'

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODone Add code to process data from a file
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of objects

        Reads the data from file identified by file_name into a 2D table
        (list of objects) table one line in the file represents one object row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime

        Returns:
            None.
        """
        with open(file_name, 'rb') as objFile:
            data = pickle.load(objFile)
            return data
        
     
    # TODone Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Function to write in memory data into a file
        Saves the data into identified file name from a 2D table
        
        
        Args:
            file_name (string): name of the file used to save the data
            lst_Inventory: 2D data structure used to save the in memory data
            
            
        Returns:
            None.
        """
        with open(file_name, 'wb') as objFile:
            pickle.dump(lst_Inventory, objFile)
        

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    """ Handling Input/Output
    
    properties: 
        
    methods: 
        print_menu(): -> None
        menu_choice(): -> choice (letter corresponding to menu option)
        show inventory(table): -> None
        add entry(): -> cd_id(ID for data entry), cd_title(input for CD title, cd_artist(input for artist for CD))
    """
    # TODone add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
    # TODone add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')
    # TODone add code to get CD data from user
    @staticmethod
    def add_entry():
        """Adds user input into the in memory inventory 
        using .add_data() from Data Processing Class 
        
        
        Args:
            None.
            
            
        Returns:
            cd_id (string): ID for data entry
            cd_title (string): Input for CD Title
            cd_artist (string): Input for Artist Name 
        """
        cd_id = input('Please enter an ID:').strip()
        cd_title = input('Please enter a CD title:').strip()
        cd_artist = input('Please enter an artist name:').strip()
        return cd_id, cd_title, cd_artist


# -- Main Body of Script -- #
# TODone Add Code to the main body
# Load data from file into a list of CD objects on script start
try:
    lstOfCDObjects.clear()
    CDfile = FileIO.load_inventory(strFileName)
    lstOfCDObjects.extend(CDfile)
    IO.show_inventory(lstOfCDObjects)
    print('Welcome back!')
except FileNotFoundError:
    print('\nThere is no file currently avaiable!\n')
    print('Hello. Welcome to the program! Creating new file for you...\n')
    FileIO.save_inventory(strFileName, lstOfCDObjects)
    print('File has been created. You may now enter the program!\n')
# Display menu to user
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
    # let user exit program
    if strChoice == 'x':
        print('\nGoodbye.')
        break
    # let user load inventory from file
    if strChoice == 'l':
         print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
         strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
         if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects.clear()
            CDfile = FileIO.load_inventory(strFileName)
            lstOfCDObjects.extend(CDfile)
            IO.show_inventory(lstOfCDObjects)
         else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
            continue 
    # let user add data to the inventory
    elif strChoice == 'a':
        ID, Title, Artist = IO.add_entry()
        try: # error handling to make sure ID is an integer
            cd_id = int(ID)
        except ValueError:
            print('\nYour ID must be an integer!\n')
            print('This entry was not added to the inventory. Try again.\n')
            continue
        new_cd = CD(ID, Title, Artist)
        lstOfCDObjects.append(new_cd)
        IO.show_inventory(lstOfCDObjects)
        continue
    # show user current inventor
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue
    # let user save inventory to file
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # Process choice
        if strYesNo == 'y':
            # save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
            print('\nYour inventory was successfully saved to the file!\n')
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')

