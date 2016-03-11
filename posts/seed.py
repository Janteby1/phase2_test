import csv 
from posts.models import WCard, BCard 

'''
to run
1) python3 manage.py shell
2) from posts.seed import seed
3) save ?
'''

# open the file with information we want to seed from 
with open("posts/black_cards.txt", encoding='latin-1') as seed_file:

    "this seeds a DB from a file using csv reader"
    # use csv reader to split the each line in the file by tab or comma
    reader = csv.reader(seed_file, delimiter="\t")

    for row in reader:
        print (row) # print each row for testing
            # for each line create an object in the db
        _, created = BCard.objects.get_or_create(
            # give each part of the db object a positional from the seed file 
            content = row[0],
            )
        


# def seed_from_file():
#     "This seeds the db from a tab seperated file without using csv reader"
#     # open text file for reading
#     with open("posts/black_cards.txt", "r") as seed_file:

#     # iterate across each line
#         for line in seed_file:
#             print (line)
#             # first part is title
#             content = line(' \n')
#             # make post object with text and title
#             card = BCard(content=content)
#             # save to db
#             card.save()


# # open the file with information we want to seed from 
# with open("posts/white_cards2.txt", encoding='latin-1') as seed_file:

#     "this seeds a DB from a file using csv reader"
#     # use csv reader to split the each line in the file by tab or comma
#     reader = csv.reader(seed_file, delimiter="\t")

#     for row in reader:
#         print (row) # print each row for testing
#             # for each line create an object in the db
#         _, created = WCard.objects.get_or_create(
#             # give each part of the db object a positional from the seed file 
#             content = row[0],
#             )


        