#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date
import sys
#====Login Section====

#Reads usernames and password from the user.txt file
with open('user.txt','r') as user_database:
    dict = {}
    user_database_names = user_database.read().split('\n')

#Uses a dictionary to store a list of usernames and passwords from the file.
#Using a for loop, iterate through each line in the user.txt file, splitting each line into two items by a comma separator
#Assigning the first item as the username and second as the password
for item in user_database_names:
    item = item.split(',')
#Assigning the first item as the username and second as the password
    username = item[0]
    password = item[1]
#Adding the items into the dictionary as a key-value format
    dict[username] = password

#Uses a while loop to validate user name and password
while True:
#Request username input from user
    inputted_username = input("Username: ")
#If the username exists in the dictionary, it is accepted. Otherwise the loop continues and input is requested again
    if inputted_username in dict:
        print('\nUsername accepted! \n')
#Uses a while loop to request password from user until correct password is given
        while True:
            password_req = input("Password: ")
#Testing if password is correct
            if password_req == dict[inputted_username]:
                print('\nYou are in!')
                break
            else:
                print('\nIncorrect Password\n')
                continue
        break
    else:
        print('Username not recognised')
        continue
    
#====Menu Section====
while True:
#Presenting the menu to the user and 
#making sure that the user input is converted to lower case.
    menu = input('\nSelect one of the following Options below:\nr - Registering a user\na - Adding a task\nva - View all tasks\nvm - view my task\ne - Exit\n').lower()

#MENU OPTION 1: adding a new user
    if menu == 'r':
        while True:
#Request input of a new username
            new_user = input('New Username: ')
            if new_user in dict:
                print('\nUsername taken - please try again!\n')
                continue
#Request input of a new password
            new_password = input('New Password: ')
#Request input of password confirmation.
            confirmed_password = input('Confirm Password: ')
#Check if the new password and confirmed password are the same.
            if new_password == confirmed_password:
#If they are the same, add them to the user.txt file,
                with open('user.txt','a') as registering:
                    registering.write('\n'+ new_user +',' + new_password)
                print('\nUser accepted!\n')
                break
            else:
#Otherwise presenting a relevant message.
                print('Password not matching - try again!\n')
                continue
            
#MENU OPTION 2: adding a new task
    elif menu == 'a':
#Prompting user for username, title, description and due date of task
        while True:
            assigned_username=input("Enter the username of the person to whom the task is assigned to: ")
#The assigned user must exist in username dictionary; if not user input is requested again
            if assigned_username not in dict:
                print("\nUsername not recognised - try again!\n")
                continue
            else:
                break
        assigned_title = input("Task title: ")
        assigned_description = input("Task description: ")
        assigned_due_date = input("Due date: ")
#Retrieves current date
        today = str(date.today())
#Sets completion status variable to No since task has only just been added
        completion_status = 'No'
#Adds the data to the file task.txt in correct formatting
        with open('tasks.txt','a') as task_writer:
            task_writer.write('\n'+ assigned_username + ',' + assigned_title + ',' + assigned_description + ',' + today + ',' + assigned_due_date + ','+ completion_status)
#Notifies user task addition was successful   
            print("\nTask added!\n")
        pass

#MENU OPTION 3: viewing all tasks
    elif menu == 'va':
#Opens task file as read-only
        with open('tasks.txt','r') as task_reader:
#Splitting tasks.txt file line-by-line
#Breaking each item by comma, and assigning it to a variable
            all_tasks=task_reader.read().split('\n')
            for item in all_tasks:
                item = item.split(',')
                username = item[0]
                task_title = item[1]
                task_description = item[2]
                task_date = item[3]
                task_due_date = item[4]
                task_status = item[5]
#Outputting formatted results 
                print(f"\nAssigned User: {username}\nTask Title: {task_title}\nTask Description: {task_description}\nTask Date: {task_date}\nDate Assigned: {task_date}\nDue Date: {task_due_date}\nTask Status: {task_status}")
        pass
     
#MENU OPTION 4: View tasks relevant to user section
    elif menu == 'vm':
#Reading a file line-by-line and splitting by commas and spaces
        with open('tasks.txt','r') as task_reader:
            all_tasks=task_reader.read().split('\n')
            for item in all_tasks:
                item = item.split(',')
                username=item[0]
#Checking if username of task corresponds to user and printing the corresponding tasks
                if username == inputted_username:
                    task_title = item[1]
                    task_description = item[2]
                    task_date = item[3]
                    task_due_date = item[4]
                    task_status = item[5]
                    print(f"\nAssigned User: {username}\nTask Title: {task_title}\nTask Description: {task_description}\nTask Date: {task_date}\nDate Assigned: {task_date}\nDue Date: {task_due_date}\nTask Status: {task_status}")
        pass
    
#MENU OPTION 5: Exitting section
    elif menu == 'e':
        print('Goodbye!!!')
# Using sys module to exit loop
        sys.exit()
    else:
        print("You have made a wrong choice, Please Try again")