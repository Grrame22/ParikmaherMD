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
    monday = models.CharField("Понедельник", max_length=200)
    tuesday = models.CharField("Вторник", max_length=200)
    wednesday = models.CharField("Среда", max_length=200)
    thursday = models.CharField("Четверг", max_length=200)
    friday = models.CharField("Пятница", max_length=200)
    saturday = models.CharField("Суббота", max_length=200)
    sunday = models.CharField("Воскресенье", max_length=200)
    manicure = models.TextField("Маникюр", blank=True)
    type_of_salon = models.TextField("Тип салона", blank=True)
    services_for_hair = models.TextField("Услуги для волос", blank=True)
    services_for_face_and_body = models.TextField("Услуги для лица и тела", blank=True)
    services_for_fingernails = models.TextField("Услуги для ногтей", blank=True)
    price_list = models.TextField("Тарифы")
    sales = models.TextField("Скидки", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hairdressing"
