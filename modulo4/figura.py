 class Figura:
    
    
    def _init_(self, x, y, color):
       
        self.x = x
        self.y = y
        self.color = color

        def dibujar(self):
        print("Figura dibujada en coordenadas:\n  X:" , self.x, "\n  Y:", self.y)
        print("  Color:", self.color)   

class Cuadrado(Figura):
    

    def definir_lado(self, lado):
        self.lado = lado
        
    def dibujar(self):
        print("\nCuadrado dibujado en coordenadas:\n  X:" , self.x, "\n  Y:", self.y)
        print("  Color:", self.color)    
        print("  Longitud del costado:", self.lado)
        
class Circulo(Figura):
    
      
    def definir_radio(self…
[20:36, 16/5/2023] +56 9 8226 2756: class Persona():

	def _init_(self,dni,nombre,edad):
		self.dni=dni
		self.nombre=nombre
		self.edad=edad

	@property
	def dni(self):
		return self._dni

	@dni.setter
	def dni(self,dni):
		self._dni=dni

	@property
	def nombre(self):
		return self._nombre

	@nombre.setter
	def nombre(self,nombre):
		self._nombre=nombre	

	@property
	def edad(self):
		return self._edad

	@edad.setter
	def edad(self,edad):
		if edad>0:
			self._edad=edad	
		else:
			raise ValueError("Edad incorrecta")

	def _str_(self):
		return self.dni._str_()+" "+self.nombre+" ("+str(self.edad)+")"

class Notas():

	def _init_(self):
		self._notas={}

	
	@property
	def notas(self):
		resultado=""
		for key,value in self._notas.items():
			resultado+=key+":"+str(value)+"\n"
		return resultado

	def addnotas(self,asig,nota):
		self._notas[asig]=nota

	def modnota(self,asig,nota):
		if asig in self._notas.keys():
			self._notas[asig]=nota
		else:
			raise ValueError("Asignatura incorrecta")

	def delnota(self,asig):
		if asig in self._notas.keys():
			del self._notas[asig]
		else:
			raise ValueError("Asignatura incorrecta")

	def media(self):
		return sum(self._notas.values())/len(self._notas.values())

	def _str_(self):
		resultado=""
		for key,value in self._notas.items():
			resultado+=key+":"+str(value)+"\n"
		return resultado

class Dni():

	def _init_(self,numero):
		self.numero=numero

	def __calcular_letra(self):
		letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
		return letras[int(self.numero)%23]

	@property
	def numero(self):
		return self._numero

	@numero.setter
	def numero(self,numero):
		if len(numero)==8 and numero.isdigit():
			self._numero = numero
			self.letra = self._calcular_letra()
		else: 
			raise ValueError("DNI incorecto")


	@property
	def letra(self):
		return self._letra

	def _str_(self):
		return "{0}-{1}".format(self.numero,self.letra)
	
class Alumno(Persona,Notas):

	def _init_(self,dni,nombre,edad):
		Persona._init_(self,dni,nombre,edad)
		Notas._init_(self)

	def _str_(self):
		return Persona._str(self)+"\n"+Notas.str_(self)