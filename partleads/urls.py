from django.urls import path

from partleads.views import CandidateView

urlpatterns = [
    path('<str:position>', CandidateView.as_view())
]