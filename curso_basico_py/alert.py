from tkinter import messagebox
import tkinter as tk
# el importe esta en linia 1
"""
importar from tkinter import messagebox
messagebox.showinfo("Hinweis", "Achtung das ist ein Test")
da un mensaje alerta en windows abre ventana de alerta
"""
# muestra un mensaje de información
messagebox.showinfo("Hinweis", "Achtung das ist ein Test")
# muestra un mensaje de información
messagebox.showinfo("Info", "Das ist eine Info-Meldung!")
# muestra un mensaje de advertencia
messagebox.showwarning("Warnung", "Das ist eine Warnung!")
# muestra un fallo
messagebox.showerror("Fehler", "Das ist ein Fehler!")

# confirmar si el usuario quiere salir
antwort = messagebox.askquestion("Frage", "Möchten Sie fortfahren?")
if antwort == "yes":
    print("Benutzer möchte fortfahren.")
    
# quieres guardar?
antwort = messagebox.askokcancel("Bestätigung", "Möchten Sie speichern?")
if antwort:
    print("Speichern bestätigt.")

# estas seguro
antwort = messagebox.askyesno("Frage", "Sind Sie sicher?")
if antwort:
    print("Benutzer hat 'Ja' gewählt.")    
    
# Probar de nuevo o no
antwort = messagebox.askretrycancel("Fehler", "Möchten Sie es erneut versuchen?")
if antwort:
    print("Erneut versuchen ausgewählt.")    
    
def verificar_edad(edad):
    if edad < 18:
        messagebox.showwarning("Advertencia", "Debes ser mayor de edad.")
    else:
        messagebox.showinfo("Éxito", "Acceso permitido.")
# Crear ventana principal de Tkinter (necesario para mostrar los mensajes)
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal, solo usamos el messagebox

# Pedir al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Llamar a la función con la edad ingresada
verificar_edad(edad)

# Cerrar la ventana de Tkinter después de mostrar el mensaje
root.quit()

# haciendo un test con copilot manipulando una alerta 
def mostrar_dialogo_personalizado(titulo, mensaje, icono):
    # Crear ventana emergente personalizada
    ventana = tk.Toplevel()
    ventana.title(titulo)
    
    # Personalizar ícono (con emoji o imagen)
    if icono == "success":
        icono_texto = "👍"
        color = "green"
      
    elif icono == "error":
        icono_texto = "❗"
        color = "red"
    else:
        icono_texto = "ℹ️"
        color = "blue"
    
    # Crear y mostrar los widgets
    label = tk.Label(ventana, text=f"{icono_texto} {mensaje} {icono_texto}", font=("Arial", 14), fg=color, padx=10, pady=10)
    label.pack()

    # Botón de cerrar
    boton = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton.pack(pady=10)

    ventana.geometry("300x150")
    ventana.mainloop()

def verificar_edad(edad):
    if edad < 18:
        # Mostrar cuadro personalizado de advertencia
        mostrar_dialogo_personalizado("Advertencia", "Debes ser mayor de edad.", "error")
    else:
        # Mostrar cuadro personalizado de éxito
        mostrar_dialogo_personalizado("Éxito", "Acceso permitido.", "success")

# Crear ventana principal de Tkinter
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Pedir al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Llamar a la función con la edad ingresada
verificar_edad(edad)
root.quit()