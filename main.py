import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

cards = Passcard.objects.all()
some_card = cards[0]

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    print('Активных пропусков:', Passcard.objects.filter(is_active=True).count())  # noqa: T001

