from scholarly import scholarly
import pickle

DATA_PATH = "data/"
org = scholarly.search_org("University of Bahrain")
authors = scholarly.search_author_by_organization(org[0]['id'])

authors_details = []
author_index = 1
for author in authors:
    author_details = scholarly.fill(author)
    print(f"author {author_index}: {author_details['name']}")
    authors_details.append(author_details)
    author_index += 1

with open(DATA_PATH + 'authors.pkl', 'wb') as out:
    pickle.dump(authors_details, out, pickle.HIGHEST_PROTOCOL)

author_index = 1
publications = []
for author in authors:
    print(f"author {author_index}: {author_details['name']}")
    publication_index = 1
    for publication in author_details["publications"]:
        publication_details = scholarly.fill(publication)
        print(f"\tpublication {publication_index}: {publication_details['bib']['title']}")
        publications.append(publication_details)
        publication_index += 1

    with open('publications.pkl', 'wb') as out:
        pickle.dump(publications, out, pickle.HIGHEST_PROTOCOL)
