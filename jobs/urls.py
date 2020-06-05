from rest_framework import routers
from jobs.api import JobViewSet, ServicePointViewSet

router = routers.DefaultRouter()
router.register('api/jobs', JobViewSet, 'jobs')
router.register('api/servicepoints', ServicePointViewSet, 'servicepoints')

urlpatterns = router.urls
