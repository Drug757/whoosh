from whoosh import index
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser
import os

schema = Schema(content=TEXT(stored=True))

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)

writer = ix.writer()
writer.add_document(content="Python это язык программирования")
writer.add_document(content="Whoosh используется для поиска")
writer.commit()

# поиск
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("поиска")
    results = searcher.search(query)

    for r in results:
        print(r["content"])

print("Найдено:", len(results))