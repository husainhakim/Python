
books=['sparshva','faheem don','gauri','chaitu']
authors=['sparsh sharma','muhammed faheem','gaurang jadhav','chaitanya dalvi']
print("_______________Hello and welcome to sparshva library!_______________")
while True:
    a=int (input("Enter your choice!(1-4)\n1)Add books\t\t2)Check existing books\n3)Search for books\t\t4)Exit\n5)Remove a book\n"))
    if a==1:
        name=input('Enter the name of the book:-')
        if name in books:
            print("Book already exists in the library!")
            break
        else:
           author=input('Enter the name of the author:-')
           print(name," book by ",author,"added sucessfully")
           
           books.append(name)
           authors.append(author)
        ask=input("Do you want to work further on or close?")
        if ask=='close':
            break
    elif a==4:
        print("Thanks for visiting us! have a great day ahead")
        break 
    elif a==2:
        print(books)
        print(authors)
    elif a==3:
        titleofbook=input("Enter the name of the book to search for:-")
        if titleofbook in books:
            print(titleofbook,' book found in library')
        else:
            print('there is no book in the library called',titleofbook)
    elif a==5:
        removebook=input("Enter the name of the book you want to remove from the library:-")
        if removebook in books:
            del(books[removebook])
            print(removebook,'book removed from the library sucesfully!')
        else:
            print('there is no book called',removebook,'in library')
            
            
# library_books = []

# while True:
#     print('\nLibrary Management System')
#     print('1. Add a book')
#     print('2. Display all books')
#     print('3. Search for a book by title')
#     print('4. Exit')

#     choice = input('Enter your choice (1-4): ')

#     if choice == '1':
#         title = input('Enter the title of the book: ')
#         author = input('Enter the author of the book: ')
#         book = {'title': title, 'author': author}
#         library_books.append(book)
#         print(f'Book "{title}" by {author} added successfully.')

#     elif choice == '2':
#         if not library_books:
#             print('No books in the library.')
#         else:
#             print('List of books in the library:')
#             for index, book in enumerate(library_books, start=1):
#                 print(f'{index}. {book["title"]} by {book["author"]}')

#     elif choice == '3':
#         title = input('Enter the title of the book to search: ')
#         matching_books = [book for book in library_books if title.lower() in book['title'].lower()]
#         if not matching_books:
#             print(f'No books found with the title "{title}".')
#         else:
#             print(f'Books found with the title "{title}":')
#             for index, book in enumerate(matching_books, start=1):
#                 print(f'{index}. {book["title"]} by {book["author"]}')

#     elif choice == '4':
#         print('Exiting the library management system. Goodbye!')
#         break

#     else:
#         print('Invalid choice. Please enter a number between 1 and 4.')