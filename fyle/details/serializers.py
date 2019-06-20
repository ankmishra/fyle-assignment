from rest_framework import serializers
from .models import Branches, Banks

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches