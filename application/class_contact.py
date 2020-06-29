"""класс Contact имеет следующие поля:
Имя, фамилия, телефонный номер - обязательные поля;
Избранный контакт - необязательное поле. По умолчанию False;
Дополнительная информация(email, список дополнительных номеров, ссылки на соцсети) - необходимо использовать *args, **kwargs.
Переопределить "магический" метод str для красивого вывода контакта. Вывод контакта должен быть следующим

    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(jhon)
Вывод

Имя: Jhon
Фамилия: Smith
Телефон: +71234567809
В избранных: нет
Дополнительная информация:
	 telegram : @jhony
	 email : jhony@smith.com
"""

class Contact:

	favourites = False

	def __init__(self, name, surname, phone_number, **kwargs):
		self.name = name
		self.surname = surname
		self.phone_umber = phone_number
		self.additional_info = kwargs

	def favourites_toggle(self, toggle: int):
		if toggle == 0:
			self.favourites = False
		elif toggle == 1:
			self.favourites = True
		return print(f'В избранных: {self.favourites}')

	def __str__(self):
		return f'Имя: {self.name}\nФамилия: {self.surname}\nВ избранных: {self.favourites}\nТелефон: ' \
			   f'{self.phone_umber}\nДополнительная информация:\n{print(self.additional_info_extract())}'

	def additional_info_extract(self):
		for k, v in self.additional_info.items():
			yield f'{str(k)}: {str(v)}'


if __name__ == '__main__':
	alec = Contact('alec', 'malik', 43243255, telegram='@alik', additional_number='1164684')

	# print(alec.name, alec.surname, alec.phone_umber, alec.additional_info)
	alec.favourites_toggle(1)
	print(' ')
	print(alec)
