# modules
# ================================================
import random
import unicodedata
import datetime


# function
# =======================================
def person(self):

    # attributes
    person_first_name = first_name()
    person_last_name  = last_name()
    person_email      = email(person_first_name, person_last_name)
    person_birthday   = birthday()
    person_age        = age(person_birthday)

    # bye
    return {
        "first_name": person_first_name,
         "last_name": person_last_name,
             "email": person_email,
          "birthday": person_birthday,
               "age": person_age,
    }


# function
# =======================================
def first_name():
    items = ["Santiago", "Sebastián", "Matías", "Mateo", "Nicolás", "Alejandro", "Diego", "Samuel", "Benjamín", "Daniel", "Joaquín", "Lucas", "Tomas", "Gabriel", "Martín", "David", "Emiliano", "Jerónimo", "Emmanuel", "Agustín", "Juan Pablo", "Juan José", "Andrés", "Thiago", "Leonardo", "Felipe", "Ángel", "Maximiliano", "Adrián", "Pablo", "Carlos", "Rodrigo", "Vicente", "Ignacio", "Emilio", "Valentino", "Bruno", "Santino", "Julián", "Carlos", "Ana", "Antonia", "Carmen", "Concepcion", "Cristina", "Dolores", "Elena", "Francisca", "Isabel", "Josefa", "Laura", "Lucia", "Manuela", "Maria", "Marta", "Paula", "Pilar", "Raquel", "Rosa", "Sara"]
    return random.choice(items)


# function
# =======================================
def last_name():
    items = ["Acosta", "Álvarez", "Ayala", "Benegas", "Benítez", "Cossio", "Diaz", "Fasan", "Fernández", "Fidalgo", "Flores", "Frangi", "García", "Garitta", "Garzón", "Ghio", "Gómez", "González", "Huerta", "Ibañez", "Karbabian", "López", "Macko", "Maculan", "Martínez", "Mendiola", "Olivera", "Ortiz", "Pérez", "Pistani", "Ramírez", "Rodríguez", "Rojas", "Romero", "Ruiz", "Sánchez", "Senestrari", "Sosa", "Torres", "Ventre", "González", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto", "Contreras", "Silva", "Martínez", "Sepúlveda", "Morales", "Rodríguez", "López", "Fuentes", "Hernández", "Torres", "Araya", "Flores", "Espinoza", "Valenzuela", "Castillo", "Tapia", "Reyes", "Gutiérrez", "Castro", "Pizarro", "Álvarez", "Vásquez", "Sánchez", "Fernández", "Ramírez", "Carrasco", "Gómez", "Cortés", "Herrera", "Núñez", "Jara", "Vergara", "Rivera", "Figueroa", "Riquelme", "García", "Miranda", "Bravo", "Vera", "Molina", "Vega", "Campos", "Sandoval", "Orellana", "Cárdenas", "Olivares", "Alarcón", "Gallardo", "Ortiz", "Garrido", "Salazar", "Guzmán", "Henríquez", "Saavedra", "Navarro", "Aguilera", "Parra", "Romero", "Aravena", "Vargas", "Vázquez", "Cáceres", "Yáñez", "Leiva", "Escobar", "Ruiz", "Valdés", "Vidal", "Salinas", "Zúñiga", "Peña", "Godoy", "Lagos", "Maldonado", "Bustos", "Medina", "Pino", "Palma", "Moreno", "Sanhueza", "Carvajal", "Navarrete", "Sáez", "Alvarado", "Donoso", "Poblete", "Bustamante", "Toro", "Ortega", "Venegas", "Lopez", "Mendoza", "Farías"]
    return random.choice(items)


# function
# =======================================
def email(first_name, last_name):
    items  = ["@gmail.com", "@hotmail.com", "@yahoo.com", "@outlook.com"]
    domain = random.choice(items)
    oid    = str(random.randint(1000, 9999))
    
    # result
    email = (first_name + "." + last_name + "." + oid + domain)
    email = email.lower()
    email = strip_accents(email)

    return email


# function
# =======================================
def birthday():
    day      = random.randint(1, 365)
    year     = random.randint(1940, 2000)
    obj_date = datetime.datetime.strptime('{} {}'.format(day, year), '%j %Y')

    return obj_date.strftime("%Y/%m/%d")


# function
# =======================================
def age(birthday):
    year, month, day = birthday.split('/')
    today            = datetime.date.today()

    return int(today.year - int(year) - ((today.month, today.day) < (int(month), int(day))))


# function
# ================================================
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
