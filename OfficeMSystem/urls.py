from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import   TaskDetailsViewset, MessageViewset

router = DefaultRouter()
router.register(r'Message', MessageViewset)

router.register(r'TaskDetails', TaskDetailsViewset)

urlpatterns = [
    path('', include(router.urls)),
]
