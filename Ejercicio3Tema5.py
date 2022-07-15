def esBisiciesto(anio):
    if anio%4==0:
        if anio%100==0:
            if anio%400==0:
                return "Es bisiciesto"
            else: 
                return "No es biciesto"
        else:
            return "Es biciesto"
    else:
        return "No es biciesto"


print("Es bisiciesto?: ",esBisiciesto(2024))
