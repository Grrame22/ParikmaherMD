from django.db import models


class Area(models.Model):
    name = models.CharField("Название райнона", max_length=100)

    def __str__(self):
        return self.name


class Hairdressing(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)
    phone = models.CharField("Телефон", max_length=20, unique=True)
    website = models.URLField("Сайт", max_length=300, blank=True)
    reviews = models.URLField("Отзывы", max_length=300, blank=True)
    main_image = models.ImageField("Фотографии на главную", blank=True)
    adding_image_1 = models.ImageField("Добавочная фотография", blank=True)
    adding_image_2 = models.ImageField("Добавочная фотография", blank=True)
    description = models.TextField("Описание")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="Район")
    address_location = models.CharField("Адресс", max_length=100, unique=True)
    schedule_for_calculating = models.TextField("Расписание(для расчёта)")
    monday = models.TextField("Понедельник")
    tuesday = models.TextField("Вторник")
    wednesday = models.TextField("Среда")
    thursday = models.TextField("Четверг")
    friday = models.TextField("Пятница")
    saturday = models.TextField("Суббота")
    sunday = models.TextField("Воскресенье")
    specializations = models.TextField("Специализации")
    price_list = models.TextField("Тарифы")
    sales = models.TextField("Скидки", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hairdressing"
