# Author: Christopher Thompson
# Reciation: Tuesday 8AM, Carter Tillquist
# Assignment 10: Python Project


# Description: This function takes in a file with a list of authors and books seperated by commas
# it reads each line from the file and organizes the name and author of each book into a listed
# it then returns a list the the book name followed by the author name
def read_books(filename):
    # test to see that file opens correctly
    try:
        file_object = open(filename, "r")

    # if file does not open correctly, print error message
    except:
        return None

    fileInfo = []
    fileInfo2 = []

    # store the author and name of each book in a list
    for data in file_object:
        data = data.strip() # remove whitespace and new line
        fileInfo = (data.split(',')) # store the data into a list
        fileInfo.reverse() # reverse the info in the list so title comes first
        fileInfo2.append(fileInfo) # add the new title and author to list
    if (fileInfo2[0][0] == ''): # check if file is empty, if so return empty list
        return []
    else: # if not empty return the filled list
        return fileInfo2 # return the list of titles and authors

# Description: This function takes in a file that contains a user followed by the ratings of that user
# for every book contained in the file with the books. This function reads through each line of the
# file and organizes each user with their book ratings into a dictionary and returns this dictionary
def read_users(user_file):
        # test to see that file opens correctly
        try:
            file_object = open(user_file, "r")
        # if file does not open correctly, print error message
        except:
            return None

        listed_data = []
        ratings = []
        dictionary = {}

        #cycle through each line of file
        for data in file_object:
            listed_data = data.split() # store data from line in a list
            key = listed_data[0] # set key equal to the name of user
            listed_data.pop(0) # get rid of user_name from list
            ratings = [int(n) for n in listed_data] # create a list containing the user ratings
            dictionary[key] = ratings # set the dictionary at the user_id equal to their ratings



        return dictionary


# Description: This function takes in the dictionary of the user name and user ratings
# it goes through each index of the ratings for each user to calculate the average rating
# of every book in the book file
def calculate_average_rating(ratings_dict):
    listed = []
    sum1 = 0
    length = 0

    listed =  ratings_dict.values() # create a list that stores each users ratings

    length = len(listed[0]) # get the length of one part of the list to find the total number of books
    avg_ratings = [] # create a list that will store the average rating for each book

    for h in range(length): # cycle through each book rating for each person
        sum1 = 0 # reset sum each time the rating index is changed
        avg = 0. # reset avg
        j = 0 # reset amount of numbers that are not zero
        for i in ratings_dict: # cycle through each users rating for each book
            if ratings_dict[i][h] != 0: # look to see if the rating(h) from user(i) is 0
                j+=1 # if rating is not 0, add to j which will be the value the sum is divided by
            sum1 += ratings_dict[i][h] #add each users rating for the specified book to the sum
        if j == 0: # if j is 0, that means all ratings for that book were 0 and the average is 0
            avg = 0
        else: # if j is greater than 0, there was at least 1 rating for the book and the average needs to be calculated
            avg = float(sum1)/float(j)

        avg_ratings.append(avg) # add each books average rating to the average rating list

    return avg_ratings # return the list with all of the average ratings for each book

# Description: This function takes in an index value, the list of books and authors from read_books,
# and the list of average ratings of every book from calculate_average_rating. The function uses the
# index value to find the book at the index value and find the rating for the book at the index values
# the function returns a string that contains this infromation
def lookup_average_rating(index, book_dict, avg_ratings_dict):
    rating = avg_ratings_dict[index] # get average rating for the book (index)
    book = book_dict[index][0] # get the name of the book
    author = book_dict[index][1] # get the book author
    return "(%.2f) %s by %s" % (rating, book, author)


