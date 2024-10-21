import json
import csv

def guardar_receta(nombre, ingredientes, instrucciones):
    receta = {
        'nombre': nombre,
        'ingredientes': ingredientes,
        'instrucciones': instrucciones
    }
    
    with open('recetas.json', 'a') as f:
        f.write(json.dumps(receta) + "\n")

def guardar_menu_dia(dia, menu):
    with open('menu_diario.txt', 'a') as f:
        f.write(f"{dia}: {', '.join(menu)}\n")

def guardar_restaurante(nombre, direccion, telefono):
    with open('restaurantes.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([nombre, direccion, telefono])

def guardar_opinion(nombre_plato, opinion):
    with open('opiniones.txt', 'a') as f:
        f.write(f"{nombre_plato}: {opinion}\n")

if __name__ == "__main__":

    guardar_receta("Tortilla Española", ["huevos", "patatas", "cebolla"], "Freír las patatas, batir los huevos y mezclar.")

    guardar_menu_dia("Lunes", ["Desayuno: Avena", "Almuerzo: Ensalada", "Cena: Pollo al horno"])

    guardar_restaurante("Restaurante El Sabor", "Calle Falsa 123", "555-1234")

    guardar_opinion("Tortilla Española", "Deliciosa, me encantó!")
