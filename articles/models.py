from django.db import models

class Kullanici(models.Model):
    GENDER_CHOICES = (
        ("e", "Erkak"),
        ("k", "Kadin"),
        ("b", "Belirtmelik Istemiyorum"),
    )
    AGE_CHOICES = (
        (1, 12),
        (1, 13),
        (1, 14),
    )
    first_name = models.CharField(max_length=25, verbose_name="Isim")
    last_name = models.CharField(max_length=25, verbose_name="Soy Isim")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="b")
    yas = models.IntegerField(choices=AGE_CHOICES, default=1)

    class Meta:
        db_table = "Makaleler"
        verbose_name = "Makale"
        verbose_name_plural = "Makaleler"
        ordering = ("-created_date",)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="Boshi")
    description = models.TextField(max_length=5010, verbose_name="Aciklama")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Olusturulma Tarixi")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="Bozenlarma Tarixi")
    category = models.ManyToManyField(to="articles.Category")
    author = models.ForeignKey(Kullanici, on_delete=models.CASCADE, verbose_name="Yazar", null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Category ismi")
    created_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name