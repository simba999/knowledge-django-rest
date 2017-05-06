from rest_framework import serializers
from users.models import Category
from solutions.models import Solution


class SolutionSerializer(serializers.Serializer):
    class Meta:
        model = Solution
        fields = ('id', 'categpry', 'type_id', 'solutionparent', 'price', 'workflow_id', 'tags', 'name', 'title', 'description', 'rating', 'score', 'author', 'status', 'created_at', 'updated_at')
