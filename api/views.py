from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from solutions.models import Solution, Category, Performance, Notebook, DataSet, Price
from api.serializers import SolutionSerializer, NotebookSerializer, CategorySerializer, DatasetSerializer, PriceSerializer
from rest_framework.renderers import JSONRenderer


# Create your views here.
# Solution APIs
class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    
    def list(self, request):
        solutions = Solution.objects.all()
        serializer = SolutionSerializer(solutions, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = SolutionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SolutionDetailView(APIView):
    def get_object(self, pk):
        try:
            return Solution.objects.get(pk=pk)
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, pid, format=None):
        print pid
        # print solution
        solution = self.get_object(pid)
        serializer = SolutionSerializer(solution)
        data = JSONRenderer().render(serializer.data)
        print serializer
        print "DATA: ", data
        return Response(serializer.data)


# Notebook APIs
class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer
    
    def list(self, request):
        notebooks = Notebook.objects.all()
        print notebooks.values_list()
        serializer = NotebookSerializer(notebooks, many=True)
        data = JSONRenderer().render(serializer.data)
        return Response(serializer.data)


class SolutionLibraryView(APIView):
    def get_object(self, pk):
        try:
            return Solution.objects.filter(category__id=pk)
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, category_id, format=None):
        print category_id
        # print solution
        solution = self.get_object(category_id)
        print solution
        serializer = SolutionSerializer(solution, many=True)
        data = JSONRenderer().render(serializer.data)
        print serializer
        print "DATA: ", data
        return Response(serializer.data)


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
