from accounts.models import Client, Account

from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['code', 'balance', 'client']

class ClientSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['firstname', 'lastname', 'address', 'accounts']
