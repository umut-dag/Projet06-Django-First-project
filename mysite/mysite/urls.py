"""mysite URL Configuration"""

from django.contrib import admin
from django.urls import include, path
""" Il faut toujours utiliser include() lorsque l’on veut inclure d’autres motifs d’URL.
admin.site.urls est la seule exception à cette règle. """

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sondage/', include('polls.urls'))
]