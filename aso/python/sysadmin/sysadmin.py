# System Admin v1.2
# Author: Mario Pereira Bermúdez
# Language: Python 3.11.6

# Libraries
import tkinter as tk # To create the GUI
import platform as pl # To get the operating system name
import pathlib as plib # To get the G
import os as os # To get the current working directory
import sys as sys # To manage the system
import subprocess as sp # To run system commands
import tempfile as tf # To create temporary files

# Frames. Dictionary to store the frames of the application
frames = {}

# Check root. Function to check if the user is root
def check_root():
    if os.getuid() != 0:
        print("You must be root to run this program")
        # If the user is not root, the program is closed
        sys.exit(1)

# Main Window. Function to create the main window of the application  
def create_main_window():  
    # Create the main window tkinter instance
    main_window = tk.Tk()
    main_window.title("System Admin v1.2")
    main_window.configure(bg="midnight blue")
    
    # Centers main window depending on OS
    os_name = pl.system()
    if os_name == 'Linux':
        # If the operating system is Linux, the main window is centered using the atributte "-zoomed"
        main_window.attributes('-zoomed', True)
    else:
        # If the operating system is not Linux, the main window is centered using the state "zoomed"
        main_window.state('zoomed')
        
    # Main window grid configuration    
    main_window.grid_rowconfigure(0, weight=3) 
    main_window.grid_rowconfigure(1, weight=2)    
    main_window.grid_columnconfigure(0, weight=1)
    main_window.update_idletasks()
    
    # Returns main window instance
    return main_window

# Main Menu Title. Function to create the main menu title of the application
def create_main_menu_title():
    # Creates the main menu title with an specific font, size, color and background color
    main_menu_title = tk.Label(main_window, text=" S y s t e m   A d m i n", font=("Arial", 90, "bold"), fg="white", bg="midnight blue", anchor="center")
    main_menu_title.grid(row=0, column=0, sticky='news')
    main_window.update_idletasks()

# Show frame. Function to show an specific frame containing either a menu or a submenu 
def show_frame(frame):
    # Gets the frame from the dictionary
    frame = frames[frame]
    # Raises the frame to the top to be shown
    frame.tkraise()
    main_window.update_idletasks()

# Main Menu. Function to create the main menu of the application   
def create_main_menu_frame():
    # Creates the main menu frame
    main_menu_frame = tk.Frame(main_window)
    main_menu_frame.configure(bg="midnight blue")
    main_menu_frame.grid(row=1, column=0, sticky='news')
    
    # Creates the main menu buttons with an specific font, size, color, background color and command
    button_users = tk.Button(main_menu_frame, text="Users", height=3, bd=0, width=20, font=("Arial", 20), command=create_users_menu_frame)
    button_users.pack(pady=20)
    button_files = tk.Button(main_menu_frame, text="Files", height=3, bd=0, width=20, font=("Arial", 20), command=create_files_menu_frame)
    button_files.pack(pady=20)
    button_processes = tk.Button(main_menu_frame, text="Processes", height=3, bd=0, width=20, font=("Arial", 20), command=create_processes_menu_frame)
    button_processes.pack(pady=20)
    button_backups = tk.Button(main_menu_frame, text="Backups", height=3, bd=0, width=20, font=("Arial", 20), command=create_backups_menu_frame)
    button_backups.pack(pady=20)
    
    main_window.update_idletasks()
    
    # Stores the main menu frame in the dictionary
    frames["main_menu_frame"] = main_menu_frame
    
