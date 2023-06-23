from django.urls import path
from .import views


urlpatterns=[

    path('login/',views.userLogin,name='login'),
    path('signup/',views.signup,name='signup'),
    path('viewpost/',views.Post_list,name='postlist'),
    path('createpost/',views.Post_creation,name='postcreat')
]