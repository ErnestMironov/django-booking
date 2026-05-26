from django.apps import AppConfig


class WorkshopsConfig(AppConfig):
    name = "apps.workshops"

    def ready(self):
        from django.db.models.signals import post_migrate
        post_migrate.connect(_seed_workshops, sender=self)
        post_migrate.connect(_seed_admin, sender=self)


def _seed_admin(sender, **kwargs):
    from apps.users.models import User

    if User.objects.filter(email="admin@test.com").exists():
        return

    User.objects.create_user(
        username="admin@test.com",
        email="admin@test.com",
        password="secret123",
        role="admin",
    )


def _seed_workshops(sender, **kwargs):
    from django.utils.timezone import datetime, timezone
    from apps.workshops.models import Workshop

    if Workshop.objects.exists():
        return

    Workshop.objects.bulk_create([
        Workshop(
            title="Гончарное дело для начинающих",
            description="Научитесь лепить из глины на гончарном круге. Материалы и инструменты предоставляются. Каждый участник унесёт домой готовое изделие.",
            date=datetime(2026, 6, 20, 10, 0, tzinfo=timezone.utc),
            capacity=12,
            image_url="https://images.unsplash.com/photo-1764507768797-5b7de6eedcb7?w=900&h=300&fit=crop&auto=format",
        ),
        Workshop(
            title="Акварельная живопись",
            description="Мастер-класс по акварели для тех, кто хочет научиться писать пейзажи и натюрморты. Все расходники включены в стоимость.",
            date=datetime(2026, 6, 25, 14, 0, tzinfo=timezone.utc),
            capacity=8,
            image_url="https://images.unsplash.com/photo-1578961140619-896df05b1fd2?w=900&h=300&fit=crop&auto=format",
        ),
        Workshop(
            title="Кожаные изделия своими руками",
            description="Создадим кошелёк или брелок из натуральной кожи. Вы освоите базовые техники шитья и тиснения по коже.",
            date=datetime(2026, 7, 5, 11, 0, tzinfo=timezone.utc),
            capacity=6,
            image_url="https://images.unsplash.com/photo-1573227897444-860137a0fe74?w=900&h=300&fit=crop&auto=format",
        ),
        Workshop(
            title="Флористика и составление букетов",
            description="Научитесь составлять букеты и флористические композиции. Свежие цветы и материалы предоставляются.",
            date=datetime(2026, 7, 12, 15, 0, tzinfo=timezone.utc),
            capacity=15,
            image_url="https://images.unsplash.com/photo-1567696153798-9111f9cd3d0d?w=900&h=300&fit=crop&auto=format",
        ),
        Workshop(
            title="Столярное дело: разделочная доска",
            description="Сделаете разделочную доску из массива дерева с нуля. Весь инструмент и дерево предоставляется.",
            date=datetime(2026, 7, 20, 10, 0, tzinfo=timezone.utc),
            capacity=5,
            image_url="https://images.unsplash.com/photo-1631396328075-9c65a7406f09?w=900&h=300&fit=crop&auto=format",
        ),
    ])