# Users Submenu. Function to create the users submenu of the main menu 
def create_users_menu_frame():
    # Creates the users submenu frame
    users_menu_frame = tk.Frame(main_window)
    users_menu_frame.configure(bg="midnight blue")
    users_menu_frame.grid(row=1, column=0, sticky= 'ns')
    
    # Creates the buttons to access the different options of the users submenu
    button_create_user = tk.Button(users_menu_frame, text="Create user", height=3, bd=0, width=20, font=("Arial", 20), command=create_create_user_frame)
    button_create_user.grid(row=0, column=0, padx=20, pady=20)
    button_delete_user= tk.Button(users_menu_frame, text="Delete user", height=3, bd=0, width=20, font=("Arial", 20), command=create_delete_user_frame)
    button_delete_user.grid(row=1, column=0, padx=20, pady=20)
    button_create_user_group= tk.Button(users_menu_frame, text="Create user group", height=3, bd=0, width=20, font=("Arial", 20), command=create_create_user_group_frame)
    button_create_user_group.grid(row=2, column=0, padx=20, pady=20)
    button_change_user_group= tk.Button(users_menu_frame, text="Change user group", height=3, bd=0, width=20, font=("Arial", 20), command=create_change_user_group_frame)
    button_change_user_group.grid(row=0, column=1, padx=20, pady=20)
    button_delete_user_group= tk.Button(users_menu_frame, text="Delete user group", height=3, bd=0, width=20, font=("Arial", 20), command=create_delete_user_group_frame)
    button_delete_user_group.grid(row=1, column=1, padx=20, pady=20)
    button_go_back = tk.Button(users_menu_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("main_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
    # Stores the users submenu frame in the dictionary
    frames["users_menu_frame"] = users_menu_frame
    
# Users Submenu - Create user. Function to create the "create user panel" of the "users submenu"
def create_create_user_frame():
    # Variables to store the user creation parameters
    username = tk.StringVar()
    user_password = tk.StringVar()
    user_home = tk.StringVar()
    user_shell = tk.StringVar()
    # Create user. Function to create a new user
    def create_user(username, user_password, user_home, user_shell):
        try:
            # Runs the useradd command create a new user with the specified parameters
            sp.run(["useradd", "-m", "-d", user_home.get(), "-s", user_shell.get(), username.get()], check=True)
            # Runs the passwd command to set the password of the new user with the specified parameters
            sp.run(["passwd", username.get()], input=f"{user_password.get()}\n{user_password.get()}\n", check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to create user: {error}")
        # Resets the entry fields    
        entry_username.delete(0, tk.END)
        entry_user_password.delete(0, tk.END)
        entry_user_home.delete(0, tk.END)
        entry_user_shell.delete(0, tk.END)
        
    create_user_frame = tk.Frame(main_window)
    create_user_frame.configure(bg="midnight blue")
    create_user_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_username = tk.Label(create_user_frame, text="Username:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_username.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_username = tk.Entry(create_user_frame, font=("Arial", 20), textvariable=username, bg="white", fg="black")
    entry_username.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_user_password = tk.Label(create_user_frame, text="User password:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_user_password.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    entry_user_password = tk.Entry(create_user_frame, font=("Arial", 20), textvariable=user_password, bg="white", fg="black")
    entry_user_password.grid(row=1, column=1, sticky='news', pady=20, padx=20)
    
    label_user_home = tk.Label(create_user_frame, text="User home:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_user_home.grid(row=2, column=0, sticky='nes', pady=20, padx=20)
    entry_user_home = tk.Entry(create_user_frame, font=("Arial", 20), textvariable=user_home, bg="white", fg="black")
    entry_user_home.grid(row=2, column=1, sticky='news', pady=20, padx=20)
    
    label_user_shell = tk.Label(create_user_frame, text="User shell:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_user_shell.grid(row=3, column=0, sticky='nes', pady=20, padx=20)
    entry_user_shell = tk.Entry(create_user_frame, font=("Arial", 20), textvariable=user_shell, bg="white", fg="black")
    entry_user_shell.grid(row=3, column=1, sticky='news', pady=20, padx=20)
    
    button_create_user = tk.Button(create_user_frame, text="Create user", height=3, bd=0, width=20, font=("Arial", 20), command=lambda: create_user(username.get(), user_password.get(), user_home.get(), user_shell.get()))
    button_create_user.grid(row=4, column=0, padx=20, pady=20)
    button_go_back = tk.Button(create_user_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("users_menu_frame"))
    button_go_back.grid(row=4, column=1, padx=20, pady=20)

    main_window.update_idletasks()
        
# Users Submenu - Delete user. Function to create the "delete user panel" of the "users submenu"
def create_delete_user_frame():
    # Variable to store the username of the user to be deleted
    username = tk.StringVar()
    # Delete user. Function to delete an existing user
    def delete_user(username):
        try:
            # Deletes the user with the specified username
            sp.run(["userdel", username], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to delete user: {error}")
        # Resets the entry field
        entry_username.delete(0, tk.END)
    
    delete_user_frame = tk.Frame(main_window)
    delete_user_frame.configure(bg="midnight blue")
    delete_user_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_username = tk.Label(delete_user_frame, text="Username:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_username.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_username = tk.Entry(delete_user_frame, font=("Arial", 20), textvariable=username, bg="white", fg="black")
    entry_username.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    button_delete_user = tk.Button(delete_user_frame, text="Delete user", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: delete_user(username.get()))
    button_delete_user.grid(row=1, column=0, padx=20, pady=20)
    button_go_back = tk.Button(delete_user_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("users_menu_frame"))
    button_go_back.grid(row=1, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
# Users Submenu - Create user group. Function to create the "create user group panel" of the "users submenu"
def create_create_user_group_frame():
    # Variable to store the user group name
    user_group = tk.StringVar()
    # Create user group. Function to create a new user group
    def create_user_group(user_group):
        try:
            # Runs the groupadd command to create the user group with the specified group name
            sp.run(["groupadd", user_group], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to create user group: {error}")
        # Resets the entry field
        entry_user_group.delete(0, tk.END)
    
    create_user_group_frame = tk.Frame(main_window)
    create_user_group_frame.configure(bg="midnight blue")
    create_user_group_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_user_group = tk.Label(create_user_group_frame, text="User group:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_user_group.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_user_group = tk.Entry(create_user_group_frame, font=("Arial", 20), textvariable=user_group, bg="white", fg="black")
    entry_user_group.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    button_create_user_group = tk.Button(create_user_group_frame, text="Create user group", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: create_user_group(user_group.get()))
    button_create_user_group.grid(row=1, column=0, padx=20, pady=20)
    button_go_back = tk.Button(create_user_group_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("users_menu_frame"))
    button_go_back.grid(row=1, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
# Users Submenu - Change user group. Function to create the "change user group panel" of the "users submenu"
def create_change_user_group_frame():
    # Variables to store the username and the new user group
    username = tk.StringVar()
    user_group = tk.StringVar()
    # Change user group. Function to change the user group of an existing user
    def change_user_group(username, user_group):
        try:
            # Runs the usermod command to change the user group of the user with the specified parameters
            sp.run(["usermod", "-g", user_group, username], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to change user group: {error}")
        # Resets the entry fields
        entry_username.delete(0, tk.END)
        entry_user_group.delete(0, tk.END)
    
    change_user_group_frame = tk.Frame(main_window)
    change_user_group_frame.configure(bg="midnight blue")
    change_user_group_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_username = tk.Label(change_user_group_frame, text="Username:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_username.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_username = tk.Entry(change_user_group_frame, font=("Arial", 20), textvariable=username, bg="white", fg="black")
    entry_username.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_user_group = tk.Label(change_user_group_frame, text="User group:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_user_group.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    entry_user_group = tk.Entry(change_user_group_frame, font=("Arial", 20), textvariable=user_group, bg="white", fg="black")
    entry_user_group.grid(row=1, column=1, sticky='news', pady=20, padx=20)
    
    button_change_user_group = tk.Button(change_user_group_frame, text="Change user group", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: change_user_group(username.get(), user_group.get()))
    button_change_user_group.grid(row=2, column=0, padx=20, pady=20)
    button_go_back = tk.Button(change_user_group_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("users_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
# Users Submenu - Delete user group. Function to create the "delete user group panel" of the "users submenu"
def create_delete_user_group_frame():
    # Variable to store the user group name
    user_group = tk.StringVar()
    # Delete user group. Function to delete an existing user group
    def delete_user_group(user_group):
        try:
            # Runs the groupdel command to delete the user group with the specified group name
            sp.run(["groupdel", user_group], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to delete user group: {error}")
        entry_user_group.delete(0, tk.END)
    
    delete_user_group_frame = tk.Frame(main_window)
    delete_user_group_frame.configure(bg="midnight blue")
    delete_user_group_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_user_group = tk.Label(delete_user_group_frame, text="User group:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_user_group.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_user_group = tk.Entry(delete_user_group_frame, font=("Arial", 20), textvariable=user_group, bg="white", fg="black")
    entry_user_group.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    button_delete_user_group = tk.Button(delete_user_group_frame, text="Delete user group", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: delete_user_group(user_group.get()))
    button_delete_user_group.grid(row=1, column=0, padx=20, pady=20)
    button_go_back = tk.Button(delete_user_group_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("users_menu_frame"))
    button_go_back.grid(row=1, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()

# Files Submenu - Function to create the files submenu of the main menu
def create_files_menu_frame():
    files_menu_frame = tk.Frame(main_window)
    files_menu_frame.configure(bg="midnight blue")
    files_menu_frame.grid(row=1, column=0, sticky= 'ns')
    
    # Creates the buttons to access the different options of the files submenu
    button_copy_file = tk.Button(files_menu_frame, text="Copy file", height=3, bd=0, width=20, font=("Arial", 20), command=create_copy_file_frame)
    button_copy_file.grid(row=0, column=0, padx=20, pady=20)
    button_move_file= tk.Button(files_menu_frame, text="Move file", height=3, bd=0, width=20, font=("Arial", 20), command=create_move_file_frame)
    button_move_file.grid(row=1, column=0, padx=20, pady=20)
    button_show_file_content= tk.Button(files_menu_frame, text="Show file content", height=3, bd=0, width=20, font=("Arial", 20), command=create_show_file_content_frame)
    button_show_file_content.grid(row=2, column=0, padx=20, pady=20)
    button_delete_file= tk.Button(files_menu_frame, text="Delete file", height=3, bd=0, width=20, font=("Arial", 20), command=create_delete_file_frame)
    button_delete_file.grid(row=3, column=0, padx=20, pady=20)
    button_change_file_permissions= tk.Button(files_menu_frame, text="Change file permissions", height=3, bd=0, width=20, font=("Arial", 20), command=create_change_file_permissions_frame)
    button_change_file_permissions.grid(row=0, column=1, padx=20, pady=20)
    button_change_file_owner= tk.Button(files_menu_frame, text="Change file owner", height=3, bd=0, width=20, font=("Arial", 20), command=create_change_file_owner_frame)
    button_change_file_owner.grid(row=1, column=1, padx=20, pady=20)
    button_change_file_group= tk.Button(files_menu_frame, text="Change file group", height=3, bd=0, width=20, font=("Arial", 20), command=create_change_file_group_frame)
    button_change_file_group.grid(row=2, column=1, padx=20, pady=20)
    button_go_back = tk.Button(files_menu_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("main_menu_frame"))
    button_go_back.grid(row=3, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
    frames["files_menu_frame"] = files_menu_frame
    
# Files Submenu - Copy file. Function to create the "copy file panel" of the "files submenu"
def create_copy_file_frame():
    # Variables to store the source file and the destination file
    source_file = tk.StringVar()
    destination_file = tk.StringVar()
    # Copy file. Function to copy a file
    def copy_file(source_file, destination_file):
        try:
            # Runs the cp command to copy the file with the specified parameters
            sp.run(["cp", source_file, destination_file], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to copy file: {error}")
        # Resets the entry fields
        entry_source_file.delete(0, tk.END)
        entry_source_file.insert(0, home)
        entry_destination_file.delete(0, tk.END)
        entry_destination_file.insert(0, home)
    # Gets the user home directory        
    home = plib.Path.home()
            
    copy_file_frame = tk.Frame(main_window)
    copy_file_frame.configure(bg="midnight blue")
    copy_file_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_source_file = tk.Label(copy_file_frame, text="Source file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_file.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_source_file = tk.Entry(copy_file_frame, font=("Arial", 20), textvariable=source_file,bg="white", fg="black")
    entry_source_file.insert(0, home)
    entry_source_file.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_destination_file = tk.Label(copy_file_frame, text="Destination file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_destination_file.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    entry_destination_file = tk.Entry(copy_file_frame, font=("Arial", 20), textvariable=destination_file,bg="white", fg="black")
    entry_destination_file.insert(0, home)
    entry_destination_file.grid(row=1, column=1, sticky='news', pady=20, padx=20)
    
    button_copy_file = tk.Button(copy_file_frame, text="Copy file", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: copy_file(source_file.get(), destination_file.get()))
    button_copy_file.grid(row=2, column=0, padx=20, pady=20)
    button_go_back = tk.Button(copy_file_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
# Files Submenu - Move file. Function to create the "move file panel" of the "files submenu"
def create_move_file_frame():
    # Variables to store the source path and the destination path
    source_path = tk.StringVar()
    destination_path = tk.StringVar()
    # Move file. Function to move a file
    def move_file(source_path, destination_path):
        try:
            # Runs the mv command to move the specified file
            sp.run(["mv", source_path, destination_path], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to move file: {error}")
        # Resets the entry fields
        entry_source_path.delete(0, tk.END)
        entry_source_path.insert(0, home)
        entry_destination_path.delete(0, tk.END)
        entry_destination_path.insert(0, home)
    # Gets the user home directory
    home = plib.Path.home()
    
    move_file_frame = tk.Frame(main_window)
    move_file_frame.configure(bg="midnight blue")
    move_file_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_source_path = tk.Label(move_file_frame, text="Source path:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_path.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_source_path = tk.Entry(move_file_frame, font=("Arial", 20), textvariable=source_path, bg="white", fg="black")
    entry_source_path.insert(0, home)
    entry_source_path.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_destination_path = tk.Label(move_file_frame, text="Destination path:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_destination_path.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    entry_destination_path = tk.Entry(move_file_frame, font=("Arial", 20), textvariable=destination_path, bg="white", fg="black")
    entry_destination_path.insert(0, home)
    entry_destination_path.grid(row=1, column=1, sticky='news', pady=20, padx=20)
    
    button_move_file = tk.Button(move_file_frame, text="Move file", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: move_file(source_path.get(), destination_path.get()))
    button_move_file.grid(row=2, column=0, padx=20, pady=20)
    button_go_back = tk.Button(move_file_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
# Files Submenu - Show file content. Function to create the "show file content panel" of the "files submenu"    
def create_show_file_content_frame():
    # Variable to store the source file
    source_file = tk.StringVar()
    # Show file content. Function to show the content of a file
    def show_file_content(source_file):
        try:
            # Runs the cat command to show the content of the specified file
            sp.run(["cat", source_file], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to show file content: {error}")
        entry_source_file.delete(0, tk.END)
        entry_source_file.insert(0, home)
    # Gets the user home directory        
    home = plib.Path.home()
    
    show_file_content_frame = tk.Frame(main_window)
    show_file_content_frame.configure(bg="midnight blue")
    show_file_content_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_source_file = tk.Label(show_file_content_frame, text="Source file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_file.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_source_file = tk.Entry(show_file_content_frame, font=("Arial", 20), textvariable=source_file, bg="white", fg="black")
    entry_source_file.insert(0, home)
    entry_source_file.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    button_show_file_content = tk.Button(show_file_content_frame, text="Show file content", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_file_content(source_file.get()))
    button_show_file_content.grid(row=1, column=0, padx=20, pady=20)
    button_go_back = tk.Button(show_file_content_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=1, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
# Files Submenu - Delete file. Function to create the "delete file panel" of the "files submenu"
def create_delete_file_frame():
    # Variable to store the source file
    source_file = tk.StringVar()
    # Delete file. Function to delete a file
    def delete_file(source_file):
        try:
            # Runs the rm command to delete the specified file
            sp.run(["rm", source_file], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to delete file: {error}")
        # Resets the entry fields
        entry_source_file.delete(0, tk.END)
        entry_source_file.insert(0, home)
    # Gets the user home directory
    home = plib.Path.home()
    
    delete_file_frame = tk.Frame(main_window)
    delete_file_frame.configure(bg="midnight blue")
    delete_file_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_source_file = tk.Label(delete_file_frame, text="Source file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_file.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_source_file = tk.Entry(delete_file_frame, font=("Arial", 20), textvariable=source_file, bg="white", fg="black")
    entry_source_file.insert(0, home)
    entry_source_file.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    button_delete_file = tk.Button(delete_file_frame, text="Delete file", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: delete_file(source_file.get()))
    button_delete_file.grid(row=1, column=0, padx=20, pady=20)
    button_go_back = tk.Button(delete_file_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=1, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
# Files Submenu - Change file permissions. Function to create the "change file permissions panel" of the "files submenu"    
def create_change_file_permissions_frame():
    # Variables to store the source file and the new file permissions
    source_file = tk.StringVar()
    user_permissions = tk.StringVar()
    group_permissions = tk.StringVar()
    other_permissions = tk.StringVar()
    # Change file permissions. Function to change the permissions of a file
    def change_file_permissions(source_file, user_permissions, group_permissions, other_permissions):
        try:
            # Runs the chmod command to change the permissions of the file with the specified parameters
            sp.run(["chmod", f"{user_permissions}{group_permissions}{other_permissions}", source_file], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to change file permissions: {error}")
        # Resets the entry fields   
        entry_source_file.delete(0, tk.END)
        entry_source_file.insert(0, home)
        entry_user_permissions.delete(0, tk.END)
        entry_group_permissions.delete(0, tk.END)
        entry_other_permissions.delete(0, tk.END)
    # Gets the user home directory      
    home = plib.Path.home()

    change_file_permissions_frame = tk.Frame(main_window)
    change_file_permissions_frame.configure(bg="midnight blue")
    change_file_permissions_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_source_file = tk.Label(change_file_permissions_frame, text="Source file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_file.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_source_file = tk.Entry(change_file_permissions_frame, font=("Arial", 20), textvariable=source_file, bg="white", fg="black")
    entry_source_file.insert(0, home)
    entry_source_file.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_user_permissions = tk.Label(change_file_permissions_frame, text="User permissions:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_user_permissions.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    entry_user_permissions = tk.Entry(change_file_permissions_frame, font=("Arial", 20), textvariable=user_permissions, width=1, bg="white", fg="black")
    entry_user_permissions.grid(row=1, column=1, sticky='nws', pady=20, padx=20)
    
    label_group_permissions = tk.Label(change_file_permissions_frame, text="Group permissions:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_group_permissions.grid(row=2, column=0, sticky='nes', pady=20, padx=20)
    entry_group_permissions = tk.Entry(change_file_permissions_frame, font=("Arial", 20), textvariable=group_permissions, width=1, bg="white", fg="black")
    entry_group_permissions.grid(row=2, column=1, sticky='nws', pady=20, padx=20)
    
    label_other_permissions = tk.Label(change_file_permissions_frame, text="Other permissions:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_other_permissions.grid(row=3, column=0, sticky='nes', pady=20, padx=20)
    entry_other_permissions = tk.Entry(change_file_permissions_frame, font=("Arial", 20), textvariable=other_permissions, width=1, bg="white", fg="black")
    entry_other_permissions.grid(row=3, column=1, sticky='nws', pady=20, padx=20)
    
    button_change_file_permissions = tk.Button(change_file_permissions_frame, text="Change file permissions", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: change_file_permissions(source_file.get(), user_permissions.get(), group_permissions.get(), other_permissions.get()))
    button_change_file_permissions.grid(row=4, column=0, padx=20, pady=20)
    button_go_back = tk.Button(change_file_permissions_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=4, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
  
# Files Submenu - Change file owner. Function to create the "change file owner panel" of the "files submenu"    
def create_change_file_owner_frame():
    # Variables to store the source file and the new file owner
    source_file = tk.StringVar()
    new_file_owner = tk.StringVar()
    # Change file owner. Function to change the owner of a file
    def change_file_owner(source_file, new_file_owner):
        try:
            # Runs the chown command to change the owner of the specified file
            sp.run(["chown", new_file_owner, source_file], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to change file owner: {error}")
        # Resets the entry fields    
        entry_source_file.delete(0, tk.END)
        entry_source_file.insert(0, home)
        entry_new_file_owner.delete(0, tk.END)
    # G   
    home = plib.Path.home() 
    
    change_file_owner_frame = tk.Frame(main_window)
    change_file_owner_frame.configure(bg="midnight blue")
    change_file_owner_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_source_file = tk.Label(change_file_owner_frame, text="Source file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_file.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_source_file = tk.Entry(change_file_owner_frame, font=("Arial", 20), textvariable=source_file, bg="white", fg="black")
    entry_source_file.insert(0, home)
    entry_source_file.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_new_file_owner = tk.Label(change_file_owner_frame, text="New file owner:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_new_file_owner.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    entry_new_file_owner = tk.Entry(change_file_owner_frame, font=("Arial", 20), textvariable=new_file_owner, bg="white", fg="black")
    entry_new_file_owner.grid(row=1, column=1, sticky='news', pady=20, padx=20)
    
    button_change_file_owner = tk.Button(change_file_owner_frame, text="Change file owner", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: change_file_owner(source_file.get(), new_file_owner.get()))
    button_change_file_owner.grid(row=2, column=0, padx=20, pady=20)
    button_go_back = tk.Button(change_file_owner_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
# Files Submenu - Change file group. Function to create the "change file group panel" of the "files submenu"
def create_change_file_group_frame():
    # Variable to store the source file and the new file group
    source_file = tk.StringVar()
    new_file_group = tk.StringVar()
    # Change file group. Function to change the group of a file
    def change_file_group(source_file, new_file_group):
        try:
            # Runs the chgrp command to change the group of the specified file
            sp.run(["chgrp", new_file_group, source_file], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to change file group: {error}")
        # Resets the entry fields
        entry_source_file.delete(0, tk.END)
        entry_source_file.insert(0, home)
        entry_new_file_group.delete(0, tk.END)
    # Gets the user home directory   
    home = plib.Path.home()
    
    change_file_group_frame = tk.Frame(main_window)
    change_file_group_frame.configure(bg="midnight blue")
    change_file_group_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_source_file = tk.Label(change_file_group_frame, text="Source file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_file.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_source_file = tk.Entry(change_file_group_frame, font=("Arial", 20), textvariable=source_file, bg="white", fg="black")
    entry_source_file.insert(0, home)
    entry_source_file.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_new_file_group = tk.Label(change_file_group_frame, text="New file group:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_new_file_group.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    entry_new_file_group = tk.Entry(change_file_group_frame, font=("Arial", 20), textvariable=new_file_group, bg="white", fg="black")
    entry_new_file_group.grid(row=1, column=1, sticky='news', pady=20, padx=20)
    
    button_change_file_group = tk.Button(change_file_group_frame, text="Change file group", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: change_file_group(source_file.get(), new_file_group.get()))
    button_change_file_group.grid(row=2, column=0, padx=20, pady=20)
    button_go_back = tk.Button(change_file_group_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()

# Processes Menu. Function to create the processes submenu of the main menu
def create_processes_menu_frame():
    processes_menu_frame = tk.Frame(main_window)
    processes_menu_frame.configure(bg="midnight blue")
    processes_menu_frame.grid(row=1, column=0, sticky= 'ns')
    
    # Creates the buttons to access the different options of the processes submenu
    button_show_processes = tk.Button(processes_menu_frame, text="Show processes", height=3, bd=0, width=20, font=("Arial", 20), command=create_show_processes_frame)
    button_show_processes.grid(row=0, column=0, padx=20, pady=20)
    button_change_process_priority = tk.Button(processes_menu_frame, text="Change process priority", height=3, bd=0, width=20, font=("Arial", 20), command=create_change_process_priority_frame)
    button_change_process_priority.grid(row=1, column=0, padx=20, pady=20)
    button_kill_process = tk.Button(processes_menu_frame, text="Kill process", height=3, bd=0, width=20, font=("Arial", 20), command=create_kill_process_frame)
    button_kill_process.grid(row=0, column=1, padx=20, pady=20)
    button_go_back = tk.Button(processes_menu_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("main_menu_frame"))
    button_go_back.grid(row=1, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
    # Stores the processes submenu frame in the frames dictionary
    frames["processes_menu_frame"] = processes_menu_frame
    
# Processes Submenu - Show processes. Function to create the "show processes panel" of the "processes submenu"
def create_show_processes_frame():
    # Show processes. Function to show the processes running in the system
    def show_processes():
        try:
            # Runs the ps aux command to show the processes running in the system
            sp.run(["ps", "aux"], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to show processes: {error}")
            
    show_processes_frame = tk.Frame(main_window)
    show_processes_frame.configure(bg="midnight blue")
    show_processes_frame.grid(row=1, column=0, sticky= 'ns')
    
    button_show_processes = tk.Button(show_processes_frame, text="Show processes", height=3, bd=0, width=20, font=("Arial", 20), command=show_processes)
    button_show_processes.grid(row=0, column=0, padx=20, pady=20)
    button_go_back = tk.Button(show_processes_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("processes_menu_frame"))
    button_go_back.grid(row=0, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
# Processes Submenu - Change process priority. Function to create the "change process priority panel" of the "processes submenu"
def create_change_process_priority_frame():
    # Variable to store the process name
    process_name = tk.StringVar()
    new_process_priority = tk.StringVar()
    # Change process priority. Function to change the priority of a process
    def change_process_priority(process_name, new_process_priority):
        try:
            try:
                # Gets the operating system name
                os_name = pl.system()
                if os_name == "Linux":
                    # If the operating system is Linux, gets the process ID using the pidof command
                    process_id = sp.run(["pidof", process_name], capture_output=True, text=True, check=True).stdout.strip()
                else:
                    # If the operating system is not Linux, gets the process ID using the pgrep command
                    process_id = sp.run(["pgrep", process_name], capture_output=True, text=True, check=True).stdout.strip() 
            except sp.CalledProcessError as error:
                print(f"Error getting process ID: {error}")
            else:
                # Changes the process priority using the renice command
                sp.run(["renice", new_process_priority, process_id], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to change process priority: {error}")
        # Resets the entry fields    
        entry_process_name.delete(0, tk.END)
            
    change_process_priority_frame = tk.Frame(main_window)
    change_process_priority_frame.configure(bg="midnight blue")
    change_process_priority_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_process_name = tk.Label(change_process_priority_frame, text="Process name:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_process_name.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_process_name = tk.Entry(change_process_priority_frame, font=("Arial", 20), textvariable=process_name, bg="white", fg="black")
    entry_process_name.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_new_process_priority = tk.Label(change_process_priority_frame, text="New process priority:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_new_process_priority.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    entry_new_process_priority = tk.Entry(change_process_priority_frame, font=("Arial", 20), textvariable=new_process_priority, width=2, bg="white", fg="black")
    entry_new_process_priority.grid(row=1, column=1, sticky='nws', pady=20, padx=20)
    
    button_change_process_priority = tk.Button(change_process_priority_frame, text="Change process priority", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: change_process_priority(process_name.get(), new_process_priority.get()))
    button_change_process_priority.grid(row=2, column=0, padx=20, pady=20)
    button_go_back = tk.Button(change_process_priority_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("processes_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)

    main_window.update_idletasks()
    
# Processes Submenu - Kill process. Function to create the "kill process panel" of the "processes submenu"
def create_kill_process_frame():
    # Variable to store the process name
    process_name = tk.StringVar()
    # Kill process. Function to kill a process
    def kill_process(process_name):
        try:
            try:
                # Gets the operating system name
                os_name = pl.system()
                if os_name == "Linux":
                    # If the operating system is Linux, gets the process ID using the pidof command
                    process_id = sp.run(["pidof", process_name], capture_output=True, text=True, check=True).stdout.strip()
                else:
                    # If the operating system is not Linux, gets the process ID using the pgrep command
                    process_id = sp.run(["pgrep", process_name], capture_output=True, text=True, check=True).stdout.strip()
            except sp.CalledProcessError as error:
                print(f"Error getting process ID: {error}")
            else:
                # Runs the kill command to kill the process with the specified process ID
                sp.run(["kill", "-9", process_id], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to kill process: {error}")
        # Resets the entry field
        entry_process_name.delete(0, tk.END)
            
    kill_process_frame = tk.Frame(main_window)
    kill_process_frame.configure(bg="midnight blue")
    kill_process_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_process_name = tk.Label(kill_process_frame, text="Process name:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_process_name.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_process_name = tk.Entry(kill_process_frame, font=("Arial", 20), textvariable=process_name, bg="white", fg="black")
    entry_process_name.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    button_kill_process = tk.Button(kill_process_frame, text="Kill process", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: kill_process(process_name.get()))
    button_kill_process.grid(row=1, column=0, padx=20, pady=20)
    button_go_back = tk.Button(kill_process_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("processes_menu_frame"))
    button_go_back.grid(row=1, column=1, padx=20, pady=20)

    main_window.update_idletasks()

# Backups Menu. Function to create the backups submenu of the main menu
def create_backups_menu_frame():
    backups_menu_frame = tk.Frame(main_window)
    backups_menu_frame.configure(bg="midnight blue")
    backups_menu_frame.grid(row=1, column=0, sticky= 'ns')
    
    # Creates the buttons to access the different options of the backups submenu
    button_create_backup = tk.Button(backups_menu_frame, text="Create backup", height=3, bd=0, width=20, font=("Arial", 20), command=create_create_backup_frame)
    button_create_backup.grid(row=0, column=0, padx=20, pady=20)
    button_extract_backup = tk.Button(backups_menu_frame, text="Extract backup", height=3, bd=0, width=20, font=("Arial", 20), command=create_extract_backup_frame)
    button_extract_backup.grid(row=1, column=0, padx=20, pady=20)
    button_create_backup_crontab = tk.Button(backups_menu_frame, text="Create backup crontab", height=3, bd=0, width=20, font=("Arial", 20), command=create_create_backup_crontab)
    button_create_backup_crontab.grid(row=0, column=1, padx=20, pady=20)
    button_delete_backup_crontab = tk.Button(backups_menu_frame, text="Delete backup crontab", height=3, bd=0, width=20, font=("Arial", 20), command=create_delete_backup_crontab)
    button_delete_backup_crontab.grid(row=1, column=1, padx=20, pady=20)
    button_go_back = tk.Button(backups_menu_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("main_menu_frame"))
    button_go_back.grid(row=2, column=0, padx=20, pady=20)
    
    main_window.update_idletasks()
    
    # Stores the backups submenu frame in the frames dictionary
    frames["backups_menu_frame"] = backups_menu_frame
    
# Backups - Create backup. Function to create the "create backup panel" of the "backups submenu"
def create_create_backup_frame():
    # Variables to store the source and destination paths
    source_path = tk.StringVar()
    destination_path = tk.StringVar()
    # Create backup. Function to create a backup
    def create_backup(source_path, destination_path):
        try:
            # Runs the tar command to create a backup of the specified file
            sp.run(["tar", "-cvf", destination_path, source_path], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to create backup: {error}")
        # Resets the entry fields
        entry_source_path.delete(0, tk.END)
        entry_source_path.insert(0, home)
        entry_destination_path.delete(0, tk.END)
        entry_destination_path.insert(0, home)
    # Gets the user home directory      
    home = plib.Path.home() 

    create_backup_frame = tk.Frame(main_window)
    create_backup_frame.configure(bg="midnight blue")
    create_backup_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_source_path = tk.Label(create_backup_frame, text="Source path:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_path.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_source_path = tk.Entry(create_backup_frame, font=("Arial", 20), textvariable=source_path, bg="white", fg="black")
    entry_source_path.insert(0, home)
    entry_source_path.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_destination_path = tk.Label(create_backup_frame, text="Destination path:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_destination_path.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    entry_destination_path = tk.Entry(create_backup_frame, font=("Arial", 20), textvariable=destination_path, bg="white", fg="black")
    entry_destination_path.insert(0, home)
    entry_destination_path.grid(row=1, column=1, sticky='news', pady=20, padx=20)
    
    button_create_backup = tk.Button(create_backup_frame, text="Create backup", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: create_backup(source_path.get(), destination_path.get()))
    button_create_backup.grid(row=2, column=0, padx=20, pady=20)
    button_go_back = tk.Button(create_backup_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("backups_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
# Backups Submenu - Extract backup. Function to create the "extract backup panel" of the "backups submenu"
def create_extract_backup_frame():
    # Variables to store the source and destination paths
    source_path = tk.StringVar()
    destination_path = tk.StringVar()
    # Extract backup. Function to extract a backup
    def extract_backup(source_path, destination_path):
        try:
            # Runs the tar command to extract the specified backup
            sp.run(["tar", "-xvf", source_path, "-C", destination_path], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to extract backup: {error}")
        # Resets the entry fields    
        entry_source_path.delete(0, tk.END)
        entry_source_path.insert(0, home)
        entry_destination_path.delete(0, tk.END)
        entry_destination_path.insert(0, home)
    # Gets the user home directory     
    home = plib.Path.home() 
    
    extract_backup_frame = tk.Frame(main_window)
    extract_backup_frame.configure(bg="midnight blue")
    extract_backup_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_source_path = tk.Label(extract_backup_frame, text="Source path:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_path.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_source_path = tk.Entry(extract_backup_frame, font=("Arial", 20), textvariable=source_path, bg="white", fg="black")
    entry_source_path.insert(0, home)
    entry_source_path.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_destination_path = tk.Label(extract_backup_frame, text="Destination path:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_destination_path.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    entry_destination_path = tk.Entry(extract_backup_frame, font=("Arial", 20), textvariable=destination_path, bg="white", fg="black")
    entry_destination_path.insert(0, home)
    entry_destination_path.grid(row=1, column=1, sticky='news', pady=20, padx=20)
    
    button_extract_backup = tk.Button(extract_backup_frame, text="Extract backup", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: extract_backup(source_path.get(), destination_path.get()))
    button_extract_backup.grid(row=2, column=0, padx=20, pady=20)
    button_go_back = tk.Button(extract_backup_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("backups_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
# Backups Submenu - Create backup crontab. Function to create the "create backup crontab panel" of the "backups submenu"
def create_create_backup_crontab():
    # Variables to store the crontab configuration
    crontab_minute = tk.StringVar()
    crontab_hour = tk.StringVar()
    crontab_day_of_month = tk.StringVar()
    crontab_month = tk.StringVar()
    crontab_day_of_week = tk.StringVar()
    crontab_command = tk.StringVar()
    # Create backup crontab. Function to create a backup using crontab
    def create_backup_crontab(crontab_minute, crontab_hour, crontab_day_of_month, crontab_month, crontab_day_of_week, crontab_command):
        crontab_entry = f"{crontab_minute} {crontab_hour} {crontab_day_of_month} {crontab_month} {crontab_day_of_week} {crontab_command}\n"
        # Creates a temporary file to store the crontab entry 
        with tf.NamedTemporaryFile(mode='w+t', delete=False) as file:
            try:
                # Tries to get the current crontab and write it to the temporary file
                sp.run(['crontab', '-l'], stdout=file, check=True)
            except sp.CalledProcessError as e:
                # If the user does not have a crontab, ignore the error
                if e.returncode != 1:
                    raise
            # Writes the new crontab entry to the temporary file
            file.write(crontab_entry)
            # Saves the temporary file name
            temp_file_name = file.name
        # Tries to load the temporary file as the new crontab
        try:
            sp.run(['crontab', temp_file_name], check=True)
        except sp.CalledProcessError as e:
            print(f"Error updating crontab: {e}")
        # Resets the entry fields
        entry_crontab_minute.delete(0, tk.END)
        entry_crontab_hour.delete(0, tk.END)
        entry_crontab_day_of_month.delete(0, tk.END)
        entry_crontab_month.delete(0, tk.END)
        entry_crontab_day_of_week.delete(0, tk.END)
        entry_crontab_command.delete(0, tk.END)
        entry_crontab_command.insert(0, f"tar cvf {home} {home}")
    # Gets the user home directory  
    home = plib.Path.home()
    
    main_window.grid_rowconfigure(1, weight=0)
    create_backup_crontab_frame = tk.Frame(main_window)
    create_backup_crontab_frame.configure(bg="midnight blue")
    create_backup_crontab_frame.grid(row=1, column=0, sticky= 'ns')
    
    label_crontab_minute = tk.Label(create_backup_crontab_frame, text="Crontab minute:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_crontab_minute.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    entry_crontab_minute = tk.Entry(create_backup_crontab_frame, font=("Arial", 20), textvariable=crontab_minute, width=2, bg="white", fg="black")
    entry_crontab_minute.grid(row=0, column=1, sticky='nws', pady=20, padx=20)
    
    label_crontab_hour = tk.Label(create_backup_crontab_frame, text="Crontab hour:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_crontab_hour.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    entry_crontab_hour = tk.Entry(create_backup_crontab_frame, font=("Arial", 20), textvariable=crontab_hour, width=2, bg="white", fg="black")
    entry_crontab_hour.grid(row=1, column=1, sticky='nws', pady=20, padx=20)
    
    label_crontab_day_of_month = tk.Label(create_backup_crontab_frame, text="Crontab day of month:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_crontab_day_of_month.grid(row=2, column=0, sticky='nes', pady=20, padx=20)
    entry_crontab_day_of_month = tk.Entry(create_backup_crontab_frame, font=("Arial", 20), textvariable=crontab_day_of_month, width=2, bg="white", fg="black")
    entry_crontab_day_of_month.grid(row=2, column=1, sticky='nws', pady=20, padx=20)
    
    label_crontab_month = tk.Label(create_backup_crontab_frame, text="Crontab month:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_crontab_month.grid(row=3, column=0, sticky='nes', pady=20, padx=20)
    entry_crontab_month = tk.Entry(create_backup_crontab_frame, font=("Arial", 20), textvariable=crontab_month, width=2, bg="white", fg="black")
    entry_crontab_month.grid(row=3, column=1, sticky='nws', pady=20, padx=20)
    
    label_crontab_day_of_week = tk.Label(create_backup_crontab_frame, text="Crontab day of week:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_crontab_day_of_week.grid(row=4, column=0, sticky='nes', pady=20, padx=20)
    entry_crontab_day_of_week = tk.Entry(create_backup_crontab_frame, font=("Arial", 20), textvariable=crontab_day_of_week, width=2, bg="white", fg="black")
    entry_crontab_day_of_week.grid(row=4, column=1, sticky='nws', pady=20, padx=20)
    
    label_crontab_command = tk.Label(create_backup_crontab_frame, text="Crontab command:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_crontab_command.grid(row=5, column=0, sticky='nes', pady=20, padx=20)
    entry_crontab_command = tk.Entry(create_backup_crontab_frame, font=("Arial", 20), textvariable=crontab_command, bg="white", fg="black")
    entry_crontab_command.insert(0, f"tar cvf {home} {home}")
    entry_crontab_command.grid(row=5, column=1, sticky='news', pady=20, padx=20)
    
    button_create_backup_crontab = tk.Button(create_backup_crontab_frame, text="Create backup crontab", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: create_backup_crontab(crontab_minute.get(), crontab_hour.get(), crontab_day_of_month.get(), crontab_month.get(), crontab_day_of_week.get(), crontab_command.get()))
    button_create_backup_crontab.grid(row=6, column=0, padx=20, pady=20)
    button_go_back = tk.Button(create_backup_crontab_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("backups_menu_frame"))
    button_go_back.grid(row=6, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
# Backups Submenu - Delete backup crontab. Function to create the "delete backup crontab panel" of the "backups submenu"
def create_delete_backup_crontab():
    # Delete backup crontab. Function to delete the current backup crontab
    def delete_backup_crontab():
        try:
            # Runs the crontab command to delete the current backup crontab
            sp.run(["crontab", "-r"], check=True)
        except sp.CalledProcessError as error:
            print(f"Error trying to delete backup crontab: {error}")
            
    delete_backup_crontab_frame = tk.Frame(main_window)
    delete_backup_crontab_frame.configure(bg="midnight blue")
    delete_backup_crontab_frame.grid(row=1, column=0, sticky= 'ns')
    
    button_delete_backup_crontab = tk.Button(delete_backup_crontab_frame, text="Delete backup crontab", height=3, bd=0, width=20, font=("Arial", 20), command=delete_backup_crontab)
    button_delete_backup_crontab.grid(row=0, column=0, padx=20, pady=20)
    button_go_back = tk.Button(delete_backup_crontab_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("backups_menu_frame"))
    button_go_back.grid(row=0, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
check_root()

# Stores the window created by the create_main_window function on the main_window variable
main_window = create_main_window()

create_main_menu_title()
create_main_menu_frame()

# Execute the main loop of the main window
main_window.mainloop()