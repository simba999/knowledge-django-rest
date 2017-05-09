from rest_framework import serializers
from api.models import Category
from solutions.models import Solution, Notebook, DataSet, Price


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('category', 'user', 'usergroup_ID', 'type', 'solutionparent', 'price', 'workflow_id', 'tags',
                 'name', 'title', 'description', 'rating', 'score', 'author', 'status', 'created_at', 'updated_at')
        # depth = 1


class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('category', 'solution', 'parent', 'type', 'jupyternotebook_ID', 'graphdatabase_ID', 'performance', 
            'price', 'accessparameters', 'description', 'datafields', 'language', 'author', 'status',
            'created_at', 'updated_at')
        # depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at') 


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = ('id', 'user', 'category', 'type', 'price', 'accessparameters', 'rating', 'description', 'datafields', 'author', 'created_at', 'updated_at') 
        # depth = 1


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id', 'user', 'price', 'created_at', 'updated_at')

