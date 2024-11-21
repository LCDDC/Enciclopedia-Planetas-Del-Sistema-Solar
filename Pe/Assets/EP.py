from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Enciclopedia de planetas")
root.geometry("550x550")
root.configure(bg="black")

mercury = ImageTk.PhotoImage(Image.open("Mercurio.jpg"))
saturn = ImageTk.PhotoImage(Image.open("Saturno.jpg"))
earth = ImageTk.PhotoImage(Image.open("Tierra.jpg"))
jupiter = ImageTk.PhotoImage(Image.open("Jupiter.jpg"))
marte = ImageTk.PhotoImage(Image.open("Marte.jpg"))
neptuno = ImageTk.PhotoImage(Image.open("Neptuno.jpg"))
urano = ImageTk.PhotoImage(Image.open("Urano.jpg"))
venus = ImageTk.PhotoImage(Image.open("Venus.jpg"))


label_planet = Label(root, text="Planet : ", bg="black", fg="white")
label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
label_planet_name = Label(root, text="", bg="black", fg="white")
label_planet_name.place(relx=0.5, rely=0.25, anchor= CENTER)
label_planet_image = Label(root, bg="gold", highlightthickness=5,borderwidth=2, relief=SOLID)
label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)
label_planet_gravity_radius = Label(root, bg="black", fg="white")
label_planet_gravity_radius.place(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info = Label(root, bg="black", fg="white", wrap=500)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

planets=["Mercurio","Saturno","Tierra","Jupiter","Marte","Neptuno","Urano","Venus"]
selected_value = StringVar()
dropdown = ttk.Combobox(root, values=planets, textvariable= selected_value)
dropdown.place(relx=0.5, rely=0.1, anchor=CENTER)
def planetInfo():
    planet = selected_value.get()
    if planet=="Mercurio":
        label_planet_name['text'] = "Mercurio"
        label_planet_image['image'] = mercury
        label_planet_gravity_radius['text'] = "Gravedad: 3.7m/s² \n Radio: 2439.7 kilometros"
        label_planet_info['text'] = "Mercurio es el planeta mas pequeño en nuestro sistema solar. Es apenas un poco mas pequeña que la Luna de la tierra."
    elif planet=="Saturno":
        label_planet_name['text'] = "Saturno"
        label_planet_image['image'] = saturn
        label_planet_gravity_radius['text'] = "Gravedad: 3.711m/s² \n Radio: 60268 kilometros"
        label_planet_info['text'] = "Mercurio es el planeta mas pequeño en nuestro sistema solar. Es apenas un poco mas pequeña que la Luna de la tierra."
        
    elif planet=="Tierra":
            label_planet_name['text'] = "Tierra"
            label_planet_image['image'] = earth
            label_planet_gravity_radius['text'] = "Gravedad: 9.807m/s² \n Radio: 60371 kilometros"
            label_planet_info['text'] = "La Tierra es el tercer planeta desde el Sol y el quinto más grande de nuestro sistema solar. Es el único planeta conocido hasta ahora que alberga vida."
    
    elif planet=="Jupiter":
        label_planet_name['text'] = "Jupiter"
        label_planet_image['image'] = jupiter
        label_planet_gravity_radius['text'] = "Gravedad: 24.79m/s² \n Radio: 69,911 kilometros"
        label_planet_info['text'] = "Júpiter es el planeta más grande de nuestro sistema solar. Es tan enorme que podría contener a más de 1.300 Tierras en su interior. De hecho, es tan grande que si fuera hueco, podrían caber todos los demás planetas del sistema solar dentro de él."

    elif planet=="Marte":
        label_planet_name['text'] = "Marte"
        label_planet_image['image'] = marte
        label_planet_gravity_radius['text'] = "Gravedad: 24.79m/s² \n Radio: 3,389.5 kilometros"
        label_planet_info['text'] = "Marte, a menudo llamado el Planeta Rojo debido a su tono rojizo causado por el óxido de hierro en su superficie, es más pequeño que la Tierra. Aunque es considerablemente más grande que nuestra Luna, Marte es aproximadamente la mitad del tamaño de nuestro planeta hogar."
        
    elif planet=="Neptuno":
        label_planet_name['text'] = "Neptuno"
        label_planet_image['image'] = neptuno
        label_planet_gravity_radius['text'] = "Gravedad: 11.5m/s² \n Radio: 3,389.5 kilometros"
        label_planet_info['text'] = "A diferencia de los gigantes gaseosos como Júpiter y Saturno, Neptuno es clasificado como un gigante de hielo. Esto significa que su interior está compuesto por una mezcla de agua, amoniaco y metano, sobre un núcleo sólido del tamaño aproximado de la Tierra. Su atmósfera, rica en hidrógeno, helio y metano, es la causa de su característico color azul intenso."
        
    elif planet=="Urano":
        label_planet_name['text'] = "Urano"
        label_planet_image['image'] = urano
        label_planet_gravity_radius['text'] = "Gravedad: 8.87m/s² \n Radio: 25,559 kilometros"
        label_planet_info['text'] = "Urano está compuesto principalmente de hielo, amoníaco y metano, sobre un pequeño núcleo rocoso. Su atmósfera, rica en hidrógeno y helio, es la responsable de su color azul. A diferencia de otros gigantes gaseosos, Urano no emite mucho calor interno, lo que lo convierte en el planeta más frío del sistema solar."
        
    elif planet=="Venus":
        label_planet_name['text'] = "Venus"
        label_planet_image['image'] = venus
        label_planet_gravity_radius['text'] = "Gravedad: 8.87m/s² \n Radio: 6,051.8 kilometros"
        label_planet_info['text'] = "Venus, a menudo llamado el 'gemelo malvado' de la Tierra, es un planeta fascinante y misterioso. A pesar de ser nuestro vecino más cercano en el Sistema Solar, es un mundo completamente diferente al nuestro."

btn = Button(root, text = "Mostrar Informacion", command=planetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

root.mainloop()