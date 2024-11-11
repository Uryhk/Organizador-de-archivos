import os
import shutil

def organizar_archivos_por_extension(directorio):
    # Verificamos si el directorio existe
    if not os.path.exists(directorio):
        print(f"El directorio {directorio} no existe.")
        return
    
    # Listamos todos los archivos en el directorio
    archivos = os.listdir(directorio)
    
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
    
    print("Organización completada.")

# Llamamos a la función y pasamos el directorio donde están los archivos
directorio = '/ruta o directorio a cambiar'  # Cambia esto por la ruta de tu directorio
organizar_archivos_por_extension(directorio)
