from django.http import Http404, JsonResponse, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password, make_password
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User as AdminMember
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import permissions
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.decorators import api_view
from api.models import Solution, Category, Performance, Notebook, DataSet, Price, Ensemble, AnalyticsRecord
from api.models import User, MetaEnsemble, Commission, Vertical, Library, SolutionNavigation
from api.serializers import SolutionSerializer, NotebookSerializer, SolutionAllSerializer, AnomalySerializer
from api.serializers import UserSerializer, MetaEnsembleSerializer, DatasetSerializer, NotebookAllSerializer
from api.serializers import CommissionSerializer, AdminMemberSerializer, LibrarySerializer, VerticalSerializer, SolutionNavigationSerializer
from api.serializers import CategorySerializer, DatasetSerializer, PriceSerializer, PerformanceSerializer, EnsembleSerializer
from rest_framework.renderers import JSONRenderer
import json
from django.db.models import Q
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from functools import wraps
from authentication import ExampleAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
import json
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

OPERATOR_TYPE = {
    '=': '',
    '<': '__lt',
    '>': '__gt',
    'like': '__icontains'
}

OPERATOR_LIST = ['=', '<', '>', 'like']


def login_required():
    def login_decorator(function):
        @wraps(function)
        def wrapped_function(request):

            # if a user is not authorized, redirect to login page
            if 'user' not in request.session or request.session['user'] is None:
                return redirect("/login")
            # otherwise, go on the request
            else:
                return function(request)

        return wrapped_function

    return login_decorator


def app(request):
    context = {
        'permissions': 'permissions'
    }
    return render(request, 'app.html', context)


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


def get_user_by_pk(user_id):
    try:
        return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404


def get_user_by_name(username):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404


def get_notebook_by_user(user_id):
    try:
        return Notebook.objects.filter(user=user_id)
    except Notebook.DoesNotExist:
        raise Http404


def validate(val):
    try:
        return val.encode('utf-8')
    except Exception as e:
        return ''


# @csrf_exempt
class AuthenticationView(APIView):
    authentication_classes = (ExampleAuthentication,)
    serializer_class = UserSerializer

    def get_object(self, username):
        try:
            return User.objects.filter(username=username)
        except User.DoesNotExist:
            raise Http404 

    # @csrf_exempt
    def post(self, request):
        return Response(self.serializer_class(request.user).data)


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
        if request.user.is_authenticated():
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
    def  post(self, request, format=None):
        term = request.data['term']
        type_id = request.data['type_id']

        query = Q()
        if request.user.is_authenticated():
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
            raise exceptions.NotAuthenticated('Token is missed')


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


class category_datasetView(APIView):
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


class FilterNotebookView(APIView):
    FILTER_TYPE = ['type_id', 'ensemble_id', 'metaensemble_id', 'solutioncategory_id', 'user_id']   

    def get_token(self):
        return '123'

    def post(self, request):
        token = ''
        value = ''

        try:
            value = request.data['value']
        except:
            return Response("value error")

        try:
            filter_name = request.data.get('filter')
            operator = request.data.get('operator')
        except:
            return Response("filter or operator error")

        if operator not in OPERATOR_LIST or filter_name not in self.FILTER_TYPE:
            return Response('operator or filter is not correct', status=status.HTTP_400_BAD_REQUEST)

        if request.user.is_authenticated():
            raw_query = 'SELECT * FROM api_notebook WHERE ' + filter_name + operator + value;
            if value == '':
                notebooks = Notebook.objects.all()
            else:
                try:     
                    notebooks = Notebook.objects.raw(raw_query)
                except Notebook.DoesNotExist:
                    raise Http404

            serializer = NotebookSerializer(notebooks, many=True)
            return Response(serializer.data)

        else:
            return Response("error", status=status.HTTP_401_UNAUTHORIZED)


# User Begin
# @login_required()
class UserViewSet(viewsets.ModelViewSet):
    queryset = AdminMember.objects.all()
    serializer_class = AdminMemberSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self, request):
        users = AdminMember.objects.all()
        serializer = AdminMemberSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            request.data['password'] = make_password(request.data['password'])
            print "RequestData: "
            print request.data
            serializer = AdminMemberSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Token is wrong or expired", status=status.HTTP_401_UNAUTHORIZED)


