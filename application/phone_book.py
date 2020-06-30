from application.class_contact import Contact


class PhoneBook:
	def __init__(self, phone_book_name, *args):
		self.name = phone_book_name
		self.contacts = list(args)

	def __str__(self):
		return self.name

	def show_contacts(self):
		print(f'Содержимое телефонной книги {self.name}:\n')
		for contact in self.contacts:
			print(contact)

	def add_contact(self, contact):
		self.contacts.append(contact)
		print(f'Контакт "{contact.name} {contact.surname}" добавлен в телефонную книгу')

	def remove_contact(self, phone_number):
		for contact in self.contacts:
			if contact.phone_umber == phone_number:
				self.contacts.remove(contact)
				print(f'Контакт "{contact.name} {contact.surname}" удалён из телефонной книги')

	def show_favourites(self):
		print('Избранные контакты:\n')
		for contact in self.contacts:
			if contact.favourites:
				print(contact)


	def show_contact_name_surname(self, name, surname):
		for contact in self.contacts:
			if (name == contact.name) and (surname == contact.surname):
				print(contact)
