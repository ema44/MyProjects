from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView



urlpatterns = [

    path('',views.home, name='home-center' ),
    path('regis/',views.SignUpView.as_view(), name='regis-center' ),
    path('dashboard/', views.dashboard, name='dashboard-center'),
    path('userlist/',views.userlist, name='userlist-center' ),
    path('create/',views.CenterCreate.as_view(), name='create-center' ),
    path('viewall/',views.TotalList.as_view(), name='viewall-center' ),
    path('<int:pk>/',views.CenterDetailView.as_view(), name='detail-center' ),
    path('<int:pk>/update/',views.CenterUpdateView.as_view(), name='update-center' ),
    path('success/',views.success, name='success-center' ),
    path('<int:pk>/delete/', views.CenterDeleteView.as_view(), name='delete-center'),
    path('removal/',views.removal, name='removal-center' ),
    path('saved/',views.SaveProfile, name='saved-center' ),
    path('profile/',TemplateView.as_view(template_name='YouthCenter/profile.html'), name='profile-center' ),

]