from application.class_contact import Contact

"""_2. класс PhoneBook:

Название телефонной книги - обязательное поле;
Телефонная книга должна работать с классами Contact.
Методы:

Вывод контактов из телефонной книги;
Добавление нового контакта;
Удаление контакта по номеру телефона;
Поиск всех избранных номеров;
Поиск контакта по имени и фамилии.
"""

class PhoneBook:
	def __init__(self, *args):
		self.contacts = list(args)

	def show_contacts(self):
		for contact in self.contacts:
			print(contact)

	def add_contact(self, contact: Contact):
		self.contacts.append(contact)


if __name__ == '__main__':
	c_list = (Contact('a', 'b', 123), Contact('c', 'd', 456))
	my_phonebook = PhoneBook(c_list)
	my_phonebook.show_contacts()
	print('')
	my_phonebook.add_contact(Contact('e', 'f', 789))
	my_phonebook.show_contacts()