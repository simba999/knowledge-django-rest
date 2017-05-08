from rest_framework import serializers
from api.models import Category
from solutions.models import Solution, Notebook


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('category', 'user', 'usergroup_ID', 'type', 'solutionparent', 'price', 'workflow_id', 'tags',
                 'name', 'title', 'description', 'rating', 'score', 'author', 'status', 'created_at', 'updated_at')


class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('solution', 'category', 'parent', 'type', 'jupyternotebook_ID', 'graphdatabase_ID', 'performance', 
            'price', 'accessparameters', 'description', 'datafields', 'language', 'author', 'status', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at') 

