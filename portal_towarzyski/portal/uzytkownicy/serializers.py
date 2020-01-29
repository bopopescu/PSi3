from django.contrib.auth.models import User

from .models import Zainteresowania, Dane_uzytkownika, Znajomi, Znajomi_has_zainteresowania_uzytkownik
from rest_framework import serializers

class ZainteresowaniaSerializer(serializers.Serializer):
    class Meta:
        model = Zainteresowania
        fields = '_all_'

class Dane_uzytkownikaSerializer(serializers.Serializer):
    class Meta:
        model = Dane_uzytkownika
        fields = '_all_'
class ZnajomiSerializer(serializers.Serializer):
    class Meta:
        model = Znajomi
        fields = '_all_'
class Znajomi_has_zainteresowania_uzytkownikSerializer(serializers.Serializer):
    class Meta:
        model = Znajomi_has_zainteresowania_uzytkownik
        fields = '_all_'
class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '_all_'