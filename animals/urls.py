from django.urls import path
from animals import views


app_name = 'animals'
urlpatterns = [

    #Home
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),


    #Authentication/login
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    

     # Account
    path('account/', views.account, name='account'),
    path('account/animalprofile/', views.animal_profile, name='animal_profile'),
    
    # Animals
    path('animals/', views.animals, name='animals'),
    path('animals/recommended/', views.recommended, name='recommended'),
    
    # Help
    path('help/about/', views.about, name='about'),
    path('help/faq/', views.faq, name='faq'),
    
]