
from django.urls import path
from .views import StationList,LowCostPath

urlpatterns = [
    path('api/stations/',StationList.as_view()),
    path('api/lowcostpath/',LowCostPath.as_view())
]
