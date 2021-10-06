from django.urls import path
from news.views import news, new_detail

app_name = 'news'

urlpatterns = [
    path('', news, name='index'),
    path('<int:new_id>/', new_detail, name='new_detail'),
    path('page/<int:page>/', news, name='page')
]
