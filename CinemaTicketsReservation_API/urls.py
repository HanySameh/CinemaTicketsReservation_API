"""CinemaTicketsReservation_API URL Configuration

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
from django.urls import path,include
from tickets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests',views.Viewsets_guest)
router.register('movie',views.Viewsets_movie)
router.register('reservation',views.Viewsets_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1
    path('django/jsonresponsenomodel/', views.no_rest_no_model),

    # 2
    path('django/jsonresponsefrommodel/', views.no_rest_from_model),

    # 3.1 GET POST from rest framework function based view @api_view
    path('rest/fbv/', views.fbv_list),

    # 3.2 GET PUT DELETE from rest framework function based view @api_view
    path('rest/fbv/<int:pk>', views.fbv_pk),

    # 4.1 GET POST from rest framework class based view APIView
    path('rest/cbv/', views.CBV_List.as_view()),

    # 4.2 GET PUT DELETE from rest framework class based view APIView
    path('rest/cbv/<int:pk>', views.CBV_pk.as_view()),
    
    #5.1 GET POST from rest framework class based view mixins
    path('rest/mixins/', views.Mixins_list.as_view()),

    #5.2 GET PUT DELETE from rest framework class based view mixins
    path('rest/mixins/<int:pk>', views.Mixins_pk.as_view()),
    
    #6.1 GET POST from rest framework class based view generics
    path('rest/generics/', views.Generics_list.as_view()),

    #6.2 GET PUT DELETE from rest framework class based view generics
    path('rest/generics/<int:pk>', views.Generics_pk.as_view()),
    
    #viewsets
    path('rest/viewsets/',include(router.urls)),
    
    #8 find movie 
    path('fbv/findmovie', views.find_movie),

    #9 new reservation
    path('fbv/newreservation',views.new_reservation),

]
