from django.urls import path

from . import views

app_name = 'wechat'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<manager_id>/', views.detail, name='detail'),
    path('dengluzhuce_login/', views.dengluzhuce_login, name='dengluzhuce_login'),
    #path('<CharField:manager_id>/results/', views.results, name='results'),
    #path('<CharField:manager_id/vote/', views.vote, name='vote'),
]