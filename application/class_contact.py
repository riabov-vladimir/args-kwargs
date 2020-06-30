class Contact:

	def __init__(self, name, surname, phone_number, favourites: bool = False, **kwargs):
		self.name = name
		self.surname = surname
		self.phone_umber = phone_number
		self.favourites = favourites
		self.additional_info = kwargs

	def favourites_toggle(self, toggle: int):
		if toggle == 0:
			self.favourites = False
		elif toggle == 1:
			self.favourites = True

	def	favourites_view(self) -> str:
		if self.favourites:
			return 'Да'
		else:
			return 'Нет'

	def __str__(self):
		string = (
			f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон: {self.phone_umber}\n'
			f'В избранных: {self.favourites_view()}\n'
		)

		if self.additional_info:
			string += f'Дополнительная информация:\n'
			for k, v in self.additional_info.items():
				string += f'         {str(k)}: {str(v)}\n'

		return string
