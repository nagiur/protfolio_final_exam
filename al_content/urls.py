from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('createCategory/', views.createCatagory, name='createcategory'),
    path('createProject/', views.createProject, name='createproject'),
    path('createskill/', views.createskill, name='createSkill'),
    path('createblog/', views.createblog, name='createBlog'),
    path('details/<int:id>', views.detalils.as_view(), name='details'),
    path('createCV/', views.CVview.as_view(), name='CV'),
    path('blog/', views.showBlock, name='showBlock'),
    path('contact_us/', views.contact, name='contact'),
    path('CV/', views.cvx, name='mycv'),
    path('skills/', views.skilx, name='skills'),
    
]
