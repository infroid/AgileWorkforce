from Member.models import Country
from Member.serializers import CountrySerializer
from rest_framework import viewsets

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer