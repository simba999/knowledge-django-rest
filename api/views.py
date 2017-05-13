from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password, make_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import permissions
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.decorators import api_view
from solutions.models import Solution, Category, Performance, Notebook, DataSet, Price, Ensemble, MetaEnsemble
from api.models import User
from api.serializers import SolutionSerializer, NotebookSerializer, SolutionAllSerializer, AnomalySerializer
from api.serializers import UserSerializer, MetaEnsembleSerializer, DatasetSerializer, NotebookAllSerializer
from api.serializers import CategorySerializer, DatasetSerializer, PriceSerializer, PerformanceSerializer, EnsembleSerializer
from rest_framework.renderers import JSONRenderer
import json
from django.db.models import Q
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
import pdb

SOLUTION_TYPE = {
    'Solution': 'Solution',
    'CustomSolution': 'CustomSolution',
    'SolutionLibrary': 'SolutionLibrary'
}

ENSEMBLE_TYPE = {
    'Ensemble': 0,
    'Solution': 1,
}

METAENSEMBLE_TYPE = {
    'Ensemble': 0,
    'Solution': 1,
}

FILTER_TYPE = {
    '=': '',
    '<': '__lt',
    '>': '__gt',
    'like': '__icontains'
}

def get_token(request, pk):
    try:
        return User.objects.values('rememeber_token').get(pk=pk)
    except User.DoesNotExist:
        return Http404


def get_solutions_by_user(user_id):
    try:
        return Solution.objects.filter(user__id=user_id)
    except Solution.DoesNotExist:
        raise Http404


def get_datasets_by_user(user_id):
    try:
        return DataSet.objects.filter(user__id=user_id)
    except Solution.DoesNotExist:
        raise Http404


def get_solutionlibrary_by_user(user_id):
    try:
        return Solution.objects.filter(user__id=user_id, type__name=SOLUTION_TYPE['SolutionLibrary'])
    except Solution.DoesNotExist:
        raise Http404


# @csrf_exempt
class AuthenticationView(APIView):
    def get_object(self, username):
        try:
            return User.objects.get(name=username)
        except User.DoesNotExist:
            raise Http404 

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response("Please insert username or password", status=status.HTTP_204_NO_CONTENT)
        
        user = self.get_object(username)
        pwd_valid = check_password(password, user.password)
        if pwd_valid:
            user.remember_token = uuid.uuid4()
            user.save()
            return Response({'token': user.remember_token}, status=status.HTTP_200_OK)
        else:
            return Response("Authentication Error", status=status.HTTP_401_UNAUTHORIZED)


# Create your views here.
# Solution APIs Begins
class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

    def get_token(self):
        return '123'

    def list(self, request):
        solutions = Solution.objects.all()
        serializer = SolutionSerializer(solutions, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        token = ''
        try:
            token = request.META['HTTP_TOKEN']
        except:
            raise exceptions.NotAuthenticated('Token is missed')

        if token == self.get_token():
            serializer = SolutionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Token is wrong or expired", status=status.HTTP_401_UNAUTHORIZED)


class SolutionDetailView(APIView):
    def get_object(self, pk):
        try:
            return Solution.objects.get(pk=pk)
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, pid, format=None):
        solution = self.get_object(pid)
        serializer = SolutionSerializer(solution)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


