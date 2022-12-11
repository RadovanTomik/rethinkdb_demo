import rethinkdb.errors
from rethinkdb import RethinkDB

r = RethinkDB()
r.connect("localhost", 55001).repl()


def create_database():
    try:
        r.query.db_create("demo").run()
    except rethinkdb.errors.ReqlOpFailedError:
        print("Database already exists")


def create_table():
    try:
        r.query.db("demo").table_create("heroes").run()
    except rethinkdb.errors.ReqlOpFailedError:
        print("Table already exists")


def add_wolverine():
    r.query.db("demo").table("heroes").insert({
        "hero": "Wolverine",
        "name": "James 'Logan' Howlett",
        "magazine_titles": ["Amazing Spider-Man vs. Wolverine", "Avengers",
                            "X-MEN Unlimited", "Magneto War", "Prime"],
        "appearances_count": 98
    }).run()


def print_wolverine():
    print(r.query.db("demo").table("heroes").filter({"hero": "Wolverine"}).run())


def update_appearances_count():
    r.query.db("demo").table("heroes").update({
        'appearances_count': r.query.row['appearances_count'] + 1}).run()


def remove_wolverine():
    r.query.db("demo").table("heroes").filter({"hero": "Wolverine"}).delete().run()


create_database()
create_table()
print_wolverine()
remove_wolverine()
