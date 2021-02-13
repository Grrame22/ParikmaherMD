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
    schedule_for_calculating = models.TextField("Расписание(для расчёта)", blank=True)
    monday = models.CharField("Понедельник", max_length=200, blank=True)
    tuesday = models.CharField("Вторник", max_length=200, blank=True)
    wednesday = models.CharField("Среда", max_length=200, blank=True)
    thursday = models.CharField("Четверг", max_length=200, blank=True)
    friday = models.CharField("Пятница", max_length=200, blank=True)
    saturday = models.CharField("Суббота", max_length=200, blank=True)
    sunday = models.CharField("Воскресенье", max_length=200, blank=True)
    work_graphic = models.CharField("График работы", max_length=500, blank=True)
    manicure = models.TextField("Маникюр", blank=True)
    type_of_salon = models.TextField("Тип салона", blank=True)
    services_for_hair = models.TextField("Услуги для волос", blank=True)
    services_for_face_and_body = models.TextField("Услуги для лица и тела", blank=True)
    services_for_fingernails = models.TextField("Услуги для ногтей", blank=True)
    tattooash_and_microblading = models.TextField("Татуаж и микроблэдинг", blank=True)
    eye_contour = models.TextField("Контур глаз", blank=True)
    other = models.TextField("Другое", blank=True)
    sales = models.TextField("Скидки", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hairdressing"
