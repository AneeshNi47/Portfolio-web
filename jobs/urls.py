from rest_framework import routers
from jobs.api import JobViewSet

router = routers.DefaultRouter()
router.register('api/jobs', JobViewSet, 'jobs')

urlpatterns = router.urls
