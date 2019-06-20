from rest_framework import serializers
from .models import Branches, Banks

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = ('name',)

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        model = Branches
        fields = ('ifsc', 'bank', 'branch', 'address', 'city', 'district','state')

class BranchReadSerializer(BranchSerializer):
    bank = BankSerializer()