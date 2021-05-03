import pymongo

client = pymongo.MongoClient( "Here insert your Mongo DB connection link in quotes")

db = client["phishing_website"]
collection = db["phishing_website"]


def add_url(url=''):
    post = {"url": url}
    collection.insert_one(post)


def url_in_database(url=''):
    finding = collection.find({"url": url})
    exist = True
    if finding:
        for result in finding:
            return exist
        exist = False
    return exist

