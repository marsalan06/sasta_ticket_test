from rest_framework import viewsets
from .models import Item
from django.http import HttpResponse

from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status



class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


    # def create (self,request):
    #     print("=======testing create===")
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_execption=True)
    #     self.perform_create(serializer)
    #     headers=self.get_success_headers(serializer.data)
    #     return Response(serializer.data,status=status.HTTP_201_CREATED,headers=headers)

    # def retrieve(self, request,pk=None):
    #     queryset = self.get_queryset()
    #     item = get_object_or_404(queryset,pk=pk)

    def get_queryset(self):
        queryset = Item.objects.all()
        name = self.request.query_params.get('name',None)
        if name is not None:
            queryset = queryset.filter(name = name)
        return queryset

    
    def destroy(self, request, *args, **kwargs):
        name = request.query_params.get('name', None)
        if name:
            self.queryset = self.queryset.filter(name=name)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
    
    # def list(self, request):
    #     if self.request.query_params.get('name',None):

    #     query_set = Item.objects.all()
    #     return Response(self.serializer_class(query_set, many=True).data,
    #                     status=status.HTTP_200_OK)

    

    
    # def delete(self, request, pk=None):
    #     name = self.request.query_params.get('name',None)
    #     print(name)
    #     print("======delete=====")

    #     del_obj = Item.objects.filter(name=name)
    #     del_obj.delete()
    #     queryset = Item.objects.all()
    #     return HttpResponse (queryset)
    


