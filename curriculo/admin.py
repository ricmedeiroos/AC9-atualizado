from django.contrib import admin
from curriculo.models import Curso, Disciplina, Turma, DisciplinaOfertada
from curriculo.models.cursos import Periodo
__alunos__ = ["aluno1@aluno.faculdadeimpacta.com.br",
              "aluno2@aluno.faculdadeimpacta.com.br"]


class DisciplinaInline(admin.TabularInline):
    model = Curso.disciplinas.through


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')
    search_fields = ('nome', 'sigla')
    inlines = [DisciplinaInline, ]


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria', 'status', 'coordenador',
                    'percentual_pratico', 'percentual_teorico')
    search_fields = ('nome',)
    list_filter = ('coordenador', 'status', 'carga_horaria')


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('ano', 'semestre', 'nome')
    list_filter = ('ano', 'semestre', 'nome')


class DisciplinaOfertadaAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'turma', 'curso', 'professor')
    search_fields = ('disciplina__nome', 'curso__nome')


admin.site.register(Turma, TurmaAdmin)
admin.site.register(DisciplinaOfertada, DisciplinaOfertadaAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)