class UserViewTypesByUser(APIView):
    def get_librarys_by_category(self, category_id):
        try:
            return Library.objects.filter(category=category_id)
        except Library.DoesNotExist:
            return None

    def get_solutions_by_library(self, library_id):
        solution_data = []
        parent_solutions = Solution.objects.filter(library=library_id)
        if not parent_solutions:
            solution_data = []
            return solution_data
        else:
            for parent_solution in json.loads(serializers.serialize('json', parent_solutions)):
                temp_parent_solution = {}
                temp_parent_solution = parent_solution
                # temp_parent_solution['id'] = parent_solution.id
                # temp_parent_solution['name'] = validate(parent_solution.name)

                chlid_solution_data = []
                child_solutions = Solution.objects.filter(parent=parent_solution["pk"])

                if not child_solutions:
                    chlid_solution_data = []
                else:
                    for child_solution in json.loads(serializers.serialize('json', child_solutions)):
                        temp_child_solution = {}
                        temp_child_solution = json.dumps(child_solution)
                        chlid_solution_data.append(temp_parent_solution)
                temp_parent_solution['Solution'] = json.dumps(chlid_solution_data)
                solution_data.append(temp_parent_solution)
            return solution_data

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

        # if type == "notebooks":
        #     notebooks = get_notebook_by_user(user_id)
        #     serializer = NotebookSerializer(notebooks, many=True)
        #     return Response(serializer.data)

        if type == "home":
            results = {}
            
            verticals = Vertical.objects.filter(user=user_id)
            if not verticals:
                return Response({})
            vertical_data = []
            parent_category_data = []

            for vertical in verticals:
                temp_vertical = {}
                temp_vertical["id"] = vertical.id
                temp_vertical["name"] = validate(vertical.name)

                categories = Category.objects.all() #filter(pk=vertical.category)
                for category in categories:
                    temp_parent_category = {}
                    temp_parent_category['id'] = category.id
                    temp_parent_category['name'] = validate(category.name)

                    child_category_data = []

                    sub_categories = Category.objects.filter(parent=category.id)

                    if not sub_categories:
                        temp_parent_category['Category'] = []
                        parent_category_data.append(temp_parent_category)
                    else:
                        for sub_category in sub_categories:
                            temp_child_category = {}
                            temp_child_category['id'] = category.id
                            temp_child_category['name'] = validate(category.name)
                            child_category_data.append(temp_child_category)

                        temp_parent_category['Category'] = child_category_data
                        parent_category_data.append(temp_parent_category)
                
                for parent_item in parent_category_data:
                    if not parent_item['Category']:
                        librarys = self.get_librarys_by_category(parent_item['id'])

                        library_data = []

                        for library in librarys:
                            temp_library = {}
                            temp_library['id'] = library.id
                            temp_library['name'] = validate(library.name)
                            solutions = self.get_solutions_by_library(library.id)
                            temp_library['Solution'] = solutions
                            library_data.append(temp_library)

                        parent_item['Library'] = library_data
                    else:
                        for category_item in parent_item['Category'].items():
                            librarys = self.get_librarys_by_category(parent_item['Category']['id'])

                            library_data = []
                            libraty_solution_data = []

                            for library in librarys:
                                temp_library = {}
                                temp_library['id'] = library.id
                                temp_library['name'] = validate(library.name)
                                solutions = self.get_solutions_by_library(library.id)
                                temp_library['Solution'] = solutions
                                library_data.append(temp_library)

                            category_item['Library'] = library_data
                temp_vertical['Category'] = parent_category_data
                vertical_data.append(temp_vertical)
                print "Vertical Data*****************:"
                print vertical_data
            return JsonResponse(vertical_data, safe=False)
            # return HttpResponse(vertical_data, content_type="application/json")

        return Response("Request Error", status=status.HTTP_400_BAD_REQUEST)


