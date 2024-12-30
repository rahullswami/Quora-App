from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('following/', following, name='following'),
    path('answer/<int:question_id>/', answer, name='answer'),
    path('notification/', notification, name='notification'),
    path('spaces/', spaces, name='spaces'),
    path('profile/', profile, name='profile'),

    # foolowing paths ?
    path('following/', following, name='following'),
    path('follow/<int:user_id>/', follow, name='follow'),
    path('unfollow/<int:user_id>/', unfollow, name='unfollow'),

    # delete urls 
    path('delete_question/<int:question_id>/', delete_question, name='delete_question'),
    path('delete_answer/<int:answer_id>/', delete_answer, name='delete_answer'),
    path('delete_space/<int:space_id>/', delete_space, name='delete_space'),
    
]

# username = root
# password = root