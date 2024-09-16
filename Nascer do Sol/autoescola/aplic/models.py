from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Aluno(User):
    # Herda de User, você pode adicionar campos adicionais se necessário
    pass

class Instrutor(User):
    # Herda de User, você pode adicionar campos adicionais se necessário
    pass

class Aula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    confirmada = models.BooleanField(default=False)

    def __str__(self):
        return f'Aula de {self.aluno.username} com {self.instrutor.username} em {self.data_hora}'

    class Meta:
        ordering = ['data_hora']

class HorarioDisponivel(models.Model):
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    data_hora_inicio = models.DateTimeField()
    data_hora_fim = models.DateTimeField()

    def __str__(self):
        return f'Horário disponível de {self.data_hora_inicio} a {self.data_hora_fim} para {self.instrutor.username}'

    class Meta:
        ordering = ['data_hora_inicio']

    def esta_disponivel(self, data_hora):
        """Verifica se a data_hora está dentro do intervalo disponível."""
        return self.data_hora_inicio <= data_hora <= self.data_hora_fim
