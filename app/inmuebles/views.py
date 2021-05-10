# Django REST Framework
from rest_framework import viewsets
from rest_framework import mixins
from inmuebles.serializers import StatusHistorySerializer

# models imports
from inmuebles.models import StatusHistory


class InmueblesViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = StatusHistorySerializer

    def get_queryset(self):
        """
        defining a queryset function to filter unwanted status
        and also aplying additional filters
        year, city, status
        """
        queryset = StatusHistory.objects.\
            order_by('-update_date').filter(status__pk__in=[3, 4])
        year = self.request.query_params.get('year')
        city = self.request.query_params.get('city')
        status = self.request.query_params.get('status')
        if year is not None:
            queryset = queryset.filter(property__year=year)
        if city is not None:
            queryset = queryset.filter(property__city=city)
        if status is not None:
            queryset = queryset.filter(status__name=status)
        return queryset