# This class takes all of the functions from the previous code and organizes them into a class
# it then uses these functions to find the most similar users and to recommend books to a user
class Recommender:
    def __init__(self, books_filename, ratings_filename):
        self.book_list = [] # list returned from read_books function
        self.user_dictionary = {} # dictionary returned from read_users function
        self.average_rating_list = [] # list returned from calculate_average_rating function

        self.read_books(books_filename)
        self.read_users(ratings_filename)
        self.calculate_average_rating()

    #test to see class works
    def __repr__(self):
        return "testing..."

    # Description: This function takes in a file with a list of authors and books seperated by commas
    # it reads each line from the file and organizes the name and author of each book into a listed
    # it then returns a list the the book name followed by the author name
    def read_books(self, file_name):

        # test to see that file opens correctly
        try:
            file_object = open(file_name, "r")
        # if file does not open correctly, print error message
        except:
            return None

        fileInfo = []

        # store the author and name of each book in a list
        for data in file_object:
            data = data.strip() # remove whitespace and new line
            fileInfo = (data.split(',')) # store the data into a list
            fileInfo.reverse() # reverse the info in the list so title comes first
            self.book_list.append(fileInfo) # add the new title and author to list

        if (self.book_list[0][0] == ''): # check if file is empty, if so return empty list
            return []
        else:
            return self.book_list # return the list of titles and authors

    # Description: This function takes in a file that contains a user followed by the ratings of that user
    # for every book contained in the file with the books. This function reads through each line of the
    # file and organizes each user with their book ratings into a dictionary and returns this dictionary
    def read_users(self, user_file):
        # test to see that file opens correctly
        try:
            file_object = open(user_file, "r")
        # if file does not open correctly, print error message
        except:
            return None
        listed_data = []
        ratings = []

        #cycle through each line of file
        for data in file_object:
            listed_data = data.split() # create a list out of info from file
            key = listed_data[0] # get the name of the user
            listed_data.pop(0) # remove user name from list
            ratings = [int(n) for n in listed_data] # create a list of ratings for each user
            self.user_dictionary[key] = ratings # store the user name and the user ratings in dictionary



        return self.user_dictionary

    # Description: This function goes through each index of the ratings for each user
    #  to calculate the average rating of every book in the book file it then returns a
    # list with every average rating for every book
    def calculate_average_rating(self):
        listed = []
        sum1 = 0
        length = 0


        listed =  self.user_dictionary.values() # create a list that stores each users ratings

        length = len(listed[0]) # get the length of one part of the list to find the total number of books
        self.average_rating_list = [] # create a list that will store the average rating for each book

        for h in range(length): # cycle through each book rating for each person
            sum1 = 0 # reset sum each time the rating index is changed
            avg = 0. # reset avg
            j = 0 # reset amount of numbers that are not zero
            for i in self.user_dictionary: # cycle through each users rating for each book
                if self.user_dictionary[i][h] != 0: # look to see if the rating(h) from user(i) is 0
                    j+=1 # if rating is not 0, add to j which will be the value the sum is divided by
                sum1 += self.user_dictionary[i][h] #add each users rating for the specified book to the sum
            if j == 0: # if j is 0, that means all ratings for that book were 0 and the average is 0
                avg = 0
            else: # if j is greater than 0, there was at least 1 rating for the book and the average needs to be calculated
                avg = float(sum1)/float(j)

            self.average_rating_list.append(avg) # add each books average rating to the average rating list

        return self.average_rating_list # return the list with all of the average ratings for each book

    # Description: This function takes in an index value the function uses the index value to find
    # the book at the index value and find the rating for the book at the index values
    # the function returns a string that contains this infromation
    def lookup_average_rating(self, index):
        rating = self.average_rating_list[index] # get average rating for book (index)
        book = self.book_list[index][0] # get the book name
        author = self.book_list[index][1] # get the authors name
        return "(%.2f) %s by %s" % (rating, book, author)

    #Description: This function takes in the name of two users and calculates their calc_similarity
    # score based on their ratings for every book. The function uses the user dictionary to get the
    # ratings for the user for every book and then multiplies and adds the ratings of every book between
    # the two users to return a value that represents the two users similarity
    def calc_similarity(self, user1, user2):
        ratings1 = []
        ratings2 = []
        combined_ratings = []
        ratings1 = self.user_dictionary[user1] # create a list of all the ratings for user1
        ratings2 = self.user_dictionary[user2] # create a list of all the ratings for user2
        #cycle through all ratings for both users
        for i in range(len(ratings1)):
            combined_ratings.append(ratings1[i] * ratings2[i]) # mutliply the ratings together and put in list

        self.sim_score = sum(combined_ratings) # sum the list of multiplied ratings for each book
        return self.sim_score

    #Description: This function takes in a user id then goes through uses the
    # entire user_dictionary putting in each user into the calc_similarity function along
    # with the current_user_id to find which user is most similar to the current_user_id
    # it then returns the user that is most similar.
    def get_most_similar_user(self, current_user_id):
        sim_score = 0
        max = 0
        most_similar_user = ""
        #go throught each dictionary key/value
        for key in self.user_dictionary:
            if key == current_user_id: #if key is the same as current_user_id skip it
                continue
            # get similarity score between current_user_id and every other user in dictionary
            sim_score = self.calc_similarity(current_user_id, key)
            # if the similarity score is greater than the last, set it as new max to find most similar user
            if sim_score > max:
                most_similar_user = key
                max = sim_score
        return most_similar_user

    #Description: This function takes in the current_user_id and using the the get_most_similar_user funciton
    # finds the most similar user to the current_user_id. Then the function creates a list of all the book ratings
    # for the most similar user and the book ratings for the current_user_id to find which books the current user has
    # not read and the most_similar_user has read and rated a 3 or a 5. Then the function returns a list of all
    # these books as recomended books for the current_user_id.
    def recommend_books(self, current_user_id):
        j = 0
        similar_user_books = []
        current_user_books = []
        recomendations = []
        most_similar_user = self.get_most_similar_user(current_user_id) # find the most similar user to the current_user_id
        similar_user_books = self.user_dictionary[most_similar_user] # get list of book ratings for most sim user
        current_user_books = self.user_dictionary[current_user_id] # get list of book ratings for current user
        #go through the list of book ratings of both users
        for i in range(len(similar_user_books)):
            # if the sim user book rating at index is a 3 or a 5 and current_user_id book rating at index is a 0
            # create a recomendation for that book and add it to list of recomendaions using lookup_average_rating
            if (similar_user_books[i] == 3 or similar_user_books[i] == 5)and(current_user_books[i] == 0):
                recomendations.append(self.lookup_average_rating(i))
        return recomendations






# main for testing
def main():
    R1 = Recommender("book.txt", "ratings.txt")
    R1.read_users("ratings.txt")
    R1.read_books("book.txt")
    R1.calculate_average_rating()
    R1.lookup_average_rating(0)
    print""
    print "THIS IS THE OUTPUT FROM ASSIGNMENT10.PY:"
    print ""
    print "your sim score with ben is:", R1.calc_similarity("Justin", "Ben")
    print ""
    print "the most similar user to you is:", R1.get_most_similar_user("Justin")
    print""
    print "the books best suited for you are:", R1.recommend_books("Justin")
    # print read_books("book.txt")
    # print read_users("ratings.txt")
    # avg = calculate_average_rating(read_users("ratings.txt"))
    # lookup_average_rating(2, books, avg)

    # print "testing second object..."
    # R2 = Recommender("book2.txt", "ratings2.txt")
    # R2.read_users()
    # R2.read_books()
    # print R2.calculate_average_rating()

if __name__ == '__main__':
    main()
