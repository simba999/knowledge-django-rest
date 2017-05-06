from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from solutions.models import Solution
from categories.serializers import SolutionSerializer


# Create your views here.
class CategoriesViewSet(viewsets.ModelViewSet):
    """
    List Solution object by category id or return fail
    """
    def get_object(self, pk):
        try:
            return Solution.objects.get(pk=pk)
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print pk
        print "SDFsdf"
        solution = self.get_object(pk)
        serializer = SolutionSerializer(solution)
        return Response(serializer.data)


class CategoryDetailView(APIView):
    def get_object(self, pk):
        try:
            return Solution.objects.get(pk=pk)
        except Solution.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print pk
        print "SDFsdf"
        solution = self.get_object(pk)
        serializer = SolutionSerializer(solution)
        return Response(serializer.data)
        # return Response({})
