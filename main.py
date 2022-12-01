from rethinkdb import RethinkDB

r = RethinkDB()
r.connect("localhost", 55001).repl()
print(r.query.db("demo").table("authors").filter({}).run())
