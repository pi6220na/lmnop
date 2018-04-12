"""lmnop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from api.resources import ArtistResource, VenueResource, ShowResource
from tastypie.api import Api

artist_resource = ArtistResource()
venue_resource = VenueResource()
show_resource = ShowResource()


v1_api = Api(api_name='v1')
v1_api.register(ArtistResource(), canonical=True)
v1_api.register(VenueResource(), canonical=True)
v1_api.register(ShowResource(), canonical=True)


# private_api = Api(api_name='v1')
# private_api.register(MoleculeDictionaryResource(), canonical=True)
#
#
# url(r'^api/', include(private_api.urls)),

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
    url(r'^artist/', include(artist_resource.urls)),
    url(r'^venue/', include(venue_resource.urls)),
    url(r'^show/', include(show_resource.urls)),
]

