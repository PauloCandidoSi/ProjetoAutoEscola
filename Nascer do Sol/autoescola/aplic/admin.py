from django.contrib import admin
from .models import Aluno, Instrutor, Aula, HorarioDisponivel

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

@admin.register(Instrutor)
class InstrutorAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'instrutor', 'data_hora', 'confirmada']
    list_filter = ['confirmada', 'data_hora']
    search_fields = ['aluno__username', 'instrutor__username']

@admin.register(HorarioDisponivel)
class HorarioDisponivelAdmin(admin.ModelAdmin):
    list_display = ['instrutor', 'data_hora_inicio', 'data_hora_fim']
    search_fields = ['instrutor__username']
