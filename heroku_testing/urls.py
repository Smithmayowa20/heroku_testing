"""heroku_testing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail
from django.conf.urls.static import static
from django.conf import settings

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        # the named URL that we want to redirect to after
        # successful registration
        return ('user_feed')

app_name = 'services'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^summernote/',include('django_summernote.urls')),
	url(r'^accounts/register/$', MyRegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	url(r'', include('services.urls')),
	url(r'^oauth/', include('social_django.urls', namespace='social')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)