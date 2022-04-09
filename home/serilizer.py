from pyexpat import model
from rest_framework import serializers
from django.template.defaultfilters import slugify
import re
from .models import Todo

class TodoSerilizer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    
    class Meta:
        model = Todo
        fields = ['id','todo_title','todo_description','is_done','slug']

    def get_slug(self, obj):
        return slugify(obj.todo_title)    

    def validate(self, validated_data):
        if validated_data.get('todo_title'):
            todo_title = validated_data['todo_title']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            
            if len(todo_title) < 3:
                raise serializers.ValidationError('Todo tiele must be more than 3 chars..')

            if not regex.search(todo_title) == None:
                raise serializers.ValidationError('Todo tiele cannot contains special character..')

        return validated_data