from django.db import models



class Vacunas(models.Model):
    INTENSIDAD = (
        (1, 'Poco'),
        (2, 'Normal'),
        (3, 'Mucho'),
        )

    proveedor = models.CharField(max_length=40)
    fecha_creacion = models.DateField()
    pais_origen = models.CharField(max_length=40)
    grado_de_dolor = models.IntegerField(default = 0, choices= INTENSIDAD)

    def __str__(self):
        return f"Vacuna de proveedor {self.proveedor} - Creado el {self.fecha_creacion} - Creado en {self.pais_origen} - Con un grado de dolor : {self.grado_de_dolor}"

class Barbijos(models.Model):
    
    marca= models.CharField(max_length=40)
    tamanio= models.CharField(max_length=20)
    precio= models.IntegerField()

    def __str__(self):

        return f"Barbijos: Marca: {self.marca} Tamaño: {self.tamanio} Precio: {self.precio} "


class Oximetros(models.Model):
    
    marca= models.CharField(max_length=40)
    modelo= models.CharField(max_length=20)
    precio= models.IntegerField()

    def __str__(self):

        return f"Oximetro: Marca: {self.marca} Tamaño: {self.modelo} Precio: {self.precio} "
    

