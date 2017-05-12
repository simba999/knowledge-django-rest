from rest_framework import serializers
from api.models import Category, User
from solutions.models import Solution, Notebook, DataSet, Price, Performance, MetaEnsemble, Ensemble


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('id', 'category', 'user', 'usergroup_ID', 'type', 'parent', 'notebook', 'library_id', 'price', 'workflow_id', 
                'tags', 'name', 'title', 'description', 'rating', 'score', 'ensemble', 'metaensemble', 'dataset',
                'author', 'status', 'created_at', 'updated_at')
        # depth = 1


class SolutionAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('category', 'user', 'usergroup_ID', 'type', 'parent', 'notebook', 'library_id', 'price', 'workflow_id', 
                'tags', 'name', 'title', 'description', 'rating', 'score', 'ensemble', 'metaensemble', 'dataset',
                'author', 'status', 'created_at', 'updated_at')
        depth = 1


class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('category', 'solution', 'parent', 'type', 'jupyternotebook_ID', 'graphdatabase_ID', 'performance', 
            'price', 'accessparameters', 'description', 'datasource', 'datafields', 'language', 'author', 'status',
            'created_at', 'updated_at')


class NotebookAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('category', 'solution', 'parent', 'type', 'jupyternotebook_ID', 'graphdatabase_ID', 'performance', 
            'price', 'accessparameters', 'description', 'datasource', 'datafields', 'language', 'author', 'status',
            'created_at', 'updated_at')
        # depth = 1/


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at') 


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = ('id', 'user', 'category', 'type', 'price', 'accessparameters', 'rating', 'description', 'datafields',
                'author', 'created_at', 'updated_at') 
        # depth = 1


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id', 'user', 'solution', 'notebook', 'datafield', 'dataset', 'price', 'created_at', 'updated_at')


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ('id', 'user', 'usergroup', 'solution', 'notebook', 'ensemble', 'results', 'ABTest', 'PredictionAccuracyScore', 'ChangefromPrevious', 'PredictedImpact', 'RecordsinFile', 'DateRun', 'Date', 'created_at', 'updated_at')
        depth = 1


class AnomalySerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ('id', 'PredictionAccuracyScore', 'ChangefromPrevious', 'PredictedImpact', 'RecordsinFile', 'DateRun')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'parent_id', 'group', 'tags', 'name', 'email', 'password', 'remember_token', 'image', 'profile_name',
                'profile_description', 'api_paypal', 'api_payment', 'commissions', 'commission_rate', 'commission_total', 'commission_monthtodata', 'number_transaction', 'trend',
                'potential_place', 'potential_earning', 'total_commission', 'total_purchase', 'proj_earning_to_date', 'proj_earning_overall',
                'proj_place_to_date', 'proj_place_overall', 'noteworthy', 'redeem_state', 'datascientist_reg', 'created_at', 'updated_at')


class MetaEnsembleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaEnsemble
        fields = ('id', 'collection_id', 'foreign_id', 'foreign_type', 'name', 'status', 'created_at', 'updated_at')


class EnsembleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ensemble
        fields = ('id', 'user', 'usergroup', 'parent', 'foreign_id', 'foreign_type', 'performance', 'name', 'status', 'created_at', 'updated_at')

# class AnomalySerializer(serializers.Serializer):
#     fields = ('id', 'PredictionAccuracyScore', 'ChangefromPrevious', 'PredictedImpact', 'RecordsinFile', 'DateRun')   
#     id = serializers.IntegerField(read_only=True)
#     PredictionAccuracyScore = serializers.IntegerField(default=0)
#     ChangefromPrevious = serializers.IntegerField(default=0)
#     PredictedImpact = serializers.IntegerField(default=0)
#     RecordsinFile = serializers.IntegerField(default=0)
#     DateRun = serializers.DataTimeField(required=False, alllow_blank=True)
