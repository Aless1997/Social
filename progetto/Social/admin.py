from django.contrib import admin
from Social.models import Company, Post, Tipologia, Profile, SocialUserActivity
from django.contrib.admin.models import LogEntry

admin.site.register(Company)
admin.site.register(Post)
admin.site.register(Tipologia)
admin.site.register(LogEntry)
admin.site.register(Profile)
admin.site.register(SocialUserActivity)

admin.site.site_header = "Gestione Social App"
admin.site.site_title = "Amministrazione Prodotti"
admin.site.index_title = "Benvenuto nell'Admin"

