from django.urls import path
from animals import views

app_name = 'animals'

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),

    # Authentication/login
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Account
    path('account/', views.account, name='account'),
    path('account/edit/', views.edit_profile, name='edit_profile'),
    path('account/add-animal/', views.add_animal, name='add_animal'),

    # Animals
    path('animals/', views.animals, name='animals'),
    path('animals/recommended/', views.recommended, name='recommended'),

    # Help
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),

    # Animal profile
    path('animal/<int:animal_id>/', views.animal_profile, name='animal_profile'),
    path('animal/<int:animal_id>/edit/', views.edit_animal, name='edit_animal'),
    path('animal/<int:animal_id>/adopt/', views.request_adoption, name='request_adoption'),
    path('animal/<int:animal_id>/favourite/', views.add_favourite, name='add_favourite'),
    path('animal/<int:animal_id>/unfavourite/', views.remove_favourite, name='remove_favourite'),
    path('animal/<int:animal_id>/mark-adopted/', views.mark_adopted, name='mark_adopted'),
    path('animal/<int:animal_id>/mark-available/', views.mark_available, name='mark_available'),

    # Admin
    path('adoption-request/<int:request_id>/<str:status>/', views.process_adoption, name='process_adoption'),

    #delte/romve button
    path('adoption-request/<int:request_id>/<str:status>/', views.process_adoption, name='process_adoption'),
    path('animal/<int:animal_id>/delete/', views.delete_animal, name='delete_animal'),
    
   
]