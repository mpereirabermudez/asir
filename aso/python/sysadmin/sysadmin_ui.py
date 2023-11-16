import tkinter as tk

# Window Size
def window_size(width, height):
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    x = (screen_width - width) / 2
    y = (screen_height - height) / 2
    main_window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    main_window.resizable(False, False)
    
# Users 
def show_users_window():
    window_size(280, 450)
    files_menu_frame.pack_forget()
    processes_menu_frame.pack_forget()
    backups_menu_frame.pack_forget()
    main_menu_frame.pack_forget()
    users_menu_frame.configure(bg="black")
    users_menu_frame.pack()
    
    button_create_user = tk.Button(users_menu_frame, text="Crear usuario", height=2, bd=0, width=11)
    button_create_user.pack(pady=10)
    button_create_group= tk.Button(users_menu_frame, text="Crear grupo", height=2, bd=0, width=11)
    button_create_group.pack(pady=10)
    button_change_group= tk.Button(users_menu_frame, text="Cambiar de grupo", height=2, bd=0, width=11)
    button_change_group.pack(pady=10)
    button_delete_user= tk.Button(users_menu_frame, text="Eliminar usuario", height=2, bd=0, width=11)
    button_delete_user.pack(pady=10)
    button_delete_group= tk.Button(users_menu_frame, text="Eliminar grupo", height=2, bd=0, width=11)
    button_delete_group.pack(pady=10)  

# Files
def show_files_window():
    window_size(280, 570)
    users_menu_frame.pack_forget()
    processes_menu_frame.pack_forget()
    backups_menu_frame.pack_forget()
    main_menu_frame.pack_forget()
    files_menu_frame.configure(bg="black")
    files_menu_frame.pack()
    
    button_copy_file = tk.Button(files_menu_frame, text="Copiar archivo", height=2, bd=0, width=11)
    button_copy_file.pack(pady=10)
    button_move_file= tk.Button(files_menu_frame, text="Mover archivo", height=2, bd=0, width=11)
    button_move_file.pack(pady=10)
    button_show_content= tk.Button(files_menu_frame, text="Mostrar contenido", height=2, bd=0, width=11)
    button_show_content.pack(pady=10)
    button_delete_file= tk.Button(files_menu_frame, text="Eliminar archivo", height=2, bd=0, width=11)
    button_delete_file.pack(pady=10)
    button_change_permissions= tk.Button(files_menu_frame, text="Cambiar permisos", height=2, bd=0, width=11)
    button_change_permissions.pack(pady=10)
    button_change_owner= tk.Button(files_menu_frame, text="Cambiar propietario", height=2, bd=0, width=11)
    button_change_owner.pack(pady=10)
    button_change_group= tk.Button(files_menu_frame, text="Cambiar grupo", height=2, bd=0, width=11)
    button_change_group.pack(pady=10)

# Processes
def show_proccess_window():
    window_size(280, 330)
    users_menu_frame.pack_forget()
    files_menu_frame.pack_forget()
    backups_menu_frame.pack_forget()
    main_menu_frame.pack_forget()
    processes_menu_frame.configure(bg="black")
    processes_menu_frame.pack()
    
    button_show_processes = tk.Button(processes_menu_frame, text="Mostrar procesos", height=2, bd=0, width=11)
    button_show_processes.pack(pady=10)
    button_change_priority = tk.Button(processes_menu_frame, text="Cambiar prioridad", height=2, bd=0, width=11)
    button_change_priority.pack(pady=10)
    button_kill_process = tk.Button(processes_menu_frame, text="Terminar proceso", height=2, bd=0, width=11)
    button_kill_process.pack(pady=10)

# Backups
def show_backup_window():
    window_size(280, 390)
    users_menu_frame.pack_forget()
    files_menu_frame.pack_forget()
    processes_menu_frame.pack_forget()
    main_menu_frame.pack_forget()
    backups_menu_frame.configure(bg="black")
    backups_menu_frame.pack()
    
    button_create_backup = tk.Button(backups_menu_frame, text="Crear backup", height=2, bd=0, width=11)
    button_create_backup.pack(pady=10)
    button_create_backup = tk.Button(backups_menu_frame, text="Crear crontab", height=2, bd=0, width=11)
    button_create_backup.pack(pady=10)
    button_create_backup = tk.Button(backups_menu_frame, text="Eliminar crontab", height=2, bd=0, width=11)
    button_create_backup.pack(pady=10)
    button_create_backup = tk.Button(backups_menu_frame, text="Extraer backup", height=2, bd=0, width=11)
    button_create_backup.pack(pady=10)

# Main Window    
main_window = tk.Tk()
main_window.title("Sys Admin v1")
main_window.configure(bg="black")
window_size(280, 390)

main_menu_title = tk.Label(main_window, text="Sys Admin v1", font=("Arial", 30, "bold"), fg="white", width=400, height=3, anchor="center")
main_menu_title.configure(bg="black")
main_menu_title.pack()

# Main Frames
users_menu_frame = tk.Frame(main_window)
files_menu_frame = tk.Frame(main_window)
processes_menu_frame = tk.Frame(main_window)
backups_menu_frame = tk.Frame(main_window)

# Main Menu Buttons
main_menu_frame = tk.Frame(main_window)
main_menu_frame.configure(bg="black")
main_menu_frame.pack()

button_users = tk.Button(main_menu_frame, text="Usuarios", height=2, bd=0, width=7, command=show_users_window)
button_users.pack(pady=10)
button_files = tk.Button(main_menu_frame, text="Archivos", height=2, bd=0, width=7, command=show_files_window)
button_files.pack(pady=10)
button_processes = tk.Button(main_menu_frame, text="Procesos", height=2, bd=0, width=7, command=show_proccess_window)
button_processes.pack(pady=10)
button_backups = tk.Button(main_menu_frame, text="Backups", height=2, bd=0, width=7, command=show_backup_window)
button_backups.pack(pady=10)

main_window.mainloop()