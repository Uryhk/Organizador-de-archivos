import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organizar_archivos_por_extension(directorio, archivos):
    # Verificamos si el directorio existe
    if not os.path.exists(directorio):
        messagebox.showerror("Error", f"El directorio {directorio} no existe.")
        return
    
    # Creamos la carpeta "otros" si no existe
    carpeta_otros = os.path.join(directorio, 'otros')
    if not os.path.exists(carpeta_otros):
        os.makedirs(carpeta_otros)
        print(f"Carpeta 'otros' creada.")
    
    # Recorremos todos los archivos en el directorio
    for archivo in archivos:
        ruta_archivo = os.path.join(directorio, archivo)
        
        # Verificamos que sea un archivo (no un directorio)
        if os.path.isfile(ruta_archivo):
            # Obtenemos la extensión del archivo
            _, extension = os.path.splitext(archivo)
            
            # Si tiene extensión, la procesamos
            if extension:
                # Quitamos el punto al principio de la extensión para crear la carpeta
                extension_carpeta = extension[1:]  # Esto elimina el punto (.)
                
                # Si la carpeta con el nombre de la extensión no existe, la creamos
                carpeta_destino = os.path.join(directorio, extension_carpeta)
                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)
                    print(f"Carpeta '{extension_carpeta}' creada.")
                
                # Movemos el archivo a la carpeta correspondiente (esto mueve el archivo)
                destino = os.path.join(carpeta_destino, archivo)
                shutil.move(ruta_archivo, destino)  # Mueve el archivo, no lo copia
                print(f"Moviendo archivo {archivo} a {carpeta_destino}")
            
            else:
                # Si no tiene extensión, lo movemos a la carpeta 'otros'
                destino = os.path.join(carpeta_otros, archivo)
                shutil.move(ruta_archivo, destino)  # Mueve el archivo a 'otros'
                print(f"Moviendo archivo {archivo} a {carpeta_otros}")
    
    messagebox.showinfo("Éxito", "Organización completada.")

def seleccionar_directorio():
    # Crear la ventana principal de tkinter (no se mostrará)
    root = tk.Tk()
    root.withdraw()  # Esto oculta la ventana principal

    # Mostrar un cuadro de diálogo para seleccionar el directorio
    directorio = filedialog.askdirectory(title="Selecciona un directorio para ordenar")
    
    if directorio:
        mostrar_archivos_y_ordenar(directorio)
    else:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ningún directorio.")

def mostrar_archivos_y_ordenar(directorio):
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Ordenador de Archivos")

    # Mostrar el directorio seleccionado en la ventana
    label = tk.Label(root, text=f"Archivos en: {directorio}")
    label.pack(pady=10)

    # Listamos todos los archivos en el directorio
    archivos = os.listdir(directorio)
    archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(directorio, archivo))]

    # Crear un Listbox para mostrar los archivos
    listbox = tk.Listbox(root, width=60, height=15)
    listbox.pack(padx=10, pady=10)

    # Insertar los archivos en el Listbox
    for archivo in archivos:
        listbox.insert(tk.END, archivo)

    # Función para ordenar los archivos cuando se presiona el botón
    def ordenar_archivos():
        archivos_seleccionados = listbox.get(0, tk.END)
        if archivos_seleccionados:
            organizar_archivos_por_extension(directorio, archivos_seleccionados)
        else:
            messagebox.showwarning("Advertencia", "No hay archivos para ordenar.")

    # Botón para ordenar los archivos
    ordenar_button = tk.Button(root, text="Ordenar Archivos", command=ordenar_archivos)
    ordenar_button.pack(pady=20)

    # Iniciar el bucle principal de tkinter
    root.mainloop()

# Llamamos a la función para seleccionar el directorio
seleccionar_directorio()
