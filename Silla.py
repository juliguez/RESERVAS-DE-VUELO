class Silla:
    
    CLASE = {
        'eje': 'Ejecutiva',
        'eco': 'Economica'
    }
    
        
    UBICACION = {
        'ventana': 'Ventana',
        'centro': 'Centro',
        'pasillo': 'Pasillo',

    }
    
    def __init__(self, pNumero, pClase, pUbicacion):
        self.numero = pNumero
        #operador ternario forma 1 - operador pClase debe ser true or false 
        self.clase = (self.CLASE.eje, self.CLASE.eco)[pClase]
        #operador ternario forma 2 
        #self.clase = self.CLASE.eje if pClase == 'Ejecutiva' else self.CLASE.eco
        
        if pUbicacion == 'ventana':
            self.__ubicacion = self.UBICACION.ventana
        elif pUbicacion == 'centro':
            self.__ubicacion = self.UBICACION.centro 
        elif pUbicacion == 'pasillo':
            self.__ubicacion = self.UBICACION.pasillo
        
        else:
            self.__ubicacion = None 
       
        self.__pasajero = None
    
    def asignarPasajero(self,pPasajero):
        self.__pasajero=pPasajero
    def designarSilla(self):
        self.__numero=None
    def sillaAsignada (self):
        return True if self.__numero == None else False
    def getNumero (self):
        return self.__numero
    def getClase (self):
        return self.__clase
    def getUbicacion (self):
        return self.__ubicacion
    def getPasajero (self):
        return self.__pasajero