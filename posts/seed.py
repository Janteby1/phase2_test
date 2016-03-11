import csv 
from posts.models import WCard, BCard 

# '''
# to run
# 1) python3 manage.py shell
# 2) from posts.seed import seed
# 3) save ?
# '''

# def seed_file():
#     # open the file with information we want to seed from 
#     with open("posts/black_cards.txt", "r") as seed_file:

#         "this seeds a DB from a file using csv reader"
#         # use csv reader to split the each line in the file by tab or comma
#         reader = csv.reader(seed_file, delimiter="\t")

#         for row in reader:
#             print (row) # print each row for testing
#                 # for each line create an object in the db
#             _, created = BCard.objects.get_or_create(
#                 # give each part of the db object a positional from the seed file 
#                 content = row[0],
#                 )
        


def seed_from_file_black():
    "This seeds the db from a tab seperated file without using csv reader"
    # open text file for reading
    with open("posts/black_cards.txt", "r") as seed_file:

    # iterate across each line
        for line in seed_file:
            # get line
            # split on tab
            split = line.split("\t")
            # print (split)
            # second part is text
            length = len(split)
            print (length)

            for i in range (length-1):
                content = split[i]
                print (content)
                # make post object with text and title
                card = BCard(content=content)
                card.save()
         


def seed_from_file_white():
    "This seeds the db from a tab seperated file without using csv reader"
    # open text file for reading
    with open("posts/white_cards2.txt", encoding='latin-1') as seed_file:

    # iterate across each line
        for line in seed_file:
            # get line
            # split on tab
            split = line.split("\t")
            # print (split)
            # second part is text
            length = len(split)
            print (length)

            for i in range (length-1):
                content = split[i]
                print (content)
                # make post object with text and title
                card = WCard(content=content)
                card.save()



        