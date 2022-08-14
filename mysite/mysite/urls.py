"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import include, path



# Text to put at the end of each page's <title>.
#site_title = gettext_lazy("Django site admin")

# Text to put in each page's <h1>.
#site_header = gettext_lazy("Django administration")

# Text to put at the top of the admin index page.
#index_title = gettext_lazy("Site administration")

# https://stackoverflow.com/questions/4938491/django-admin-change-header-django-administration-text
admin.site.site_header = 'Polls site'                    # default: "Django Administration"
admin.site.index_title = 'Polls Administration'                 # default: "Site administration"
admin.site.site_title = 'Polls site admin'  # default: "Django site admin"

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
