#User class
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Your email address has been changed to {address}".format(address = self.email))

    def __repr__(self):
        return  "User {name}, email: {email}, books read : {num_books}".format(name = self.name, email = self.email, num_books = len(self.books))

    def __eq__(self, other_user):
        return ((self.name == other_user.name) and (self.email == other_user.email))

    def read_book(self, book, rating = None):
        self.books[book] = rating
        return self.books

    def get_average_rating(self):
        rating_total = 0
        #only count num of books with ratings
        books_with_ratings = 0
        for rating in self.books.values():
            #check if book has rating
            if rating != None:
                rating_total += rating
                books_with_ratings += 1
        return rating_total/books_with_ratings

 
 #Book class        
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("This book's ISBN # had been updated to {isbn}".format(isbn = self.isbn))

    def add_rating(self, rating):
        if (rating >= 0) and (rating <= 4):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        return ((self.title == other_book.title) and (self.isbn == other_book.isbn))

    def get_average_rating(self):
            rating_total = 0
            for rating in self.ratings:
                rating_total += rating
            return rating_total/len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{title}".format(title = self.title)

#Fiction class
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)


#Non-fiction class
class Non_fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

#TombRater class
class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users:
            user = self.users.get(email)
            user.read_book(book,rating)
            if book in self.books: 
                self.books[book] += 1
            else:
                self.books[book] = 1
            if rating != None:
                book.add_rating(rating)
        else:
            print("No user with email {email}!".format(email = email))

    def add_user(self, name, email, user_books = None):
        email_domains = [".com", ".edu", ".org"]
        if ("@" in email) and any(domain in email for domain in email_domains):
            user = User(name, email)
            self.users[email] = user
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)
        else:
            print("Invalid email")


    def print_catalog(self):
        print("Books:")
        for book in self.books.keys():
            print(book)


    def print_users(self):
        print("Users:")
        for key, value in self.users.items():
            print(value)

    def most_read_book(self):
        frequency = 0
        most_read = None
        for book, num in self.books.items():
            if num > frequency:
                frequency = num
                most_read = book
        return most_read

    def get_n_most_read_books(self, n):
        if n > len(self.books):
            return "The number you have entered is larger than the number of books"
        else:
            counter = 0
            most_read_list = []
            while (counter < n):
                frequency = 0
                most_read = None
                #Add most read book to most_read_list without changing original dictionary
                for book, num in self.books.items():
                    if num > frequency and (book.title not in most_read_list):
                        frequency = num
                        most_read = book
                most_read_list.append(most_read.title)
                counter +=1
            return most_read_list


    def get_n_most_prolific_readers(self, n): 
        if n > len(self.users):
            return "The number you have entered is larger than the number of users"
        else:
            counter = 0
            prolific_readers_list = []
            while (counter < n):
                num_books = 0
                reader = None
                #Add most read book to prolific_readers_list without changing original dictionary
                for user in self.users.values():
                    if len(user.books) > num_books and (user.name not in prolific_readers_list):
                        num_books = len(user.books)
                        reader = user
                prolific_readers_list.append(reader.name)
                counter +=1
            return prolific_readers_list


    def highest_rated_book(self):
        avg_rating = 0
        highest_rated = None
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > avg_rating:
                avg_rating = rating
                highest_rated = book
        return highest_rated

    def most_positive_user(self):
        avg_rating = 0
        highest_rater = None
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > avg_rating:
                avg_rating = rating
                highest_rater = user
        return highest_rater


    def __repr__(self):
        return "{num_users} have read {num_books}".format(num_users = len(self.users), num_books = len(self.books))
