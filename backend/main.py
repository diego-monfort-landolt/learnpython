from logging import root
import tkinter as tk 
from tkinter import messagebox, filedialog
from db import conectar, insertar_usuario, obtener_usuarios, eliminar_usuario_por_id, actualizar_usuario
import openpyxl

# Global für Bearbeitung
usuario_seleccionado = None

conectar()

def agregar_o_actualizar_usuario():
    global usuario_seleccionado
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    edad = entry_edad.get()

    if not nombre or not correo or not edad:
        messagebox.showwarning("Faltan datos", "Completa todos los campos.")
        return

    try:
        if usuario_seleccionado is None:
            insertar_usuario(nombre, correo, int(edad))
            messagebox.showinfo("Éxito", "Usuario agregado.")
        else:
            actualizar_usuario(usuario_seleccionado[0], nombre, correo, int(edad))
            messagebox.showinfo("Éxito", "Usuario actualizado.")
            usuario_seleccionado = None
            btn_agregar.config(text="Agregar Usuario")

        mostrar_usuarios()
        entry_nombre.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def seleccionar_usuario(event):
    global usuario_seleccionado
    seleccion = lista_usuarios.curselection()
    if not seleccion:
        return
    indice = seleccion[0]
    usuario_seleccionado = usuarios[indice]

    entry_nombre.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_edad.delete(0, tk.END)

    entry_nombre.insert(0, usuario_seleccionado[1])
    entry_correo.insert(0, usuario_seleccionado[2])
    entry_edad.insert(0, usuario_seleccionado[3])

    btn_agregar.config(text="Actualizar Usuario")

def eliminar_usuario():
    global usuario_seleccionado
    seleccion = lista_usuarios.curselection()
    if not seleccion:
        messagebox.showwarning("Atención", "Selecciona un usuario para eliminar.")
        return

    indice = seleccion[0]
    usuario = usuarios[indice]

    confirmacion = messagebox.askyesno("Eliminar", f"¿Eliminar a {usuario[1]}?")
    if confirmacion:
        eliminar_usuario_por_id(usuario[0])
        mostrar_usuarios()
        usuario_seleccionado = None
        btn_agregar.config(text="Agregar Usuario")
def mostrar_usuarios():
    global usuarios
    usuarios = obtener_usuarios()
    lista_usuarios.delete(0, tk.END)
    for usuario in usuarios:
        lista_usuarios.insert(tk.END, f"{usuario[1]} | {usuario[2]} | {usuario[3]} años")
def exportar_excel():
    ruta = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if not ruta:
        return

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Usuarios"
    ws.append(["ID", "Nombre", "Correo", "Edad"])

    for u in obtener_usuarios():
        ws.append(list(u))

    try:
        wb.save(ruta)
        messagebox.showinfo("Exportado", f"Archivo guardado en:\n{ruta}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar:\n{str(e)}")
# Interfaz
ventana = tk.Tk()
ventana.title("Gestión de Usuarios")
ventana.geometry("420x500")
ventana.configure(bg="#f0f0f0")

try:
   root.iconbitmap("../tests/cod.ico")

except:
    pass  # Falls Icon nicht gefunden wird, trotzdem starten

tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Correo").pack()
entry_correo = tk.Entry(ventana)
entry_correo.pack()

tk.Label(ventana, text="Edad").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

# Estilo de botón uniforme
btn_style = {
    "width": 30,
    "height": 2,
    "padx": 5,
    "font": ("Segoe UI", 10),
    "bd": 0,
    "relief": "flat",
    "highlightthickness": 0
}


btn_agregar = tk.Button(ventana, text="Agregar Usuario", bg="#2196F3", fg="white", command=agregar_o_actualizar_usuario, **btn_style)
btn_agregar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Usuario", bg="#f44336", fg="white", command=eliminar_usuario, **btn_style)
btn_eliminar.pack(pady=5)

btn_exportar = tk.Button(ventana, text="Exportar a Excel", bg="#4CAF50", fg="white", command=exportar_excel, **btn_style)
btn_exportar.pack(pady=5)


lista_usuarios = tk.Listbox(ventana, width=50)
lista_usuarios.pack(pady=10)
lista_usuarios.bind("<<ListboxSelect>>", seleccionar_usuario)

mostrar_usuarios()
ventana.mainloop()