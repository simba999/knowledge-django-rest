from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from solutions.models import Solution, Category, Performance, Notebook
from api.serializers import SolutionSerializer, NotebookSerializer
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
