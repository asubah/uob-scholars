from scholarly import scholarly

org = scholarly.search_org("University of Bahrain")
authors = scholarly.search_author_by_organization(org[0]['id'])


for i in range(1, 6):
    author = next(authors)
    scholarly.pprint(author)
    author_details = scholarly.fill(author)
    scholarly.pprint(author_details)
    publications = author_details["publications"][0]
    pub_details = scholarly.fill(publications)
    scholarly.pprint(pub_details)
