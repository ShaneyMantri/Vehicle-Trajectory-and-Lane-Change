from django.urls import path
from . import views
from django.urls import include
from rest_framework import routers  # Responsible fr generating urls for models
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register('images', views.ImageView)
router.register('user', views.UserView)


urlpatterns = [
    path('', views.home, name="MPHome"),
    path('api/', include(router.urls)),
    path('photoUpload', views.photoUpload, name="PhotoUpload"),
    path('register_user', views.register_user, name="APIRegister"),  #API for register
    path('login_api', views.verify_login, name="APILogin"),     #API for login
    # path('image_upload_api', views.image_upload_api, name="ImageUploadAPI"),    #API for image upload(not working)
    path('image_upload_api', views.image_upload_api, name='ImageUploadAPI')

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

