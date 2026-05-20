# Nombre estudiante: Adriana Loaiza Escobar
# Grupo: 213022_502
# Programa: Ingeniería de sistemas
# Código fuente: Propia autoría

# Problema 5: Control de horas laborales

recursos = []

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

def calcular_total_horas(horas):
    return sum(horas)
def clasificar_jornada(total_horas):
    if total_horas > 40:
        return "Sobretiempo"
    else:
        return "Horario Estándar"

cantidad_recursos = int(input("Ingrese la cantidad de recursos: "))
for i in range(cantidad_recursos):
    print("==============================")
    print(f"Registro empleado {i + 1}")
    print("==============================")
    
    nombre = input("Ingrese el nombre del recurso: ")
    horas_semana = []
    for dia in dias:
        horas = float(input(f"Ingrese las horas trabajadas el {dia}: "))
        horas_semana.append(horas)
    recursos.append([nombre] + horas_semana)
    
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
