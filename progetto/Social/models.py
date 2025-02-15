from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Tipologia(models.Model):
    nominativo = models.CharField(max_length=25, null=False, blank=False)
    creato = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Tipologia'
        verbose_name_plural = "Tipologie"
    
    def __str__(self):
        return f"{self.nominativo}"

class Company(models.Model):
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, null= False, blank=False)
    tipologia = models.ForeignKey(Tipologia, on_delete=models.CASCADE, related_name='C_Tipologia')
    target = models.CharField(max_length=100, default="Compania Standard")
    descrizione = models.TextField(max_length=250, null=True, default="Nessuna Nota Particolare")
    registrazione = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companys"

    def __str__(self):
        return f"{self.nome} {self.target}"
    
class Post(models.Model):
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    compania = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="P_Company")
    oggetto = models.TextField(max_length=250, null=False, blank=False)
    creazione = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f"Post creao da {self. utente}"
    
class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=now)
    
    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

class SocialUserActivity(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action}"
    
