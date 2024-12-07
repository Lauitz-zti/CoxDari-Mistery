from pymongo import MongoClient
import datetime

# Conexión a la base de datos
client = MongoClient('mongodb://localhost:27017/')
db = client['CoxDariMysteri']

# Colecciones de la base de datos
usuarios = db['usuarios']
personajes_secundarios = db['personajes_secundarios']
progresos = db['progresos']
retos_misiones = db['retos_misiones']
items = db['items']
pistas = db['pistas']

# Funciones de inicialización
def crear_usuario(nombre, avatar, nivel=1):
    usuario = {
        "avatar": avatar,
        "nombre": nombre,
        "nivel": nivel,
        "progreso": [],
        "inventario": [],
        "experiencia": 0,
        "fecha_creacion": datetime.datetime.now()
    }
    usuarios.insert_one(usuario)
    print(f"Usuario {nombre} creado exitosamente.")

def agregar_personaje_secundario(nombre, lenguaje_programacion, habilidad, pistas_asociadas=[]):
    personaje = {
        "nombre": nombre,
        "lenguaje_programacion": lenguaje_programacion,
        "habilidad": habilidad,
        "pistas_asociadas": pistas_asociadas
    }
    personajes_secundarios.insert_one(personaje)
    print(f"Personaje {nombre} agregado.")

def agregar_reto(nombre, logica, lenguaje, solucion, dificultad, recompensa, tiempo_limite, requisito):
    reto = {
        "nombre": nombre,
        "logica": logica,
        "lenguaje": lenguaje,
        "solucion": solucion,
        "dificultad": dificultad,
        "recompensa": recompensa,
        "tiempo_limite": tiempo_limite,
        "requisito": requisito
    }
    retos_misiones.insert_one(reto)
    print(f"Reto {nombre} agregado.")

def agregar_item(nombre, descripcion, categoria, efecto):
    item = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "efecto": efecto
    }
    items.insert_one(item)
    print(f"Item {nombre} agregado.")

def agregar_pista(descripcion, personaje_asociado, reto_asociado):
    pista = {
        "descripcion": descripcion,
        "personaje_asociado": personaje_asociado,
        "reto_asociado": reto_asociado
    }
    pistas.insert_one(pista)
    print(f"Pista agregada: {descripcion}")