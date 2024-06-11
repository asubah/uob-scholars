from scholarly import scholarly
import pickle

org = scholarly.search_org("University of Bahrain")
authors = scholarly.search_author_by_organization(org[0]['id'])

with open("authors.txt", "w") as f:
    for author in authors:
        f.write(str(author))
        f.write("\n")

# with open('authors.pkl', 'wb') as outp:
#     pickle.dump(authors, outp, pickle.HIGHEST_PROTOCOL)


# for i in range(1, 6):
#     author = next(authors)
#     scholarly.pprint(author)
#     author_details = scholarly.fill(author)
#     scholarly.pprint(author_details)
#     publications = author_details["publications"][0]
#     pub_details = scholarly.fill(publications)
#     scholarly.pprint(pub_details)
