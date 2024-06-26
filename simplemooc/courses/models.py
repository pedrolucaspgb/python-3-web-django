from django.db import models

# Create your models here.'

class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) | models.Q(description__icontains=query))


class Course(models.Model):

    name = models.CharField('Nome', max_length=101)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de Início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    
    created_at= models.DateTimeField('Criado em', auto_now_add=True)
    updated_at= models.DateTimeField('Atualizado em', auto_now=True)
      
    objects =CourseManager()
    
    """função para mostrar os nomes dos objetos(cursos) no django admin
    """
    def __str__(self):
        return self.name
    

    """classe meta que interfere no django admin para ajustar os nomes e ordenar os publicações pelo nome(name)
    """
    class Meta:
        verbose_name="Curso"
        verbose_name_plural="Cursos"
        ordering= ['name']
