from tkinter import messagebox
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
    