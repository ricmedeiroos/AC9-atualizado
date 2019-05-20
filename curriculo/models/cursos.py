from django.db import models
from .disciplinas import Disciplina


class Curso(models.Model):
    '''
    Classe Curso
    '''
    tipos = [
        ('CST', 'Tecnólogo'),
        ('BACH', 'Bacharelado'),
        ('ESP', 'Especialização'),
        ('MST', 'Mestrado'),
        ('PHD', 'Doutorado')
    ]
    nome = models.CharField(max_length=255, unique=True)
    sigla = models.CharField(max_length=5, unique=True)
    tipo = models.CharField(max_length=4, choices=tipos, default='CST')
    descricao = models.TextField(blank=True)
    semestres = models.IntegerField(default=4)
    periodo = models.ManyToManyField('Periodo')
    disciplinas = models.ManyToManyField(Disciplina,
                                         through='MatrizCurricular')

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def monta_matriz(self):
        '''
        Monta um dicionário com as chaves sendo o semestre do curso
        e o valor uma lista de disciplinas que pertencem a aquele
        semestre.
        '''
        matriz = {}
        for i in range(1, self.semestres + 1):
            matriz[i] = []
        for disciplina in self.matrizcurricular_set.all():
            matriz[disciplina.semestre].append(disciplina.disciplina)
        return matriz


class MatrizCurricular(models.Model):
    '''
    Classe Matriz Curricular realizada para o relacionamento
    entre Curso e Disciplina.
    '''
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    disciplina = models.ForeignKey(Disciplina,
                                   on_delete=models.SET_NULL,
                                   null=True)
    semestre = models.IntegerField()


class Periodo(models.Model):
    turno = models.CharField(max_length=20)
    entrada = models.TimeField()
    saida = models.TimeField()

    class Meta:
        ordering = ['entrada']

    def __str__(self):
        return "{} - das {} as {}".format(self.turno,
                                          self.entrada.isoformat(timespec='minutes'),
                                          self.saida.isoformat(timespec='minutes'))