from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


def upload_to(instance, filename):
    return 'photos/portfolio/{filename}'.format(filename=filename)


class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    imageurl = models.ImageField(_("Image"), upload_to=upload_to)
    feedback = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Testimonials'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name


class Abouts(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField()
    imageurl = models.ImageField(_("Image"), upload_to=upload_to)

    class Meta:
        verbose_name = 'Abouts'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.title


class Brands(models.Model):
    name = models.CharField(max_length=150)
    imageurl = models.ImageField(_("Image"), upload_to=upload_to)

    class Meta:
        verbose_name = 'Brands'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    year = models.CharField(blank=True, max_length=50)
    work = models.ManyToManyField(
        "WorkExperience", blank=True, related_name='experiences'
    )

    def __str__(self):
        return self.year


class Skills(models.Model):
    name = models.CharField(max_length=150)
    bgColor = models.CharField(blank=True, max_length=100)
    icon = models.ImageField(_("Icon"), upload_to=upload_to)

    class Meta:
        verbose_name = _("Skills")
        verbose_name_plural = _("Skills")

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    name = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    desc = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    projectLink = models.CharField(max_length=150)
    codeLink = models.CharField(max_length=150)
    imageurl = models.ImageField(_("Image"), upload_to=upload_to)
    tag = models.ManyToManyField(
        "Tag", blank=True, related_name='works'
    )

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=150)

    def __str__(self):
        return self.tag
