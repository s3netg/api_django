from django.db import models

class aluno (models.Model):
   
    nome  = models.CharField(max_length = 30)
    rg  = models.CharField(max_length = 9)
    cpf  = models.CharField(max_length = 11)
    data_nascimento  = models.DateField()
    
    def __str__(self):
        return self.nome


class curso (models.Model):
    NIVEL = (
        ('B','Basico'),
        ('I','Intermediario'),
        ('A','Avançado')
    )
    codigo_curso = models.CharField(max_length =10)
    Descricao = models.CharField( max_length=100)
    nivel  = models.CharField(max_length = 1,choices=NIVEL,blank=False,null = False,default='B')
       

    def __str__(self):
        return self.Descricao
    
class matricula(models.Model):
    PERIODO = (
        ('M','Matutuino'),
        ('V','Vespertino'),
        ('N','Noturno')
    )
    aluno = models.ForeignKey(aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    periodo  = models.CharField(max_length = 1,choices=PERIODO,blank=False,null = False,default='M')
    