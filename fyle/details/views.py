from django.shortcuts import render
from .models import Branches, Banks
from .serializers import BranchReadSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ApiList(APIView):
    permission_classes = (IsAuthenticated,)
    """
    List all snippets, or create a new snippet.
    """
    paginate_by = 100
    def get(self, request, format=None):
        pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        paginator = pagination_class()
        queryset = Branches.objects.all()
        bank_name = request.query_params.get('bank_name', None)
        city = request.query_params.get('city', None)
        if bank_name is not None:
            queryset = queryset.filter(bank__name=bank_name)
        if city is not None:
             queryset = queryset.filter(city=city)

        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = BranchReadSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = BranchReadSerializer(queryset, many=True)
        return Response(serializer.data)
        # if limit is not None:
        #     serializer = ApiSerializer(limit, many=True)
        #     return paginator.get_paginated_response(serializer.data)

        # # limit = paginator.paginate_queryset(queryset, request)
        # # serializer = ApiSerializer(limit, many=True)
        # # return paginator.get_paginated_response(serializer.data)
        # api = Api.objects.all()
        # serializer = ApiSerializer(api, many=True)
        # return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = ApiSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiDetail(APIView):
    permission_classes = (IsAuthenticated,)
    """
    Retrieve, update or delete a api instance.
    """
    def get_object(self, ifsc):
        try:
            return Branches.objects.get(ifsc=ifsc)
        except Branches.DoesNotExist:
            raise Http404

    def get(self, request, ifsc, format=None):
        branch = self.get_object(ifsc)
        serializer = BranchReadSerializer(branch)
        return Response(serializer.data)

    def put(self, request, ifsc, format=None):
        branch = self.get_object(ifsc)
        print(branch)
        serializer = BranchReadSerializer(branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ifsc, format=None):
        branch = self.get_object(ifsc)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)