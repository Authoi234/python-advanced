import csv

field_names = ["Name", "Author", "Publisher", "Price", "Category"]

book1 = {"Name":"Kimiya E Saadat (Volume 1)", "Author":"Abu Hamid Muhammad ibn Muhammad al-Ghazzali","Publisher": "Shaikh Ghulam Ali and Sons Educational Publishers, Lahore", "Price": "12,142.58", "Category":  "Islamic Book"}
book2 = {"Name":"মারহাবা, জাভাস্ক্রিপ্টে মারো থাবা", "Author":"Jhankar Mahbub", "Publisher":"আদর্শ", "Price": "671.00",  "Category": "Programming"}
book3 = {"Name":"The Road to Life","Author": "Anton Makarenko","Publisher": "Progress Publishers, Moscow", "Price": "3,138.67",  "Category": "Novel"}

book_list = [book1, book2, book3]

with open("books.csv", "w", encoding="utf-8") as csvf:
    csv_writer = csv.DictWriter(csvf , fieldnames=field_names )
    csv_writer.writeheader()
    csv_writer.writerows(book_list)