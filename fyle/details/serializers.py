from rest_framework import serializers
from .models import Branches, Banks

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        bank = BankSerializer()
        model = Branches
        fields = ('ifsc', bank, 'branch', 'address', 'city', 'district','state')