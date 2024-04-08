from rest_framework import serializers
from .models import Disciplines, Scientist, State, Student, Tag

class DisciplinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplines
        fields = ['id', 'name', 'description']

class ScientistSerializer(serializers.ModelSerializer):
    discipline = serializers.SlugRelatedField(slug_field='name', queryset=Disciplines.objects.all())

    class Meta:
        model = Scientist
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'biography', 'birthday', 'position', 'discipline', 'academic_degree', 'photo']

class StateSerializer(serializers.ModelSerializer):
    scientist_tag = ScientistSerializer(read_only=True)
    scientist_tag_id = serializers.PrimaryKeyRelatedField(queryset=Scientist.objects.all(), source='scientist_tag', write_only=True)
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = State
        fields = ['id', 'title', 'text', 'scientist_tag', 'scientist_tag_id', 'photo', 'tags']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'group', 'course', 'faculty', 'birthday', 'phone']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'state']
