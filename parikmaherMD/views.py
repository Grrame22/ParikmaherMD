from django.shortcuts import render
from django.views.generic.base import View
from django.core.paginator import Paginator
from .models import Hairdressing
from datetime import datetime
import calendar


class HomePageView(View):
    """Home page with all hairdressing salons"""

    def get(self, request):
        week_days = {"Monday": "Пн", "Tuesday": "Вт",
                     "Wednesday": "Ср", "Thursday": "Чт",
                     "Friday": "Пт", "Saturday": "Сб",
                     "Sunday": "Вс"}
        local_date = calendar.day_name[datetime.today().weekday()]
        local_time = datetime.today().time()

        for day in week_days.items():
            if local_date == day[0]:
                local_date = day[1]
            continue

        hairdressing = Hairdressing.objects.all()
        hairdressing = sorted(hairdressing, key=lambda salon: salon.name)

        paginator = Paginator(hairdressing, 30)
        page = request.GET.get("page")
        hairdressing = paginator.get_page(page)

        context = {"hairdressing": hairdressing, "local_date": local_date,
                   "local_time": local_time}

        return render(request, "parikmaherMD/home_page.html", context)


class HairdressingAreaView(View):
    """Home page with particular hairdressing salons, sorted by the area"""

    def get(self, request, id):
        hairdressing = Hairdressing.objects.filter(area=id)

        paginator = Paginator(hairdressing, 30)
        page = request.GET.get("page")
        hairdressing = paginator.get_page(page)

        week_days = {"Monday": "Пн", "Tuesday": "Вт",
                     "Wednesday": "Ср", "Thursday": "Чт",
                     "Friday": "Пт", "Saturday": "Сб",
                     "Sunday": "Вс"}
        local_date = calendar.day_name[datetime.today().weekday()]
        local_time = datetime.today().time()

        for day in week_days.items():
            if local_date == day[0]:
                local_date = day[1]
            continue

        area = ""
        areas_dict = {1: "Центр", 2: "Боюканы", 3: "Рышкановка",
                      4: "Чеканы", 5: "Ботаника"}

        area += areas_dict[id]

        context = {"hairdressing": hairdressing, "area": area, "local_date": local_date,
                   "local_time": local_time}

        return render(request, "parikmaherMD/hairdressing_area.html", context)


class ParticularHairdressingView(View):
    """Page with particular hairdressing salon and its information"""

    def get(self, request, id):
        week_days = {"Monday": "Пн", "Tuesday": "Вт",
                     "Wednesday": "Ср", "Thursday": "Чт",
                     "Friday": "Пт", "Saturday": "Сб",
                     "Sunday": "Вс"}
        local_date = calendar.day_name[datetime.today().weekday()]
        local_time = datetime.today().time()

        for day in week_days.items():
            if local_date == day[0]:
                local_date = day[1]
            continue

        hairdressing = Hairdressing.objects.get(id=id)

        context = {"hairdressing": hairdressing, "local_date": local_date,
                   "local_time": local_time}

        return render(request, "parikmaherMD/particualr_hairdressing.html", context)
