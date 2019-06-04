from django.urls import path,include
from .views import FileView,DetailView,xyz,TemplateView,abcView,IdchangerView,SubmitView
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('activate',abcView)


urlpatterns = [
  # path('', include(router.urls)),
  path('upload/', FileView.as_view()),
  path('Detail/', DetailView.as_view()),
  path('systemtemplate/', xyz.as_view()),
  path('viewtemplate/',TemplateView.as_view()),
  path('activate/', abcView.as_view()),
  path('changer/',IdchangerView.as_view()),
  path('temp_submit/',SubmitView.as_view()),
  # path('mit/', mitView.as_view()),


]
