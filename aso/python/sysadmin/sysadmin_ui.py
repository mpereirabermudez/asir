import tkinter as tk

# Frames
frames = {}

# Show frame
def show_frame(frame):
    frame = frames[frame]
    frame.tkraise()

# Main Menu
def create_main_menu_frame():
    global main_menu_frame
    main_menu_frame = tk.Frame(main_window)
    main_menu_frame.configure(bg="midnight blue")
    main_menu_frame.grid(row=1, column=0, sticky= 'news')

    button_users = tk.Button(main_menu_frame, text="Users", height=3, bd=0, width=20, font=("Arial", 20), command=create_users_menu_frame)
    button_users.pack(pady=20)
    
    button_files = tk.Button(main_menu_frame, text="Files", height=3, bd=0, width=20, font=("Arial", 20), command=create_files_menu_frame)
    button_files.pack(pady=20)
    
    button_processes = tk.Button(main_menu_frame, text="Processes", height=3, bd=0, width=20, font=("Arial", 20), command=create_processes_menu_frame)
    button_processes.pack(pady=20)
    
    button_backups = tk.Button(main_menu_frame, text="Backups", height=3, bd=0, width=20, font=("Arial", 20), command=create_backups_menu_frame)
    button_backups.pack(pady=20)

    frames["main_menu_frame"] = main_menu_frame
    
