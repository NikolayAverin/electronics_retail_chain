from django.db import models

HIERARCHY_TYPE = [
    ("factory", "завод"),
    ("retail network", "розничная сеть"),
    ("individual entrepreneur", "индивидуальный предприниматель"),
]


class Contact(models.Model):
    """Модель контактной информации."""

    email = models.EmailField(max_length=100, unique=True, verbose_name="Почта")
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=50, verbose_name="Улица")
    house_number = models.PositiveSmallIntegerField(verbose_name="Номер дома")

    def __str__(self):
        return f"{self.email} из {self.country}, {self.city}, {self.street}, {self.house_number}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    """Модель продукта."""

    title = models.CharField(max_length=100, verbose_name="Наименование")
    product_model = models.CharField(max_length=250, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода продукта на рынок")

    def __str__(self):
        return f"{self.title}, {self.product_model} вышел на рынок {self.release_date}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class HierarchyElement(models.Model):
    """Модель элемента иерархии."""

    name = models.CharField(max_length=150, verbose_name="Название звена иерархии")
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, verbose_name="Контакты"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукты"
    )
    supplier = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Поставщик",
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Задолженность перед поставщиком",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    hierarchy_type = models.CharField(
        max_length=50, choices=HIERARCHY_TYPE, verbose_name="Тип звена иерархии"
    )
    hierarchy_level = models.IntegerField(
        default=0, verbose_name="Уровень звена иерархии"
    )
    country = models.CharField(
        max_length=50, default=None, blank=True, null=True, verbose_name="Страна"
    )
    city = models.CharField(
        max_length=50, default=None, blank=True, null=True, verbose_name="Город"
    )

    def __str__(self):
        return f"{self.name} - {self.contact}, {self.product}"

    class Meta:
        verbose_name = "Элемент иерархии"
        verbose_name_plural = "Элементы иерархии"
