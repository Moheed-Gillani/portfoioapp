from django.urls import path,include
from . import views
from personal_portfolio import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('add_reviews/',views.add_reviews,name='add_reviews'),
    path('accounts/',include("django.contrib.auth.urls")),
    path('oauth/',include('social_django.urls',)),
    path('register/',views.register,name="register"),
    path('subscribe',views.subscribe,name='subscribe'),
    path('<int:id>',views.detail,name='detail'),
    path('<int:id>/add_comments',views.add_comments,name='add_comments'),
    path('show_comments',views.show_comments,name='show_comments'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

