# Nombre estudiante: Adriana Loaiza Escobar
# Grupo: 213022_502
# Programa: Ingeniería de sistemas
# Código fuente: Propia autoría

# Problema 5: Control de horas laborales

recursos = [
    ["Victoria Romero", 8, 9, 8, 8, 9], 
    ["Johanna Contreras", 7, 8, 7, 8, 7],
    ["Máximo Romero", 10, 9, 10, 9, 10],
    ["Sofía Martínez", 6, 7, 6, 7, 6],
]
def calcular_total_horas(horas):
    return sum(horas)

def clasificar_jornada(total_horas):
    if total_horas > 40:
        return "Sobretiempo"
    else:
        return "Horario Estándar"

print("==============================")
print("Reporte horas semanales laborales")
print("==============================")

for recurso in recursos:
    nombre = recurso[0]
    horas = recurso[1:]
    total_horas = calcular_total_horas(horas)
    clasificacion = clasificar_jornada(total_horas)
    
    print(f"Recurso: {nombre}")
    print(f"Total horas trabajadas: {total_horas}")
    print(f"Clasificación: {clasificacion}")
    
print("==============================")
print("FIN REPORTE")
print("==============================")
