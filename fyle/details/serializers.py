from rest_framework import serializers
from .models import Branches, Banks

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks

class BranchSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    class Meta:
        model = Branches
        fields = ('ifsc', bank, 'branch', 'address', 'city', 'district','state')