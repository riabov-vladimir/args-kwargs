from application.class_contact import Contact
from application.phone_book import PhoneBook

if __name__ == '__main__':
	my_phonebook = PhoneBook('Моя телефонная книга')
	print(my_phonebook)  # отображение названия телефонной книги
	my_phonebook.add_contact(Contact('Филлип', 'Киркоров', 123456789, True, email = 'kirkorov@mail.zz'))
	my_phonebook.add_contact(Contact('Алла', 'Пугачёва', 434443544, False, email='allo4ka@mail.zz'))
	my_phonebook.add_contact(Contact('Влад', 'Сташевский', 8876364438, True, email='vladstach@mail.zz'))
	my_phonebook.add_contact(Contact('Валерий', 'Меладзе', 1438456789, False, email='melazze@mail.zz'))
	my_phonebook.show_contacts()  # вывод всех контактов
	my_phonebook.show_favourites()  # вывод всех избранных контактов
	my_phonebook.remove_contact(8876364438)  # удаление контакта по номеру телефона
	my_phonebook.show_contact_name_surname('Валерий', 'Меладзе')  # отображение контакта по имени и фамилии
