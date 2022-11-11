from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Book, Category
from .serializers import BookSerilizer, CategorySerializer

class BookApiView(APIView):

    def get(self, request: Request):
        # print(request.data)
        books = Book.objects.all()
        serialiser = BookSerilizer(books, many=True)

        return Response(
            data={
                'message': 'hello',
                'data': [1,2,3],
                'books': serialiser.data
                }
                )

    def post(self, request: Request):
        # print(request.QUERY_PARAMS)
        # # print(request.data.get('title'))
        # desc = request.data['desc']
        # title = request.data['title']
        # book = Book(title=title, desc=desc)
        # book.save()
        serializer = BookSerilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response('okey')

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerilizer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryApiView(APIView):
    def get(self, request: Request, title: str = None):
        if title:
            retrieve_category = get_object_or_404(Category, title=title)
            # try:
            #     retrieve_category = Category.objects.get(title=title)
            # except Category.DoesNotExist as e:
            #     return Response(str(e))
            # else:
            serializer = CategorySerializer(instance=retrieve_category)
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(instance=categories, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request: Request):
        data = request.POST
        serializer = CategorySerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        full_data = {
            "data": serializer.data,
            "message": "hello"
        }
        return Response(data=full_data)