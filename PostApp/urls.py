from django.urls import path
from .import views
from .views import userLogout
from .views import userLogin



urlpatterns=[

    path('login/',userLogin,name='login'),
    path('signup/',views.signup,name='signup'),
    path('viewpost/',views.Post_list,name='postlist'),
    path('createpost/',views.Post_creation,name='postcreat'),
    path('logout/', userLogout, name='logout'),
]