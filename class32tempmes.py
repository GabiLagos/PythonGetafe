class TempMes:
    nombre = ""
    tmax = 0
    tmin = 0
    
    def gettempMedia(self):
        return (self.tmax + self.tmin) / 2
    
    def __str__(self):
        return "En el mes de "+ self.nombre+ " la T máxima fue " + str(self.tmax)+"ºC" + " y la T mínima fue " + str(self.tmin)+"ºC"