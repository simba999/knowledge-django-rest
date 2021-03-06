from rest_framework import serializers
from api.models import User
from api.models import Solution, Category, Notebook, DataSet, Price, Performance
from api.models import MetaEnsemble, Ensemble, Commission, Library, Vertical, SolutionNavigation
from django.contrib.auth.models import User as AdminMember
import json


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('id', 'category', 'user', 'usergroup_ID', 'type', 'parent', 'notebook', 'library', 'price', 'workflow_id', 
                'tags', 'name', 'title', 'description', 'rating', 'score', 'ensemble', 'metaensemble', 'dataset',
                'author', 'status', 'created_at', 'updated_at')
        depth = 1


class SolutionAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('id', 'category', 'user', 'usergroup_ID', 'type', 'parent', 'notebook', 'library', 'price', 'workflow_id', 
                'tags', 'name', 'title', 'description', 'rating', 'score', 'ensemble', 'metaensemble', 'dataset',
                'author', 'status', 'created_at', 'updated_at')
        depth = 1


class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('id', 'category', 'solution', 'parent', 'type', 'jupyternotebook_ID', 'graphdatabase_ID', 'performance', 
            'price', 'accessparameters', 'description', 'datasource', 'datafields', 'language', 'author', 'status',
            'ensemble', 'metaensemble', 'created_at', 'updated_at')


class NotebookAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('id', 'category', 'solution', 'parent', 'type', 'jupyternotebook_ID', 'graphdatabase_ID', 'performance', 
            'price', 'accessparameters', 'description', 'datasource', 'datafields', 'language', 'author', 'status',
            'ensemble', 'metaensemble', 'created_at', 'updated_at')
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
        fields = ('id', 'parent_id', 'group', 'tags', 'image', 'profile_name',
                'profile_description', 'api_paypal', 'api_payment', 'commissions', 'commission_rate', 'commission_total', 'commission_monthtodata', 'number_transaction', 'trend',
                'potential_place', 'potential_earning', 'total_commission', 'total_purchase', 'proj_earning_to_date', 'proj_earning_overall',
                'proj_place_to_date', 'proj_place_overall', 'noteworthy', 'redeem_state', 'datascientist_reg', 'is_authenticated'
                )
        depth = 3


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminMember
        fields = ('username', 'password', 'email')
        depth = 3


class AdminMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # users = TrackListingField()

    class Meta:
        model = AdminMember
        fields = ('username', 'password', 'email', 'user')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print "User_DATA"
        print json.loads(json.dumps(user_data))
        print "**** Validate *****"
        print validated_data
        user = AdminMember.objects.create(**validated_data)
        User.objects.create(user=user, **user_data)
        return user

class MetaEnsembleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaEnsemble
        fields = ('id', 'collection_id', 'foreign_id', 'foreign_type', 'name', 'status', 'created_at', 'updated_at')


class EnsembleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ensemble
        fields = ('id', 'user', 'usergroup', 'parent', 'foreign_id', 'foreign_type', 'performance', 'name', 'status', 'notebook', 'created_at', 'updated_at')


class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = ('user', 'solution', 'product_sales')


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('id', 'name', 'category', 'vertical')
        depth = 1


class VerticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vertical
        fields = ('id', 'name')


class HomeSerializer(serializers.ModelSerializer):
    vertical = VerticalSerializer()
    solution = SolutionSerializer()
    library = LibrarySerializer()

    class Meta:
        model = Category
        fields = ('id', 'name', 'vertical', 'solution', 'library')

class SolutionNavigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionNavigation
        fields = ('vertical', 'cateogry', 'category_child', 'library', 'solution', 'solution_child', 'created_at', 'updated_at')
