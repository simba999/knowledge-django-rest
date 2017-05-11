from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import exceptions
from rest_framework import permissions
from rest_framework.decorators import api_view
from solutions.models import Solution, Category, Performance, Notebook, DataSet, Price
from api.serializers import SolutionSerializer, NotebookSerializer
from api.serializers import CategorySerializer, DatasetSerializer, PriceSerializer, PerformanceSerializer, AnomalySerializer
from rest_framework.renderers import JSONRenderer
import json


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


#GET /solution/customsolution/parent/{id}
class CustomSolutionViewByParent(APIView):
    def get_object(self, id):
        try:
            return Solution.objects.filter(parent=id, type__name="CustomSolution")
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, parent_id, format=None):
        print "Parent:" + parent_id
        solution = self.get_object(parent_id)
        print solution
        serializer = SolutionSerializer(solution, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


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

@api_view(['POST'])
def CustomSolutionAddView(request):
    print "TYPE: " + request.data
    type = SolutionType.objects.filter(name='CustomSolution')
    print "TYPE: " + request.data
    request.data['type'] = type
    print "New Type: " + request.data
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

