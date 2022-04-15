from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import (ModelSerializer, Serializer,
                                        ValidationError)
from reviews.models import Comment, Review
from titcatgen.models import Category, Genre, Title
from users.models import User


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id',)


class TitleCreateSerializer(ModelSerializer):
    category = SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        model = Title
        fields = '__all__'


class TitleSerializer(ModelSerializer):
    category = CategorySerializer()
    genre = GenreSerializer(many=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    title = SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    # нужен котекст, он не передаётся
    def validate(self, data):
        request = self.context['request']
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if (
            request.method == 'POST'
            and Review.objects.filter(
                title=title,
                author=request.user
            ).exists()
        ):
            raise ValidationError('Один отзыв, не более!')
        return data

    class Meta:
        model = Review
        fields = (
            'id', 'author', 'score', 'pub_date', 'text', 'title'
        )


class CommentSerializer(ModelSerializer):
    review = SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role')


class NotAdminSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role')
        read_only_fields = ('role',)


class GetTokenSerializer(Serializer):
    username = serializers.CharField(
        required=True)
    confirmation_code = serializers.CharField(
        required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'confirmation_code'
        )


class SignUpSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username')
