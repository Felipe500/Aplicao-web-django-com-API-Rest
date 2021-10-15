
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from django.contrib.auth.models import User, Group
from livros.models import Obra, Editora, Autor



class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = ['nome']

class EditoraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Editora
        fields =  ['nome']



class ObraSerializer(serializers.ModelSerializer):
    autores = AutorSerializer(many=True)
    editora = EditoraSerializer()
    class Meta:
        model = Obra
        fields = ['id','titulo','img','descricao','autores','editora']


    def cria_editoras(self, x_autores, ponto):
        for autor in x_autores:
            at = Autor.objects.create(**autor)
            ponto.autores.add(at)

    def create(self, validated_data):
        x_autores = validated_data['autores']
        del validated_data['autores']
        print(validated_data['editora'])
        editor = validated_data['editora']
        del validated_data['editora']
        
        ponto = Obra.objects.create(**validated_data)
        self.cria_editoras(x_autores, ponto)
        
        edit = Editora.objects.create(**editor)
        ponto.editora = edit

        return ponto




