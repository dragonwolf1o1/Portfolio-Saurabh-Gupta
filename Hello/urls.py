from django.contrib import admin
from django.urls import path,include

admin.site.site_header="Saurabh Admin"
admin.site.site_title="Saurabh Admin Page"
admin.site.index_title="Saurabh Authentication"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