class SolutionLibraryView(APIView):
    def get_object(self, pk):
        try:
            return Solution.objects.filter(category__id=pk)
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, category_id, format=None):
        solution = self.get_object(category_id)
        print solution
        serializer = SolutionSerializer(solution, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


class SolutionLibraryAddView(APIView):
    def post(self, request):
        serializer = SolutionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#GET /solution/customsolution/{user_id}
class CustomSolutionViewByUser(APIView):
    def get_object(self, id):
        try:
            return Solution.objects.filter(user=id, type__name="CustomSolution")
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        solution = self.get_object(user_id)
        serializer = SolutionSerializer(solution, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


#GET /solution/customsolution/group/{group_id}
class CustomSolutionViewByGroup(APIView):
    def get_object(self, id):
        try:
            return Solution.objects.filter(usergroup_ID=id, type__name="CustomSolution")
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, group_id, format=None):
        solution = self.get_object(group_id)
        serializer = SolutionSerializer(solution, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


#GET /solution/customsolution/parent/{id} //mode
class CustomSolutionViewByParent(APIView):
    def get_object(self, id):
        try:
            return Solution.objects.filter(parent__pk=id, type__name="CustomSolution")
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, parent_id, format=None):
        solution = self.get_object(parent_id)
        serializer = SolutionSerializer(solution, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


#GET return solution object by solution id
class SolutionEnsembleView(APIView):
    def get_object(self, id):
        try:
            return Ensemble.objects.filter(foreign_id=id, foreign_type=ENSEMBLE_TYPE['Solution'])
        except Ensemble.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        ensembles = self.get_object(id)
        serializer = EnsembleSerializer(ensembles, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


class SolutionCategoryView(APIView):
    def get_object(self, id):
        try:
            return Solution.objects.filter(category=id)
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        solution = self.get_object(id)
        serializer = SolutionSerializer(solution, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


class SolutionTypeView(APIView):
    def get_object(self, id):
        try:
            return Solution.objects.filter(type=id)
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        solution = self.get_object(id)
        serializer = SolutionSerializer(solution, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


class SolutionAllView(APIView):
    def get_object(self, id):
        try:
            return Solution.objects.filter(pk=id)
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        solution = self.get_object(id)
        serializer = SolutionAllSerializer(solution, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


class ChildSolutionView(APIView):
    def get_object(self, id):
        try:
            return Solution.objects.filter(parent=id)
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        solution = self.get_object(id)
        serializer = SolutionAllSerializer(solution, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


class ParentSolutionView(APIView):
    def get_object(self, id):
        try:
            parent_id = Solution.objects.get(pk=id)
            print Solution.objects.get(pk=id)
            return Solution.objects.get(pk=id)
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        solution = self.get_object(id)
        serializer = SolutionAllSerializer(solution)
        return Response(serializer.data)


class SearchSolutionView(APIView):
    def get_token(self):
        return '123'

    def  post(self, request ,format=None):
        token = ''
        term = request.data['term']
        type_id = request.data['type_id']
        try:
            token = request.META['HTTP_TOKEN']
        except:
            raise exceptions.NotAuthenticated('Token is missed')

        query = Q()
        if token == self.get_token():
            query |= Q(name__icontains=term)
            query |= Q(title__icontains=term)
            query |= Q(description__icontains=term)
            
            solutions = Solution.objects.all()
            try:     
                solutions = solutions.filter(query).filter(type=type_id)
            except Solution.DoesNotExist:
                raise Http404

            serializer = SolutionAllSerializer(solutions, many=True)
            return Response(serializer.data)

        else:
            return Response("error", status=status.HTTP_401_UNAUTHORIZED)


class FilterSolutionView(APIView):
    def get_token(self):
        return '123'

    def  post(self, request, format=None):
        token = ''
        value = request.data['value']
        try:
            token = request.META['HTTP_TOKEN']
        except:
            raise exceptions.NotAuthenticated('Token is missed')

        try:
            filter_name = request.data['filter']
            operator = request.data['operator']
        except:
            raise exceptions.NotAuthenticated('filter or operator is missed')

        query = Q()
        query_name = filter_name + FILTER_TYPE[operator]
        if token == self.get_token():
            query |= Q(query_name=value)
            
            solutions = Solution.objects.all()
            try:     
                solutions = solutions.filter(query)
            except Solution.DoesNotExist:
                raise Http404

            serializer = SolutionAllSerializer(solutions, many=True)
            return Response(serializer.data)

        else:
            return Response("error", status=status.HTTP_401_UNAUTHORIZED)

#POST /solution/customsolution
# class CustomSolutionAddView(APIView):
#     def get(self, reqest):
#         pass

#     def post(self, request, format=None):
#         print "TYPE: " + request.data
#         type = SolutionType.objects.filter(name='CustomSolution')
#         print "TYPE: " + request.data
#         request.data['type'] = type
#         print "New Type: " + request.data
#         serializer = SolutionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# mode
@api_view(['POST'])
def CustomSolutionAddView(request):
    type = SolutionType.objects.filter(name='CustomSolution')
    request.data['type'] = type
    serializer = SolutionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Solution APIs End


#Category APIs
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


class CategoryNotebookView(APIView):
    def get_notebook_objects(self, pk):
        try:
            return Notebook.objects.filter(category__id=pk)
        except Notebook.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        notebooks = self.get_notebook_objects(id)
        
        serializer = NotebookSerializer(notebooks, many=True)
        return Response(serializer.data)


class CategoryDatasetView(APIView):
    def get_notebook_objects(self, pk):
        try:
            return DataSet.objects.filter(category__id=pk)
        except DataSet.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        datasets = self.get_notebook_objects(id)
        
        serializer = DatasetSerializer(datasets, many=True)
        return Response(serializer.data)


class CategorySolutionView(APIView):
    def get_objects(self, id):
        try:
            return Solution.objects.filter(category__id=id)
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        solutions = self.get_objects(id)
        serializer = SolutionSerializer(solutions, many=True)
        return Response(serializer.data)


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    
    def list(self, request):
        prices = Price.objects.all()
        serializer = PriceSerializer(prices, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DatasetViewSet(viewsets.ModelViewSet):
    queryset = DataSet.objects.all()
    serializer_class = DatasetSerializer
    
    def list(self, request):
        datasets = DataSet.objects.all()
        serializer = DatasetSerializer(datasets, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = DatasetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

    def list(self, request):
        performances = Performance.objects.all()
        serializer = PerformanceSerializer(performances, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


class PerformanceNotebookView(APIView):
    def get_objects(self, notebook_id, user_id):
        try:
            return Performance.objects.filter(notebook__id=notebook_id).filter(user__id=user_id)
        except Performance.DoesNotExist:
            raise Http404

    def get(self, request, notebook_id, user_id, format=None):
        # notebooks = self.get_objects(notebook_id, user_id)
        datares = self.get_objects(notebook_id, user_id)
        
        serializer = PerformanceSerializer(datares, many=True)
        performance_lists = JSONRenderer().render(serializer.data)

        notebooks = []
        performance_lists = json.loads(performance_lists)
        for performance in performance_lists:
            notebooks.append(performance['notebook'])

        return Response(notebooks)


class PerformanceEnsembleView(APIView):
    def get_objects(self, ensemble_id, user_id):
        try:
            return Performance.objects.filter(ensemble__id=ensemble_id, user__id=user_id)
        except Performance.DoesNotExist:
            raise Http404

    def get(self, request, ensemble_id, user_id, format=None):
        notebooks_list = self.get_objects(ensemble_id, user_id)
        serializer = PerformanceSerializer(notebooks_list, many=True)
        performance_lists = JSONRenderer().render(serializer.data)

        notebooks = []
        performance_lists = json.loads(performance_lists)
        for performance in performance_lists:
            notebooks.append(performance['notebook'])

        return Response(notebooks)


class PerformanceSolutionView(APIView):
    def get_objects(self, solution_id, user_id):
        try:
            return Performance.objects.filter(solution__id=solution_id, user__id=user_id)
        except Performance.DoesNotExist:
            raise Http404

    def get(self, request, solution_id, user_id, format=None):
        notebooks_list = self.get_objects(solution_id, user_id)
        serializer = PerformanceSerializer(notebooks_list, many=True)
        performance_lists = JSONRenderer().render(serializer.data)

        notebooks = []
        performance_lists = json.loads(performance_lists)
        for performance in performance_lists:
            notebooks.append(performance['notebook'])

        return Response(notebooks)


class AnomalyView(APIView):
    # serializer_class = PerformanceSerializer

    def get_object(self, id):
        try:
            return Performance.objects.get(pk=id)
        except Performance.DoesNotExist:
            raise Http404
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id, format=None):
        performance = self.get_object(id)
        serializer = AnomalySerializer(performance)
        # data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def post(self, request, id, format=None):      
        token = request.data['token']
        if token == '123':
            print "TOken succuess"
            data = request.data
            print data
            performance = self.get_object(id)
            serializer = PerformanceSerializer(performance, data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response("succes", status=status.HTTP_201_CREATED)
            else:
                return Response("update eroor")
        else:
            return Response("not token", status=status.HTTP_400_BAD_REQUEST)


# Notebook APIs
class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer
    
    def list(self, request):
        notebooks = Notebook.objects.all()
        serializer = NotebookSerializer(notebooks, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


# User Begin
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.AllowAny,)

    def get_token(self):
        return '123'

    def list(self, request):
        users = User.objects.all()
        for user in users:
            user.password = make_password(user.password)
            user.save()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        token = ''
        try:
            token = request.META['HTTP_TOKEN']
        except:
            raise exceptions.NotAuthenticated('Token is missed')

        if token == self.get_token():
            request.data['password'] = make_password(password)
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Token is wrong or expired", status=status.HTTP_401_UNAUTHORIZED)


class UserViewTypesByUser(APIView):
    def get(self, request, user_id, type, format=None):
        if type == "solutions":
            solutions = get_solutions_by_user(user_id)
            serializer = SolutionSerializer(solutions, many=True)
            return Response(serializer.data)
        
        if type == "datasets":
            datasets = get_datasets_by_user(user_id)
            serializer = DatasetSerializer(datasets, many=True)
            return Response(serializer.data)

        if type == "solutionlibrary":
            datasets = get_solutionlibrary_by_user(user_id)
            serializer = SolutionSerializer(datasets, many=True)
            return Response(serializer.data)

        return Response("Request Error", status=status.HTTP_400_BAD_REQUEST)


class UserSolutionLibraryViewById(APIView):
    def post(self, request, id, format=None):
        solution_type = SolutionType.objects.filter(name=SOLUTION_TYPE['SolutionLibrary'])
        reqeust.data['type'] = solution_type
        print "Request: ", request.data
        serializer = SolutionSerializer(data=reqeust.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User end

# NOTEBOOK BEGINS
class NotebookViewTypesById(APIView):
    def get(self, request, id, type, format=None):
        if type == "ensemble":
            solutions = get_ensembles_by_id(id)
            serializer = SolutionSerializer(solutions, many=True)
            return Response(serializer.data)
        
        if type == "metaensemble":
            datasets = get_metaensembles_by_id(id)
            serializer = MetaEnsembleSerializer(datasets, many=True)
            return Response(serializer.data)

        if type == "solutionlibrary":
            datasets = get_solutionlibrary_by_user(user_id)
            serializer = SolutionSerializer(datasets, many=True)
            return Response(serializer.data)

        return Response("Request Error", status=status.HTTP_400_BAD_REQUEST)


class SearchNotebookView(APIView):
    def get_token(self):
        return '123'

    def post(self, request, format=None):
        token = ''
        term = request.data['term']
        try:
            token = request.META['HTTP_TOKEN']
        except:
            raise exceptions.NotAuthenticated('Token is missed')

        query = Q()
        if token == self.get_token():
            # query |= Q(name__icontains=term)
            query |= Q(description__icontains=term)
            
            notebooks = Notebook.objects.all()
            try:     
                notebooks = notebooks.filter(query)
            except Notebook.DoesNotExist:
                raise Http404

            serializer = NotebookAllSerializer(notebooks, many=True)
            return Response(serializer.data)

        else:
            return Response("error", status=status.HTTP_401_UNAUTHORIZED)


# DATASET BEGINS
class SearchDatasetView(APIView):
    def get_token(self):
        return '123'

    def post(self, request, format=None):
        token = ''
        term = request.data['term']
        try:
            token = request.META['HTTP_TOKEN']
        except:
            raise exceptions.NotAuthenticated('Token is missed')

        query = Q()
        if token == self.get_token():
            # query |= Q(name__icontains=term)
            query |= Q(description__icontains=term)
            
            datasets = DataSet.objects.all()
            try:     
                datasets = DataSet.objects.filter(query)
            except Notebook.DoesNotExist:
                raise Http404

            serializer = DatasetSerializer(datasets, many=True)
            return Response(serializer.data)

        else:
            return Response("error", status=status.HTTP_401_UNAUTHORIZED)


class SolutionDataSetView(APIView):
    def get_object(self, id):
        try:
            return DataSet.objects.filter(solution=id)
        except DataSet.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        datasets = self.get_object(id)
        serializer = DatasetSerializer(datasets, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


# ENSEMBLE BEGIN
class EnsembleViewSet(viewsets.ModelViewSet):
    queryset = Ensemble.objects.all()
    serializer_class = EnsembleSerializer
    # permission_classes = (permissions.AllowAny,)

    def get_token(self):
        return '123'

    def list(self, request):
        ensembles = Ensemble.objects.all()
        serializer = EnsembleSerializer(ensembles, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        token = ''
        try:
            token = request.META['HTTP_TOKEN']
        except:
            raise exceptions.NotAuthenticated('Token is missed')

        if token == self.get_token():
            serializer = EnsemblesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Token is wrong or expired", status=status.HTTP_401_UNAUTHORIZED)


class SearchEnsembleView(APIView):
    def get_token(self):
        return '123'

    def post(self, request, format=None):
        token = ''
        try:
            term = request.data['term']
        except:
            term = ''
        try:
            type_id = request.data['type_id']
        except:
            type_id = 0
        try:
            token = request.META['HTTP_TOKEN']
        except:
            raise exceptions.NotAuthenticated('Token is missed')

        query = Q()
        if token == self.get_token():
            query |= Q(name__icontains=term)
            # query |= Q(description__icontains=term)
            
            ensembles = Ensemble.objects.all()
            try:
                ensembles = Ensemble.objects.filter(query).filter(foreign_id=type_id)
            except Ensemble.DoesNotExist:
                raise Http404

            serializer = EnsembleSerializer(ensembles, many=True)
            return Response(serializer.data)

        else:
            return Response("error", status=status.HTTP_401_UNAUTHORIZED)


# METAENSEMBLE
class SolutionMetaEnsemblesView(APIView):
    def get_object(self, id):
        try:
            return MetaEnsemble.objects.filter(foreign_id=id, foreign_type=METAENSEMBLE_TYPE['Solution'])
        except MetaEnsemble.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        metaensembles = self.get_object(id)
        serializer = MetaEnsembleSerializer(metaensembles, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)