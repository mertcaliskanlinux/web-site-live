from django.urls import path
from blog.views import blog,PostDetailView

urlpatterns = [
    path('',blog,name="blog"),
    path('<slug>/',PostDetailView.as_view(),name="post")
]
1