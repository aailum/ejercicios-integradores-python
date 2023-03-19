
"""7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
rojos"""

class Cuenta():
    def __init__(self, titular, cantidad = 0):
        self._titular = titular
        self._cantidad = cantidad

    
    def setTitular(self, titular_nuevo):
        self._titular = titular_nuevo
    
    def getTitular(self):
        return self._titular
    
    def ingresarDinero(self, cant_ingresar):
        if cant_ingresar > 0:
            self._cantidad += cant_ingresar
        
    def retirarDinero(self, cant_retirar):
        self._cantidad -= cant_retirar
    
    def getCantidad(self):
        return self._cantidad
    
    def mostrar(self):
        return f"""\nTitular: {self._titular}\n Cantidad dinero: {self._cantidad}"""
    
    



"""8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuentaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta."""
    

class CuentaJoven(Cuenta):
    
    def __init__(self, titular, edad, cantidad = 0):
        super().__init__(titular, cantidad)
        self._edad = edad
        self._bonificacion = " "
        
    def getEdad(self):
        return self._edad
    
    def setBonificacion(self, bon):
        self._bonificacion = bon
    
    def getBonificacion(self):
        return self._bonificacion
        
    
    def es_titular_valido(self):
        if  18 <= self._edad < 25:
            return True
        return False
    
    def retirarDinero(self, cant_retirar):
        if self.es_titular_valido():
            return super().retirarDinero(cant_retirar)
        else:
            return f"""Movimiento no permitido"""
    
    def mostrar(self):
        info = super().mostrar()
        return f"""Cuenta Joven""" + info + f"""\n Bonificacion: {self._bonificacion}"""
    
    