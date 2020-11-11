from django.contrib import admin

from escola.models import aluno,curso,matricula


class Alunos(admin.ModelAdmin):
    list_display = ('id','nome','rg','cpf','data_nascimento')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(aluno,Alunos)

class Cursos(admin.ModelAdmin):
    list_display= ('id','codigo_curso','Descricao')
    list_display_links = ('id','codigo_curso')
    search_fields=('codigo_curso',)

admin.site.register(curso,Cursos)

class Matriculas(admin.ModelAdmin):
    list_display= ('id','aluno','curso','periodo')
    list_display_links = ('id',)
   

admin.site.register(matricula,Matriculas)