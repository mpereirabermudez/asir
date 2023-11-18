import tkinter as tk
    
# Users 
def show_users_window():
    main_menu_frame.pack_forget()
    files_menu_frame.pack_forget()
    processes_menu_frame.pack_forget()
    backups_menu_frame.pack_forget()
    main_menu_frame.pack_forget()
    users_menu_frame.configure(bg="midnight blue")
    users_menu_frame.pack()
    
    button_create_user = tk.Button(users_menu_frame, text="Crear usuario", height=3, bd=0, width=20, font=("Arial", 20))
    button_create_user.grid(row=0, column=0, padx=20, pady=20)
    button_create_group= tk.Button(users_menu_frame, text="Crear grupo", height=3, bd=0, width=20, font=("Arial", 20))
    button_create_group.grid(row=1, column=0, padx=20, pady=20)
    button_change_group= tk.Button(users_menu_frame, text="Cambiar de grupo", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_group.grid(row=2, column=0, padx=20, pady=20)
    button_delete_user= tk.Button(users_menu_frame, text="Eliminar usuario", height=3, bd=0, width=20, font=("Arial", 20))
    button_delete_user.grid(row=0, column=1, padx=20, pady=20)
    button_delete_group= tk.Button(users_menu_frame, text="Eliminar grupo", height=3, bd=0, width=20, font=("Arial", 20))
    button_delete_group.grid(row=1, column=1, padx=20, pady=20)

# Files
def show_files_window():
    users_menu_frame.pack_forget()
    processes_menu_frame.pack_forget()
    backups_menu_frame.pack_forget()
    main_menu_frame.pack_forget()
    files_menu_frame.configure(bg="midnight blue")
    files_menu_frame.pack()
    
    button_copy_file = tk.Button(files_menu_frame, text="Copiar archivo", height=3, bd=0, width=20, font=("Arial", 20))
    button_copy_file.grid(row=0, column=0, padx=20, pady=20)
    button_move_file= tk.Button(files_menu_frame, text="Mover archivo", height=3, bd=0, width=20, font=("Arial", 20))
    button_move_file.grid(row=1, column=0, padx=20, pady=20)
    button_show_content= tk.Button(files_menu_frame, text="Mostrar contenido", height=3, bd=0, width=20, font=("Arial", 20))
    button_show_content.grid(row=2, column=0, padx=20, pady=20)
    button_delete_file= tk.Button(files_menu_frame, text="Eliminar archivo", height=3, bd=0, width=20, font=("Arial", 20))
    button_delete_file.grid(row=0, column=1, padx=20, pady=20)
    button_change_permissions= tk.Button(files_menu_frame, text="Cambiar permisos", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_permissions.grid(row=1, column=1, padx=20, pady=20)
    button_change_owner= tk.Button(files_menu_frame, text="Cambiar propietario", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_owner.grid(row=3, column=0, padx=20, pady=20)
    button_change_group= tk.Button(files_menu_frame, text="Cambiar grupo", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_group.grid(row=2, column=1, padx=20, pady=20)

# Processes
def show_proccess_window():
    users_menu_frame.pack_forget()
    files_menu_frame.pack_forget()
    backups_menu_frame.pack_forget()
    main_menu_frame.pack_forget()
    processes_menu_frame.configure(bg="midnight blue")
    processes_menu_frame.pack()
    
    button_show_processes = tk.Button(processes_menu_frame, text="Mostrar procesos", height=3, bd=0, width=20, font=("Arial", 20))
    button_show_processes.pack(pady=20)
    button_change_priority = tk.Button(processes_menu_frame, text="Cambiar prioridad", height=3, bd=0, width=20, font=("Arial", 20))
    button_change_priority.pack(pady=20)
    button_kill_process = tk.Button(processes_menu_frame, text="Terminar proceso", height=3, bd=0, width=20, font=("Arial", 20))
    button_kill_process.pack(pady=20)

# Backups
def show_backup_window():
    users_menu_frame.pack_forget()
    files_menu_frame.pack_forget()
    processes_menu_frame.pack_forget()
    main_menu_frame.pack_forget()
    backups_menu_frame.configure(bg="midnight blue")
    backups_menu_frame.pack()
    
    button_create_backup = tk.Button(backups_menu_frame, text="Crear backup", height=3, bd=0, width=20, font=("Arial", 20))
    button_create_backup.pack(pady=20)
    button_create_backup = tk.Button(backups_menu_frame, text="Crear crontab", height=3, bd=0, width=20, font=("Arial", 20))
    button_create_backup.pack(pady=20)
    button_create_backup = tk.Button(backups_menu_frame, text="Eliminar crontab", height=3, bd=0, width=20, font=("Arial", 20))
    button_create_backup.pack(pady=20)
    button_create_backup = tk.Button(backups_menu_frame, text="Extraer backup", height=3, bd=0, width=20, font=("Arial", 20))
    button_create_backup.pack(pady=20)
    
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

# Main Frames
users_menu_frame = tk.Frame(main_window)
files_menu_frame = tk.Frame(main_window)
processes_menu_frame = tk.Frame(main_window)
backups_menu_frame = tk.Frame(main_window)

# Main Menu Buttons
main_menu_frame = tk.Frame(main_window)
main_menu_frame.configure(bg="midnight blue")
main_menu_frame.pack()

button_users = tk.Button(main_menu_frame, text="Usuarios", height=3, bd=0, width=20, font=("Arial", 20), command=show_users_window)
button_users.pack(pady=20)
button_files = tk.Button(main_menu_frame, text="Archivos", height=3, bd=0, width=20, font=("Arial", 20), command=show_files_window)
button_files.pack(pady=20)
button_processes = tk.Button(main_menu_frame, text="Procesos", height=3, bd=0, width=20, font=("Arial", 20), command=show_proccess_window)
button_processes.pack(pady=20)
button_backups = tk.Button(main_menu_frame, text="Backups", height=3, bd=0, width=20, font=("Arial", 20), command=show_backup_window)
button_backups.pack(pady=20)

main_window.mainloop()