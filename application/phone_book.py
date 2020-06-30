from application.class_contact import Contact

"""_2. класс PhoneBook:

Название телефонной книги - обязательное поле;
Телефонная книга должна работать с классами Contact.
Методы:


Удаление контакта по номеру телефона;
Поиск всех избранных номеров;
Поиск контакта по имени и фамилии.
"""

class PhoneBook:
	def __init__(self, phone_book_name, *args):
		self.name = phone_book_name
		self.contacts = list(args)

	def __str__(self):
		return self.name

	def show_contacts(self):
		for contact in self.contacts:
			print(contact)

	def add_contact(self, contact):
		self.contacts.append(contact)

	def remove_contact(self, phone_number):
		for contact in self.contacts:
			if contact.phone_umber == phone_number:
				self.contacts.remove(contact)

	def show_favourites(self):
		for contact in self.contacts:
			if contact.favourites:
				print(contact)

if __name__ == '__main__':

	my_phonebook = PhoneBook('my_book', Contact('a', 'b', 123, telegram=325325), Contact('c', 'd', 456, True))
	# my_phonebook.show_contacts()
	print(my_phonebook)
	print(my_phonebook.contacts)
	my_phonebook.add_contact(Contact('e', 'f', 789))
	# my_phonebook.show_contacts()
	print(my_phonebook.contacts)
	# my_phonebook.show_contacts()
	# my_phonebook.remove_contact(789)
	# print(my_phonebook.contacts)
	my_phonebook.show_favourites()