from django.contrib import admin

from calendarApp.models import AppUser
# Register your models here.

#Ta linijka sprawia, że Django stworzy/zaktualizuje schemat bazy danych na podstwie klas modeli.
#Po uruchomieniu aplikacji z pustą bazą danych wszystkie tabele powinny zostać utworzone.
admin.autodiscover()

admin.site.register(AppUser)
