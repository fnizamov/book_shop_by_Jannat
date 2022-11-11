from rest_framework import serializers

from .models import Book, Category


class BookSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('title', 'pk',)

    def to_representation(self, instance: Category):
        books = instance.books.all()
        rep = super().to_representation(instance)
        rep['books'] = BookSerilizer(instance=books, many=True).data

        return rep