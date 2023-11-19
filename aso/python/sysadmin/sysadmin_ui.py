import tkinter as tk
    
# Users 
def create_users_menu_frame():
    main_menu_frame.pack_forget()
    files_menu_frame.pack_forget()
    processes_menu_frame.pack_forget()
    backups_menu_frame.pack_forget()
    main_menu_frame.pack_forget()
    users_menu_frame.configure(bg="midnight blue")
    users_menu_frame.pack()
    
    button_create_user = tk.Button(users_menu_frame, text="Create user", height=3, bd=0, width=20, font=("Arial", 20))
    button_create_user.grid(row=0, column=0, padx=20, pady=20)
    
    button_delete_user= tk.Button(users_menu_frame, text="Delete user", height=3, bd=0, width=20, font=("Arial", 20))
    button_delete_user.grid(row=1, column=0, padx=20, pady=20)
    
    button_create_user_group= tk.Button(users_menu_frame, text="Create user group", height=3, bd=0, width=20, font=("Arial", 20))
    button_create_user_group.grid(row=2, column=0, padx=20, pady=20)
    
    button_change_user_group= tk.Button(users_menu_frame, text="Change user group", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_user_group.grid(row=0, column=1, padx=20, pady=20)
    
    button_delete_user_group= tk.Button(users_menu_frame, text="Delete user group", height=3, bd=0, width=20, font=("Arial", 20))
    button_delete_user_group.grid(row=1, column=1, padx=20, pady=20)

# Files
def create_files_menu_frame():
    users_menu_frame.pack_forget()
    processes_menu_frame.pack_forget()
    backups_menu_frame.pack_forget()
    main_menu_frame.pack_forget()
    files_menu_frame.configure(bg="midnight blue")
    files_menu_frame.pack()
    
    button_copy_file = tk.Button(files_menu_frame, text="Copy file", height=3, bd=0, width=20, font=("Arial", 20))
    button_copy_file.grid(row=0, column=0, padx=20, pady=20)
    
    button_move_file= tk.Button(files_menu_frame, text="Move file", height=3, bd=0, width=20, font=("Arial", 20))
    button_move_file.grid(row=1, column=0, padx=20, pady=20)
    
    button_show_file_content= tk.Button(files_menu_frame, text="Show file content", height=3, bd=0, width=20, font=("Arial", 20))
    button_show_file_content.grid(row=2, column=0, padx=20, pady=20)
    
    button_delete_file= tk.Button(files_menu_frame, text="Delete file", height=3, bd=0, width=20, font=("Arial", 20))
    button_delete_file.grid(row=3, column=0, padx=20, pady=20)
    
    button_change_file_permissions= tk.Button(files_menu_frame, text="Change file permissions", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_file_permissions.grid(row=0, column=1, padx=20, pady=20)
    
    button_change_file_owner= tk.Button(files_menu_frame, text="Change file owner", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_file_owner.grid(row=1, column=1, padx=20, pady=20)
    
    button_change_file_group= tk.Button(files_menu_frame, text="Change file group", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_file_group.grid(row=2, column=1, padx=20, pady=20)

# Processes
def create_processes_menu_frame():
    users_menu_frame.pack_forget()
    files_menu_frame.pack_forget()
    backups_menu_frame.pack_forget()
    main_menu_frame.pack_forget()
    processes_menu_frame.configure(bg="midnight blue")
    processes_menu_frame.pack()
    
    button_show_processes = tk.Button(processes_menu_frame, text="Show processes", height=3, bd=0, width=20, font=("Arial", 20))
    button_show_processes.pack(pady=20)
    
    button_change_process_priority = tk.Button(processes_menu_frame, text="Change process priority", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_process_priority.pack(pady=20)
    
    button_kill_process = tk.Button(processes_menu_frame, text="Kill process", height=3, bd=0, width=20, font=("Arial", 20))
    button_kill_process.pack(pady=20)

# Backups
def create_backups_menu_frame():
    users_menu_frame.pack_forget()
    files_menu_frame.pack_forget()
    processes_menu_frame.pack_forget()
    main_menu_frame.pack_forget()
    backups_menu_frame.configure(bg="midnight blue")
    backups_menu_frame.pack()
    
    button_create_backup = tk.Button(backups_menu_frame, text="Create backup", height=3, bd=0, width=20, font=("Arial", 20))
    button_create_backup.pack(pady=20)
    
    button_extract_backup = tk.Button(backups_menu_frame, text="Extract backup", height=3, bd=0, width=20, font=("Arial", 20))
    button_extract_backup.pack(pady=20)
    
    button_create_backup_crontab = tk.Button(backups_menu_frame, text="Create backup crontab", height=3, bd=0, width=20, font=("Arial", 20))
    button_create_backup_crontab.pack(pady=20)
    
    button_delete_backup_crontab = tk.Button(backups_menu_frame, text="Delete backup crontab", height=3, bd=0, width=20, font=("Arial", 20))
    button_delete_backup_crontab.pack(pady=20)
    
# Main Window    
main_window = tk.Tk()
main_window.title("Sys Admin v1")
main_window.configure(bg="midnight blue")
main_window.update_idletasks()
main_window.state('zoomed')
main_window.resizable(False, False)

main_menu_title = tk.Label(main_window, text=" S y s t e m   A d m i n", font=("Arial", 90, "bold"), fg="white", width=400, height=3, anchor="center")
main_menu_title.configure(bg="midnight blue")
main_menu_title.pack()

users_menu_frame = tk.Frame(main_window)
files_menu_frame = tk.Frame(main_window)
processes_menu_frame = tk.Frame(main_window)
backups_menu_frame = tk.Frame(main_window)

# Main Menu Buttons
main_menu_frame = tk.Frame(main_window)
main_menu_frame.configure(bg="midnight blue")
main_menu_frame.pack()

button_users = tk.Button(main_menu_frame, text="Users", height=3, bd=0, width=20, font=("Arial", 20), command=create_users_menu_frame)
button_users.pack(pady=20)
button_files = tk.Button(main_menu_frame, text="Files", height=3, bd=0, width=20, font=("Arial", 20), command=create_files_menu_frame)
button_files.pack(pady=20)
button_processes = tk.Button(main_menu_frame, text="Processes", height=3, bd=0, width=20, font=("Arial", 20), command=create_processes_menu_frame)
button_processes.pack(pady=20)
button_backups = tk.Button(main_menu_frame, text="Backups", height=3, bd=0, width=20, font=("Arial", 20), command=create_backups_menu_frame)
button_backups.pack(pady=20)

main_window.mainloop()