# password-keyper
A random password generator that saves login information into a spreadsheet.

Build Version 1 - Published March 4, 2022

Upon installation, a file called "passwords.csv" will be automatically generated within the program folder.

Users will have the option to view all saved login information through the program by clicking "View Login Details"

#################
##  Main Menu  ##
#################

Clicking "View Login Details" will take the user to an embedded spreadsheet ("passwords.csv"). 
Clicking "Add Login Details" will bring the user to the "Add Login" window.
Clicking on "Initialize Data" will prompt the user if they wish to proceed with this action.
Clicking "Quit Program" will prompt the user to confirm this action.

##########################
##  View Login Details  ##
##########################

Clicking on any row will highlight it as active.  
Clicking on "Copy Password" when a row is highlighted will copy only the password to the machine's clipboard.
From there, the user can paste the password into their password field in their browzer.
Clicking on "Clear Login Data" will prompt the user to confirm their choice to clear their login data.
Upon confirmation, all data saved in the spreadsheet will be destroyed and will refresh within the app as an empty data table.
Clicking on "Main Menu" will bring the user back to the Main Menu screen.

#########################
##  Add Login Details  ##
#########################

Users will input whatever service they wish to record (Amazon, Google, Netflix, etc.)
Users will input whatever their username for that service is (johnsmith@email.com or johnsmith1234, etc.)
Clicking "Create Login" will record the information taken from both the above fields and will generate a 16 character password 
made up of random characters of upper case letters, lower case letters, numerals, and special characters.
All passwords begin with either an upper case or lower case letter.
Clicking "Add Login" will record all information, service, username, and new password, into the "passwords.csv" spreadsheet
and will clear the fields above for the next login information.
Clicking "Main Menu" will take the user back to the Main Menu screen.

#######################
##  Initialize Data  ##
#######################

Upon confirmation, this will clear all data from the spreadsheet. Use this option only if the original csv file has been
renamed or corrupted.

####################
##  Quit Program  ##
####################

Upon confirmation this will exit the program.