class UserSolutionLibraryViewById(APIView):
    def post(self, request, id, format=None):
        solution_type = SolutionType.objects.filter(name=SOLUTION_TYPE['SolutionLibrary'])
        reqeust.data['type'] = solution_type
        serializer = SolutionSerializer(data=reqeust.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersCommissionsSetView(APIView):
    def post(self, request, user_id, type):
        if type == 'exchange':
            if request.user.is_authenticated():
                user = get_user_by_pk(user_id)
                user.exchange = exchange
                user.save()
                return Response('success', status=status.HTTP_202_ACCEPTED)
            else:
                raise exceptions.NotAuthenticated('Authenticated Error')

        if type == 'pay':
            if request.user.is_authenticated():
                user = get_user_by_pk(user_id)
                user.exchange = exchange
                user.save()
            else:
                raise exceptions.NotAuthenticated('Authenticated Error')

        return Response("Request is not correct", status=status.HTTP_400_BAD_REQUEST)

# User end


# NOTEBOOK BEGINS
# disply ensemble or metaensemble or 
class NotebookViewTypesById(APIView):
    def get_ensembles_by_id(self, id):
        try:
            return Ensemble.objects.filter(notebook=id)
        except:
            raise e

    def get_metaensembles_by_id(self, id):
        try:
            return MetaEnsemble.objects.filter(notebook=id)
        except:
            raise e

    def get(self, request, notebook_id, type, format=None):
        if type == "ensemble":
            notebooks = self.get_ensembles_by_id(notebook_id)
            serializer = EnsembleSerializer(notebooks, many=True)
            return Response(serializer.data)
        
        if type == "metaensemble":
            metaensemble = self.get_metaensembles_by_id(notebook_id)
            serializer = MetaEnsembleSerializer(metaensemble, many=True)
            return Response(serializer.data)
        return Response("Request Error", status=status.HTTP_400_BAD_REQUEST)


class SearchNotebookView(APIView):
    def post(self, request, format=None):
        token = ''
        term = ''
        try:
            term = request.data.get('term')
        except:
            raise Http404

        try:
            term = request.data['term']
            type_id = request.data['type_id']
        except:
            raise Response("parameter is not correct")

        if request.user.is_authenticated():
            try:
                notebooks = Notebook.objects.all()
            except Notebook.DoesNotExist:
                return Response("no content")
            if term is not '':
                print 'not term'
                query1 = Q(description__icontains=term)
                notebooks = notebooks.filter(query1)

            if type_id != None:
                notebooks = notebooks.filter(type__id=type_id)

            serializer = NotebookAllSerializer(notebooks, many=True)
            return Response(serializer.data)

        else:
            return Response("error", status=status.HTTP_401_UNAUTHORIZED)


# DATASET BEGINS
class SearchDatasetView(APIView):
    def post(self, request, format=None):
        token = ''
        term = ''

        try:
            term = request.data['term']
            type_id = request.data['type_id']
        except:
            return Response("parameter is not correct")

        if request.user.is_authenticated():
            try:
                datasets = DataSet.objects.all()
            except DataSet.DoesNotExist:
                return Response("no model")

            if term is not '':
                print 'not term'
                query1 = Q(description__icontains=term)
                datasets = datasets.filter(query1)

            if type_id != None:
                datasets = datasets.filter(type=type_id)

            serializer = DatasetSerializer(datasets, many=True)
            return Response(serializer.data)
        else:
            raise exceptions.NotAuthenticated('Authenticated Error')


class FilterDatasetView(APIView):
    FILTER_TYPE = ['type_id', 'ensemble_id', 'metaensemble_id', 'solution_id', 'category_id', 'user_id']

    def post(self, request):
        token = ''
        value = ''

        try:
            value = request.data['value']
        except:
            return Response("no value")

        try:
            filter_name = request.data.get('filter')
            operator = request.data.get('operator')
        except:
            return Response("no filter or operator")

        if operator not in OPERATOR_LIST or filter_name not in self.FILTER_TYPE:
            return Response('operator or filter is not correct', status=status.HTTP_400_BAD_REQUEST)

        if request.user.is_authenticated():
            raw_query = 'SELECT * FROM api_dataset WHERE ' + filter_name + operator + value;
            if value == '':
                datasets = DataSet.objects.all()
            else:
                try:     
                    datasets = DataSet.objects.raw(raw_query)
                except Solution.DoesNotExist:
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


class FilterSolutionView(APIView):
    FILTER_TYPE = ['category_id', 'type_id', 'tags', 'author', 'created_at', 'updated_at']

    def post(self, request):
        token = ''
        value = ''

        try:
            value = request.data['value']
        except:
            return Response("no value")

        try:
            filter_name = request.data.get('filter')
            operator = request.data.get('operator')
        except:
            return Response("no filter or operator")

        if operator not in OPERATOR_LIST or filter_name not in self.FILTER_TYPE:
            return Response('operator or filter is not correct', status=status.HTTP_400_BAD_REQUEST)

        if request.user.is_authenticated():
            raw_query = 'SELECT * FROM api_solution WHERE ' + filter_name + operator + value;
            if value == '':
                solutions = Solution.objects.all()
            else:
                try:     
                    solutions = Solution.objects.raw(raw_query)
                except Solution.DoesNotExist:
                    raise Http404

            serializer = SolutionSerializer(solutions, many=True)
            return Response(serializer.data)
        else:
            raise exceptions.NotAuthenticated('Authenticated Error')


class DatasetViewTypesById(APIView):
    def get_ensembles_by_id(self, id):
        try:
            return Ensemble.objects.filter(dataset=id)
        except:
            raise e

    def get_metaensembles_by_id(self, id):
        try:
            return MetaEnsemble.objects.filter(dataset=id)
        except:
            raise e

    def get(self, request, dataset_id, type, format=None):
        if type == "ensemble":
            datasets = self.get_ensembles_by_id(dataset_id)
            serializer = EnsembleSerializer(datasets, many=True)
            return Response(serializer.data)
        
        if type == "metaensemble":
            metaensemble = self.get_metaensembles_by_id(dataset_id)
            serializer = MetaEnsembleSerializer(metaensemble, many=True)
            return Response(serializer.data)
        return Response("Request Error", status=status.HTTP_400_BAD_REQUEST)


# ENSEMBLE BEGIN
class EnsembleViewSet(viewsets.ModelViewSet):
    queryset = Ensemble.objects.all()
    serializer_class = EnsembleSerializer
    # permission_classes = (permissions.AllowAny,)

    def list(self, request):
        ensembles = Ensemble.objects.all()
        serializer = EnsembleSerializer(ensembles, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            serializer = EnsemblesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise exceptions.NotAuthenticated('Authenticated Error')


class SearchEnsembleView(APIView):
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

        query = Q()
        if request.user.is_authenticated():
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
            raise exceptions.NotAuthenticated('Authenticated Error')


class FilterEnsembleView(APIView):
    FILTER_TYPE = ['foreign_type', 'ensemble_id', 'metaensemble_id', 'solution_id', 'user_id']

    def get_token(self):
        return '123'

    def post(self, request):
        token = ''
        value = ''

        try:
            value = request.data['value']
        except:
            return Response("no value")

        try:
            filter_name = request.data.get('filter')
            operator = request.data.get('operator')
        except:
            return Response("no filter or operator")

        if operator not in OPERATOR_LIST or filter_name not in self.FILTER_TYPE:
            return Response('operator or filter is not correct', status=status.HTTP_400_BAD_REQUEST)

        if request.user.is_authenticated():
            raw_query = 'SELECT * FROM api_ensemble WHERE ' + filter_name + operator + value;
            if value == '':
                ensembles = Ensemble.objects.all()
            else:
                try:     
                    ensembles = Ensemble.objects.raw(raw_query)
                except Ensemble.DoesNotExist:
                    raise Http404

            serializer = EnsembleSerializer(ensembles, many=True)
            return Response(serializer.data)

        else:
            return Response("error", status=status.HTTP_401_UNAUTHORIZED)


class EnsembleViewTypesById(APIView):
    def get_datasets_by_id(self, id):
        try:
            return DataSet.objects.filter(ensemble=id)
        except:
            raise Http404

    def get_solutions_by_id(self, id):
        try:
            return Solution.objects.filter(ensemble=id)
        except:
            raise Http404

    def get_metaensembles_by_id(self, id):
        try:
            return MetaEnsemble.objects.filter(ensemble=id)
        except:
            raise Http404

    def get(self, request, ensemble_id, type, format=None):
        if type == "datasets":
            datasets = self.get_datasets_by_id(ensemble_id)
            serializer = DatasetSerializer(datasets, many=True)
            return Response(serializer.data)
        
        if type == "solutions":
            solutions = self.get_solutions_by_id(ensemble_id)
            serializer = SolutionSerializer(solutions, many=True)
            return Response(serializer.data)

        if type == "metaensembles":
            metaensembles = self.get_notebooks_by_id(ensemble_id)
            serializer = NotebookSerializer(metaensembles, many=True)
            return Response(serializer.data)
        return Response("Request Error", status=status.HTTP_400_BAD_REQUEST)


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


class FilterMetaEnsembleView(APIView):
    FILTER_TYPE = ['foreign_type', 'ensemble_id', 'metaensemble_id', 'solution_id', 'user_id']

    def get_token(self):
        return '123'

    def post(self, request):
        token = ''
        value = ''

        try:
            value = request.data['value']
        except:
            return Response("no value")

        try:
            filter_name = request.data.get('filter')
            operator = request.data.get('operator')
        except:
            return Response("no filter or operator")

        if operator not in OPERATOR_LIST or filter_name not in self.FILTER_TYPE:
            return Response('operator or filter is not correct', status=status.HTTP_400_BAD_REQUEST)

        if request.user.is_authenticated():
            raw_query = 'SELECT * FROM api_metaensemble WHERE ' + filter_name + operator + value;
            if value == '':
                meta_ensembles = MetaEnsemble.objects.all()
            else:
                try:     
                    meta_ensembles = MetaEnsemble.objects.raw(raw_query)
                except Ensemble.DoesNotExist:
                    raise Http404

            serializer = MetaEnsembleSerializer(meta_ensembles, many=True)
            return Response(serializer.data)

        else:
            return Response("error", status=status.HTTP_401_UNAUTHORIZED)


class CommissionViewSet(viewsets.ModelViewSet):
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer

    def list(self, request):
        commissions = Commission.objects.all()
        serializer = CommissionSerializer(commissions, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        token = ''

        if request.user.is_authenticated():
            serializer = CommissionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Token is wrong or expired", status=status.HTTP_401_UNAUTHORIZED)


# BRANCH
class BranchSolutionByParentId(APIView):
    def get_notebooks_by_id(self, id):
        try:
            return Notebook.objects.filter(parent=id)
        except:
            raise Http404

    def get_solutions_by_id(self, id):
        try:
            return Solution.objects.filter(parent=id)
        except:
            raise Http404

    def get_datasets_by_id(self, id):
        try:
            return DataSet.objects.filter(parent=id)
        except:
            raise Http404

    def get(self, request, parent_id, type, format=None):
        if type == "dataset":
            datasets = self.get_datasets_by_id(parent_id)
            serializer = DatasetSerializer(datasets, many=True)
            return Response(serializer.data)
        
        if type == "solution":
            solutions = self.get_solutions_by_id(parent_id)
            serializer = SolutionSerializer(solutions, many=True)
            return Response(serializer.data)

        if type == "notebook":
            notebooks = self.get_notebooks_by_id(parent_id)
            serializer = NotebookSerializer(notebooks, many=True)
            return Response(serializer.data)
        return Response("Request Error", status=status.HTTP_400_BAD_REQUEST)


# class VerticalViewById(APIView):
#     def get_objects(self, id):
#         try:
#             return Vertical.objects.filter(pk=id, type__name=SOLUTION_TYPE['SoluitionLibrary'])
#         except Exception as e:
#             raise Http404

#     def put(self, request, id):
#         serializer = VerticalSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.library_id = id
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         solution_libraries = self.get_objects(id)
#         solution_libraries.delete()
#         return Response('Success')


# class VerticalAddView(APIView):
#      def post(self, request, id):
#         serializer = VerticalSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.library_id = id
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerticalViewSet(viewsets.ModelViewSet):
    queryset = Vertical.objects.all()
    serializer_class = VerticalSerializer

    def get_token(self):
        return '123'

    def list(self, request):
        verticals = Vertical.objects.all()
        serializer = VerticalSerializer(verticals, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            serializer = VerticalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Token is wrong or expired", status=status.HTTP_401_UNAUTHORIZED)


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    def get_token(self):
        return '123'

    def list(self, request):
        libraries = Library.objects.all()
        serializer = LibrarySerializer(libraries, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            serializer = LibrarySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Token is wrong or expired", status=status.HTTP_401_UNAUTHORIZED)

# class LibraryViewById(APIView):
#     def post(self, request):
#         solution = request.data.get('solution')
#         return Response("None")


class UserHomeView(APIView):
    def get_solutions_by_id(self, library_id):
        try:
            return Solution.objects.filter(library=library_id)
        except:
            return None

    def get_vertical_id(category_id):
        try:
            return Vertical.objects.filter(category=category_id)
        except Exception as e:
            return None

    def get(self, request, user_id):
        results = []
        verticals = Vertical.objects.filter(user=user_id)

        for vertical in verticals:
            libraries = Library.objects.filter(vetical=vertical.id)


class SolutionNavigationView(APIView):
    def get_category_vertical_id(self, vertical_id):
        try:
            return Category.objects.filter(vertical__id=vertical_id)
        except:
            return None

    def get_library_id(self, vertical_id):
        try:
            return Library.objects.filter(vertical__id=vertical_id)
        except:
            return None

    def get_solution_child_by_id(self, id):
        try:
            return Solution.objects.filter(parent__pk=id)
        except Solution.DoesNotExist:
            return None

    def get_category_child_by_id(self, id):
        try:
            return Category.objects.filter(parent__pk=id)
        except Category.DoesNotExist:
            return None

    def get_solutions_by_category(self, id):
        try:
            return Solution.objects.filter(category__id=id)
        except:
            return None

    def get(self, request, vertical_id):
        # results = []
        # solution_list = []
        # item = []
        # vertical = Vertical.objects.get(id=vertical_id)
        # if vertical is not None:
        #     categories = self.get_category_vertical_id(vertical_id)
        #     for category in categories:
        #         solutions  = self.get_solutions_by_category(category.id)
        #         for solution in solutions:
        #             solution_list.append(solution.id)
        #             sub_solutions = self.get_solution_child_by_id(solution.id)
        #             sub_item = {}
        #             sub_item['vertical'] = vertical_id
        #             sub_item['category'] = category.id
        #             sub_item['solution'] = solution.id
        #             sub_item['solution_child'] = 0
        #             sub_item['category_child'] = 0

        #             for sub_solution in sub_solutions:
        #                 if sub_solution.id not in solution_list:
        #                     sub_categories = sub_solution.categories.all()
        #                     for sub_category in sub_categories:
        #                         sub_item['solution_child'] = sub_solution.id
        #                         sub_item['category_child'] = sub_category.id
        #                         item.append(sub_item)
        #             item.append(sub_item)
        # else:
        #     item = []
        # return JsonResponse(item, safe=False)

        try:
            solution_navigation = SolutionNavigation.objects.get(vertical__id=vertical_id)
            result = model_to_dict(solution_navigation)
        except:
            result = []
        
        return JsonResponse(result, safe=False)

class AnalyticsRecordView(APIView):
    def get_user_by_id(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None

    def get_user_group_by_id(self, user_group_id):
        try:
            return UserGroup.objects.get(pk=user_group_id)
        except:
            return None

    def get_vertical_by_id(self, id):
        try:
            return Vertical.objects.get(vertical__id=id)
        except:
            return None

    def get_user_by_id(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None

    def get_solution_parent_by_id(self, id):
        try:
            return Solution.objects.filter(parent__pk=id)
        except Solution.DoesNotExist:
            return None

    def get_category_parent_by_id(self, id):
        try:
            return Category.objects.filter(parent__pk=id)
        except Category.DoesNotExist:
            return None

    def get_solutions_by_category(self, id):
        try:
            return Solution.objects.filter(category__id=id)
        except:
            return None

    def get_category_by_id(self, category_id):
        try:
            return Category.objects.get(pk=category_id)
        except:
            return None

    def get_library_by_id(self, library_id):
        try:
            return Library.objects.get(pk=library_id)
        except:
            return None

    def get_solution_by_id(self, solution_id):
        try:
            return Solution.objects.get(pk=solution_id)
        except:
            return None

    def get_notebook_by_id(self, id):
        try:
            return Notebook.objects.get(pk=id)
        except:
            return None

    def get_notebook_parent_by_id(self, id):
        try:
            return Notebook.objects.get(parent=id)
        except:
            return None

    def get_ensemble_by_id(self, id):
        try:
            return Ensemble.objects.get(pk=id)
        except:
            return None

    def get_metaensemble_by_id(self, id):
        try:
            return MetaEnsemble.objects.get(pk=id)
        except:
            return None

    def get_performance_by_id(self, id):
        try:
            return Performance.objects.get(pk=id)
        except:
            return None

    def get_dataset_by_id(self, id):
        try:
            return DataSet.objects.get(pk=id)
        except:
            return None

    def get(self, request, user_id, usergroup_id, verticalID):
        try:
            pdb.set_trace()
            analytics_records = AnalyticsRecord.objects.get(user__id=user_id, usergroup__id=usergroup_id, vertical__id=verticalID)

            result = model_to_dict(analytics_records)
        except:
            result = []
        
        return JsonResponse(result, safe=False)

    def post(self, request):
        record = AnalyticsRecord()
        user_id = request.data.get('user_id')
        usergroup_id = request.data.get('usergroup_id')
        category_id = request.data.get('category_id')
        category_parent_id = request.data.get('category_parent_id')
        vertical_id = request.data.get('vertical_id')
        library_id = request.data.get('library_id')
        solution_id = request.data.get('solution_id')
        solution_parent_id = request.data.get('solution_parent_id')
        notebook_id = request.data.get('notebook_id')
        notebook_parent_id = request.data.get('notebook_parent_id')
        dataset_id = request.data.get('dataset_id')
        ensemble_id = request.data.get('ensemble_id')
        metaensemble_id = request.data.get('meta_ensemble_id')
        performance_id = request.data.get('performance_id')

        user = self.get_user_by_id(user_id)
        if not user:
            return HttpResponse("Error")
        else:
            record.user = user

            usergroup = self.get_user_group_by_id(usergroup_id)
            if usergroup:
                record.usergroup = usergroup
            else:
                record.usergroup = None

            vertical = self.get_vertical_by_id(vertical_id)
            record.vertical = vertical if vertical else None

            category = self.get_category_by_id(category_id)
            record.category = category if category else None

            category_parent = self.get_category_by_id(category_parent_id)
            record.category_parent = category_parent if category_parent else category_parent

            library = self.get_library_by_id(library_id)
            record.library = library if library else library

            solution = self.get_solution_by_id(solution_id)
            if solution:
                record.solution = solution
                solution_parent = self.get_solution_by_id(solution_parent_id)
                if solution_parent:
                    record.solution_parent = solution_parent
                else:
                    record.solution_parent = None
            else:
                record.solution = None
                record.solution_parent = None

            notebook = self.get_notebook_by_id(notebook_id)
            record.notebook = notebook if notebook else None

            notebook_parent = self.get_notebook_by_id(notebook_parent_id)
            record.notebook = notebook_parent if notebook_parent else None

            dataset = self.get_dataset_by_id(dataset_id)
            record.dataset = dataset if dataset else None

            ensemble = self.get_ensemble_by_id(ensemble_id)
            record.ensemble = ensemble if ensemble else None

            meta_ensemble = self.get_metaensemble_by_id(0)
            if meta_ensemble:
                record.meta_ensemble = meta_ensemble 

            performance = self.get_performance_by_id(performance_id)
            record.performance = performance if performance else None

            record.save()

        return HttpResponse("Success")







