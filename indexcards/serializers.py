from indexcards.models import IndexcardsItem
from rest_framework import serializers

class IndexcardsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexcardsItem
        fields = '__all__'