from django.db import models

# Create your models here.







class Hopital (models.Model):
    nom = models.CharField("Nom de l'hopital ", max_length=255,)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'Hopital'
        verbose_name_plural = 'Hopitaux'


class Service (models.Model):
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE, related_name='services')
    nom = models.CharField("Libelle du service ", max_length=255,)
    en_operation = models.BooleanField("En opération", default=False)

    
    def __str__(self):
        return f" service {self.nom} de {self.hopital.nom}"
    
    class Meta:
        db_table = 'Service'
        verbose_name_plural = 'Services'


class Medecin (models.Model):
    service = models.ForeignKey(Service, on_delete = models.CASCADE, related_name='medecins')
    nom = models.CharField("Nom du medecin ", max_length=255,)
    titre = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo-medecin/')
    tel = models.CharField(max_length=20)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'Medecin'
        verbose_name_plural = 'Medecins'



class Appareil (models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Appareil", related_name='appareils')
    nom = models.CharField("Nom de l'appareil ", max_length=255,)
    

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'Appareil'
        verbose_name_plural = 'Appareils'



class Patient(models.Model):

    nom =models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateField(null=True, blank=True)
    recu = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'Patient'
        verbose_name_plural = 'Patients'