# Users 
def create_users_menu_frame():
    users_menu_frame = tk.Frame(main_window)
    users_menu_frame.configure(bg="midnight blue")
    users_menu_frame.grid(row=1, column=0, sticky= 'news', padx=415)
    
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
    
    button_go_back = tk.Button(users_menu_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("main_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    frames["users_menu_frame"] = users_menu_frame
    show_frame("users_menu_frame")

# Files
def create_files_menu_frame():
    files_menu_frame = tk.Frame(main_window)
    files_menu_frame.configure(bg="midnight blue")
    files_menu_frame.grid(row=1, column=0, sticky= 'news', padx=415)
    
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
    
    frames["files_menu_frame"] = files_menu_frame
    show_frame("files_menu_frame")
    
# Files - Copy file 
def create_copy_file_frame():
    copy_file_frame = tk.Frame(main_window)
    copy_file_frame.configure(bg="midnight blue")
    copy_file_frame.grid(row=1, column=0, sticky= 'news', padx=415)
    
    source_file = tk.StringVar()
    destination_file = tk.StringVar()
    
    label_source_file = tk.Label(copy_file_frame, text="Source file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_file.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    
    entry_source_file = tk.Entry(copy_file_frame, font=("Arial", 20), textvariable=source_file,bg="white", fg="black")
    entry_source_file.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_destination_file = tk.Label(copy_file_frame, text="Destination file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_destination_file.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    
    entry_destination_file = tk.Entry(copy_file_frame, font=("Arial", 20), textvariable=destination_file,bg="white", fg="black")
    entry_destination_file.grid(row=1, column=1, sticky='news', pady=20, padx=20)
    
    button_copy_file = tk.Button(copy_file_frame, text="Copy file", height=3, bd=0, width=20, font=("Arial", 20))
    button_copy_file.grid(row=2, column=0, padx=20, pady=20)
    
    button_go_back = tk.Button(copy_file_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
    frames["copy_file_frame"] = copy_file_frame
    show_frame("copy_file_frame")
    
# Files - Move file
def create_move_file_frame():
    move_file_frame = tk.Frame(main_window)
    move_file_frame.configure(bg="midnight blue")
    move_file_frame.grid(row=1, column=0, sticky= 'news', padx=415)
    
    source_path = tk.StringVar()
    destination_path = tk.StringVar()
    
    label_source_path = tk.Label(move_file_frame, text="Source path:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_path.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    
    entry_source_path = tk.Entry(move_file_frame, font=("Arial", 20), textvariable=source_path, bg="white", fg="black")
    entry_source_path.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_destination_path = tk.Label(move_file_frame, text="Destination path:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_destination_path.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    
    entry_destination_path = tk.Entry(move_file_frame, font=("Arial", 20), textvariable=destination_path, bg="white", fg="black")
    entry_destination_path.grid(row=1, column=1, sticky='news', pady=20, padx=20)
    
    button_move_file = tk.Button(move_file_frame, text="Move file", height=3, bd=0, width=20, font=("Arial", 20))
    button_move_file.grid(row=2, column=0, padx=20, pady=20)
    
    button_go_back = tk.Button(move_file_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
    frames["move_file_frame"] = move_file_frame
    show_frame("move_file_frame")
    
# Files - Show file content    
def create_show_file_content_frame():
    show_file_content_frame = tk.Frame(main_window)
    show_file_content_frame.configure(bg="midnight blue")
    show_file_content_frame.grid(row=1, column=0, sticky= 'news', padx=415)
    
    source_file = tk.StringVar()
    
    label_source_file = tk.Label(show_file_content_frame, text="Source file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_file.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    
    entry_source_file = tk.Entry(show_file_content_frame, font=("Arial", 20), textvariable=source_file, bg="white", fg="black")
    entry_source_file.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    button_show_file_content = tk.Button(show_file_content_frame, text="Show file content", height=3, bd=0, width=20, font=("Arial", 20))
    button_show_file_content.grid(row=1, column=0, padx=20, pady=20)
    
    button_go_back = tk.Button(show_file_content_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=1, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
    frames["show_file_content_frame"] = show_file_content_frame
    show_frame("show_file_content_frame")
    
# Files - Delete file
def create_delete_file_frame():
    delete_file_frame = tk.Frame(main_window)
    delete_file_frame.configure(bg="midnight blue")
    delete_file_frame.grid(row=1, column=0, sticky= 'news', padx=415)
    
    source_file = tk.StringVar()
    
    label_source_file = tk.Label(delete_file_frame, text="Source file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_file.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    
    entry_source_file = tk.Entry(delete_file_frame, font=("Arial", 20), textvariable=source_file, bg="white", fg="black")
    entry_source_file.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    button_delete_file = tk.Button(delete_file_frame, text="Delete file", height=3, bd=0, width=20, font=("Arial", 20))
    button_delete_file.grid(row=1, column=0, padx=20, pady=20)
    
    button_go_back = tk.Button(delete_file_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=1, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
    frames["delete_file_frame"] = delete_file_frame
    show_frame("delete_file_frame")
    
# Files - Change file permissions    
def create_change_file_permissions_frame():
    change_file_permissions_frame = tk.Frame(main_window)
    change_file_permissions_frame.configure(bg="midnight blue")
    change_file_permissions_frame.grid(row=1, column=0, sticky= 'news', padx=415)
    
    source_file = tk.StringVar()
    
    label_source_file = tk.Label(change_file_permissions_frame, text="Source file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_file.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    
    entry_source_file = tk.Entry(change_file_permissions_frame, font=("Arial", 20), textvariable=source_file, bg="white", fg="black")
    entry_source_file.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    read_permission = tk.IntVar()
    write_permission = tk.IntVar()
    execute_permission = tk.IntVar()
    
    checkbutton_read = tk.Checkbutton(change_file_permissions_frame, text="Read", variable=read_permission, bg="midnight blue", fg="white")
    checkbutton_read.grid(row=1, column=0, sticky='nes', pady=10, padx=20)
    
    checkbutton_write = tk.Checkbutton(change_file_permissions_frame, text="Write", variable=write_permission, bg="midnight blue", fg="white")
    checkbutton_write.grid(row=2, column=0, sticky='nes', pady=10, padx=20)
    
    checkbutton_execute = tk.Checkbutton(change_file_permissions_frame, text="Execute", variable=execute_permission, bg="midnight blue", fg="white")
    checkbutton_execute.grid(row=3, column=0, sticky='nes', pady=10, padx=20)
    
    button_change_file_permissions = tk.Button(change_file_permissions_frame, text="Change file permissions", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: print(read_permission.get()))
    button_change_file_permissions.grid(row=4, column=0, padx=20, pady=20)
    
    button_go_back = tk.Button(change_file_permissions_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=4, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
    frames["change_file_permissions_frame"] = change_file_permissions_frame
    show_frame("change_file_permissions_frame")
  
# Files - Change file owner    
def create_change_file_owner_frame():
    change_file_owner_frame = tk.Frame(main_window)
    change_file_owner_frame.configure(bg="midnight blue")
    change_file_owner_frame.grid(row=1, column=0, sticky= 'news', padx=415)
    
    source_file = tk.StringVar()
    new_file_owner = tk.StringVar()
    
    label_source_file = tk.Label(change_file_owner_frame, text="Source file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_file.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    
    entry_source_file = tk.Entry(change_file_owner_frame, font=("Arial", 20), textvariable=source_file, bg="white", fg="black")
    entry_source_file.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_new_file_owner = tk.Label(change_file_owner_frame, text="New file owner:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_new_file_owner.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    
    entry_new_file_owner = tk.Entry(change_file_owner_frame, font=("Arial", 20), textvariable=new_file_owner, bg="white", fg="black")
    entry_new_file_owner.grid(row=1, column=1, sticky='news', pady=20, padx=20)
    
    button_change_file_owner = tk.Button(change_file_owner_frame, text="Change file owner", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_file_owner.grid(row=2, column=0, padx=20, pady=20)
    
    button_go_back = tk.Button(change_file_owner_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
    frames["change_file_owner_frame"] = change_file_owner_frame
    show_frame("change_file_owner_frame")
    
# Files - Change file group
def create_change_file_group_frame():
    change_file_group_frame = tk.Frame(main_window)
    change_file_group_frame.configure(bg="midnight blue")
    change_file_group_frame.grid(row=1, column=0, sticky= 'news', padx=415)
    
    source_file = tk.StringVar()
    new_file_group = tk.StringVar()
    
    label_source_file = tk.Label(change_file_group_frame, text="Source file:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_source_file.grid(row=0, column=0, sticky='nes', pady=20, padx=20)
    
    entry_source_file = tk.Entry(change_file_group_frame, font=("Arial", 20), textvariable=source_file, bg="white", fg="black")
    entry_source_file.grid(row=0, column=1, sticky='news', pady=20, padx=20)
    
    label_new_file_group = tk.Label(change_file_group_frame, text="New file group:", font=("Arial", 20), bg="midnight blue", fg="white")
    label_new_file_group.grid(row=1, column=0, sticky='nes', pady=20, padx=20)
    
    entry_new_file_group = tk.Entry(change_file_group_frame, font=("Arial", 20), textvariable=new_file_group, bg="white", fg="black")
    entry_new_file_group.grid(row=1, column=1, sticky='news', pady=20, padx=20)
    
    button_change_file_group = tk.Button(change_file_group_frame, text="Change file group", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_file_group.grid(row=2, column=0, padx=20, pady=20)
    
    button_go_back = tk.Button(change_file_group_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("files_menu_frame"))
    button_go_back.grid(row=2, column=1, padx=20, pady=20)
    
    main_window.update_idletasks()
    
    frames["change_file_group_frame"] = change_file_group_frame
    show_frame("change_file_group_frame")

# Processes
def create_processes_menu_frame():
    processes_menu_frame = tk.Frame(main_window)
    processes_menu_frame.configure(bg="midnight blue")
    processes_menu_frame.grid(row=1, column=0, sticky= 'news', padx=415)
    
    button_show_processes = tk.Button(processes_menu_frame, text="Show processes", height=3, bd=0, width=20, font=("Arial", 20))
    button_show_processes.grid(row=0, column=0, padx=20, pady=20)
    
    button_change_process_priority = tk.Button(processes_menu_frame, text="Change process priority", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_process_priority.grid(row=1, column=0, padx=20, pady=20)
    
    button_kill_process = tk.Button(processes_menu_frame, text="Kill process", height=3, bd=0, width=20, font=("Arial", 20))
    button_kill_process.grid(row=0, column=1, padx=20, pady=20)
    
    button_go_back = tk.Button(processes_menu_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("main_menu_frame"))
    button_go_back.grid(row=1, column=1, padx=20, pady=20)
    
    frames["processes_menu_frame"] = processes_menu_frame
    show_frame("processes_menu_frame")

# Backups
def create_backups_menu_frame():
    backups_menu_frame = tk.Frame(main_window)
    backups_menu_frame.configure(bg="midnight blue")
    backups_menu_frame.grid(row=1, column=0, sticky= 'news', padx=415)
    
    button_create_backup = tk.Button(backups_menu_frame, text="Create backup", height=3, bd=0, width=20, font=("Arial", 20))
    button_create_backup.grid(row=0, column=0, padx=20, pady=20)
    
    button_extract_backup = tk.Button(backups_menu_frame, text="Extract backup", height=3, bd=0, width=20, font=("Arial", 20))
    button_extract_backup.grid(row=1, column=0, padx=20, pady=20)
    
    button_create_backup_crontab = tk.Button(backups_menu_frame, text="Create backup crontab", height=3, bd=0, width=20, font=("Arial", 20))
    button_create_backup_crontab.grid(row=0, column=1, padx=20, pady=20)
    
    button_delete_backup_crontab = tk.Button(backups_menu_frame, text="Delete backup crontab", height=3, bd=0, width=20, font=("Arial", 20))
    button_delete_backup_crontab.grid(row=1, column=1, padx=20, pady=20)
    
    button_go_back = tk.Button(backups_menu_frame, text="Go back", height=3, bd=0, width=20, font=("Arial", 20), command= lambda: show_frame("main_menu_frame"))
    button_go_back.grid(row=2, column=0, padx=20, pady=20)
    
    frames["backups_menu_frame"] = backups_menu_frame
    show_frame("backups_menu_frame")
    
# Main Window    
main_window = tk.Tk()
main_window.title("Sys Admin v1")
main_window.configure(bg="midnight blue")
main_window.state('zoomed')
main_window.update_idletasks()

main_menu_title = tk.Label(main_window, text=" S y s t e m   A d m i n", font=("Arial", 90, "bold"), fg="white", bg="midnight blue")
main_menu_title.grid(row=0, column=0, sticky='news', pady=100, padx=250)

create_main_menu_frame()

main_window.mainloop()