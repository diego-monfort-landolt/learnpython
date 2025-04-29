import tkinter as tk
from tkinter import messagebox
from db import conectar, insertar_usuario, obtener_usuarios, eliminar_usuario_por_id  # <- actualizado

# Conectarse y crear la tabla si no existe
conectar()

def agregar_usuario():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    edad = entry_edad.get()

    if not nombre or not correo or not edad:
        messagebox.showwarning("Faltan datos", "Completa todos los campos.")
        return

    try:
        insertar_usuario(nombre, correo, int(edad))
        messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
        mostrar_usuarios()
        entry_nombre.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def eliminar_usuario():
    seleccion = lista_usuarios.curselection()
    if not seleccion:
        messagebox.showwarning("Atención", "Selecciona un usuario para eliminar.")
        return

    indice = seleccion[0]
    usuario = usuarios[indice]  # Obtener usuario desde la lista completa

    confirmacion = messagebox.askyesno("Eliminar", f"¿Eliminar a {usuario[1]}?")
    if confirmacion:
        eliminar_usuario_por_id(usuario[0])
        messagebox.showinfo("Eliminado", f"{usuario[1]} fue eliminado.")
        mostrar_usuarios()

def mostrar_usuarios():
    global usuarios  # Variable global para que eliminar_usuario pueda acceder
    usuarios = obtener_usuarios()
    lista_usuarios.delete(0, tk.END)
    for usuario in usuarios:
        lista_usuarios.insert(tk.END, f"{usuario[1]} | {usuario[2]} | {usuario[3]} años")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Usuarios")
ventana.resizable(True, True)
ventana.configure(bg="#f0f0f0")
ventana.geometry("400x400")

# Icono personalizado (si tienes uno)
try:
    ventana.iconbitmap("mi_icono.ico")
except:
    pass

# Campos de entrada
tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Correo").pack()
entry_correo = tk.Entry(ventana)
entry_correo.pack()

tk.Label(ventana, text="Edad").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

# Botón agregar
btn_agregar = tk.Button(ventana, text="Agregar Usuario", command=agregar_usuario)
btn_agregar.pack(pady=10)

# Botón eliminar
btn_eliminar = tk.Button(ventana, text="Eliminar Usuario Seleccionado", command=eliminar_usuario, bg="red", fg="white")
btn_eliminar.pack(pady=5)

# Lista de usuarios
lista_usuarios = tk.Listbox(ventana, width=50)
lista_usuarios.pack(pady=10)

mostrar_usuarios()

ventana.mainloop()
