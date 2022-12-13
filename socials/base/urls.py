from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AddPostView,HomeView,EditProfilePageView,CreateProfilePageView,ShowProfilePageView,PasswordsChangeView,FriendView,AddCommentView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('login/', views.login,name='login'),
    path('error/', views.error,name='error'),
    path('logout/', views.logout,name='logout'),
    path('signup/', views.signup,name='signup'),
    # path('friends/', views.friends,name='friends'),
    path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(),name='edit_profile_page'),
    path('<int:pk>/profile/',ShowProfilePageView.as_view(),name='show_profile_page'),
    path('create_profile_page/',CreateProfilePageView.as_view(),name='create_profile_page'),
    path('add_post/',AddPostView.as_view(),name="add_post"),
    path('password/',PasswordsChangeView.as_view(template_name='base/change-password.html')),
    path('password_success/', views.password_success, name="password_success"),
    path('friends/',FriendView.as_view(),name='friends'),
    path('post/<int:pk>/comment/',AddCommentView.as_view(),name='add_comment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)