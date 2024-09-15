from rest_framework import serializers

from ...models import Post, Category
from accounts.models import Profile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    # relative_url = serializers.URLField(source='get_absolute_url',read_only=True)
    category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'title', 'snippet', 'content', 'category', 'author', 'published_date']
        read_only_fields = ['author']

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
        else:
            rep.pop('content', None)
        rep['category'] = CategorySerializer(instance.category).data
        return rep

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)
