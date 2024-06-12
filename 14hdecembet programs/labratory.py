
class Libraryitem:
    def puchouser(self):
         print( "----------Welcome to sparshva library!------------")
         self.checkintime = float(input("Enter the checkintime (24 hours, e.g., 3:30pm=15.5): "))
         self.ask = int(input("Enter what are you interested in and what do you want? \n1)Books\n2)DVD\n3)Journal: "))

         if self.ask == 1:
            self.booksjao = Book()
            self.booksjao.books()


class Book(Libraryitem):
    def books(self):
        print("Your interest is in books!")
        self.askbooksinput = int(input("Choose a book: 1) Where the Crawdads Sing, 2) The Silent Patient, 3) Normal People, 4) Pachinko, 5) King Areeb: "))

        if self.askbooksinput == 1:
            print('Book name: Where the Crawdads Sing\nAuthor: Delia Owens\nRelease year: 2018')
        elif self.askbooksinput == 2:
            print('Book name: The Silent Patient\nAuthor: Alex Michaelides\nRelease year: 2019')
        elif self.askbooksinput == 3:
            print('Book name: Normal People\nAuthor: Sally Rooney\nRelease year: 2018')
        elif self.askbooksinput == 4:
            print('Book name: Pachinko\nAuthor: Min Jin Lee\nRelease year: 2017')
        elif self.askbooksinput == 5:
            print('Book name: King Areeb\nAuthor: King Areeb\nRelease year: 2023')
        else:
            print("Book unavailable")

        self.checkouttime = float(input("Enter the checkout time (24 hours, e.g., 3:30pm=15.5): "))
        self.askforrenting = input("Would you like to rent the book? (yes/no): ")
        if self.askforrenting.lower() == "yes":
            self.askfortime = int(input("How many hours would you like to rent the book? "))
            if self.askfortime>100:
                print("We dont rent books for more than 100 hours")
                return
            elif self.askfortime<100:
                print("\n\nHere is your book for rental please return the book on time or you might get a fine!\nWe are generating a bill for you please stray on handby...\n\n")
husayn = Libraryitem()
husayn.puchouser()
