from django.conf.urls import include, url
from index import views

urlpatterns = [
    url(r'^test$',views.test),
]
