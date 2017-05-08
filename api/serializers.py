from rest_framework import serializers
from api.models import Category
from solutions.models import Solution, Notebook


class SolutionSerializer(serializers.Serializer):
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = Solution
        fields = ('id', 'category', 'type_id', 'solutionparent', 'price', 'workflow_id', 'tags',
                 'name', 'title', 'description', 'rating', 'score', 'author', 'status', 'created_at', 'updated_at')


class NotebookSerializer(serializers.Serializer):
    class Meta:
        model = Notebook
        fields = ('solution', 'category', 'type_id', 'jupyternotebook_ID', 'graphdatabase_ID', 'performance', 
            'price', 'accessparameters')

