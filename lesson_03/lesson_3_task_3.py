from mailing import Mailing
from address import Address

from_addr = Address('123456', 'Москва', 'Ленинградская улица', '10', '1')
to_addr = Address('654321', 'Норильск', 'улица Кирова', '20', '2')

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=500,
    track='TRACK123'
)

print(f'Отправление {mailing.track} '
      f'из {mailing.from_address.index}, {mailing.from_address.city}, '
      f'{mailing.from_address.street}, '
      f'{mailing.from_address.house}-{mailing.from_address.apartment} '
      f'в {mailing.to_address.index}, {mailing.to_address.city}, '
      f'{mailing.to_address.street}, '
      f'{mailing.to_address.house}-{mailing.to_address.apartment}. '
      f'Стоимость {mailing.cost} рублей.')
