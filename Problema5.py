# Nombre del estudiante: Eliana Elizabeth Agudelo Barón 
# Grupo: 213022
# Programa: Ingenieria de sistemas

#-------------------------------------------------------------------
# MODULO 1: Calcular el total de horas semanales por recurso
#-------------------------------------------------------------------

def calcular_total_horas(horas_diarias):
    """
    Recibe una lista con las horas trabajadas de lunes a viernes.
    Retorna la suma total de horas de la semana.
    """
    total = 0
    for horas in horas_diarias:
        total += horas
    return total


#--------------------------------------------------------------------
# MÓDULO 2: Clasificar la jornada laboral
#--------------------------------------------------------------------
def clasificar_jornada(total_horas, umbral=40):
    """
    Recibe el total de horas semanales y el umbral estandar (40 h).
    Retorna la clasificación de la jornada laboral.
    """
    if total_horas > umbral:
        return "Sobretiempo"
    else:
        return "Horario Estándar"
    
#--------------------------------------------------------------------
# Modulo 3: Imprimir el reporte de cada recurso
#--------------------------------------------------------------------

def imprimir_reporte(nombre, total_horas, clasificacion):
    """
    Recibe el nombre del recurso, el total de horas y la clasificación.
    Imprime la información formateada en consola.
    """
    print(f"Reporte para {nombre}:")
    print(f"Total de hrs : {total_horas} horas")
    print(f"Jornada: {clasificacion}")
    print("-"*40)

#--------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------
def main():
    # ---------------------------------------------------------------
    # Matriz: [Nombre, Lun, Mar, Mie, Jue, Vie]
    # ---------------------------------------------------------------
    equipo = [
        ["Ana Garcia", 9, 8, 10, 9, 8],
        ["Luis Martinez", 8, 8, 8, 8, 8],
        ["Sofia Torres",10,9,11,10,9],
        ["Carlos Ruiz", 7, 6, 8, 7, 6],
    ]
    UMBRAL_HORAS = 40
    print ("="*40)
    print(" REPORTE DE HORAS SEMANALES DEL EQUIPO")
    print ("="*40)
    
    for recurso in equipo:
        nombre = recurso[0]
        horas_diarias = recurso[1:]

        total_horas = calcular_total_horas(horas_diarias)
        clasificacion = clasificar_jornada(total_horas, UMBRAL_HORAS)
        imprimir_reporte(nombre, total_horas, clasificacion)

    print("\nUmbral estandar semanal:", UMBRAL_HORAS, "horas")
    print("Fin del reporte.")

# Punto de entrada
if __name__ == "__main__":
    main()
