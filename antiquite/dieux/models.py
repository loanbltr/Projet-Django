from django.db import models

class Dieu(models.Model):
    nom = models.CharField(max_length=100)
    association = models.CharField(max_length=100)
    arme = models.CharField(max_length=100, blank=True, null=True)
    histoire = models.TextField(null=True, blank=True)
    civilisation = models.ForeignKey("civilisation", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"{self.nom} est un dieu. Voici son association: {self.association}."
        return chaine

    def dico(self):
        return {'nom': self.nom, 'association':self.association, 'arme':self.arme, 'histoire':self.histoire, 'civilisation':self.civilisation}

class civilisation(models.Model):
    nom = models.CharField(max_length=50)
    desc = models.TextField(null=True, blank=True)
    def __str__(self):
        chain = f"Civilisation {self.nom} "
        return chain

    def civilisation(self):
        return {"nom":self.nom, "desc": self.desc}
