from rest_framework import serializers
from Member.models import Country, State, City, Job, Member

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('code', 'name')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('code', 'name', 'country')