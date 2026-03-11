import os
from pymongo import MongoClient

MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")

def main():

    client = MongoClient(
        MONGODB_ATLAS_URL,
        username=MONGODB_ATLAS_USER,
        password=MONGODB_ATLAS_PWD
    )

    db = client["bookstore"]
    authors = db["authors"]

    total_authors = authors.count_documents({})
    print("----- Bookstore Author Report -----")
    print(f"Total authors: {total_authors}")
    print()

    for author in authors.find({}):

        name = author.get("name")
        nationality = author.get("nationality")
        birthday = author.get("birthday")

        print(f"Name: {name}")
        print(f"Nationality: {nationality}")
        print(f"Birthday: {birthday}")
        print("---------------------------")

    client.close()


if __name__ == "__main__":
    main()
