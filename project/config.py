from whoosh.fields import SCHEMA, TEXT, KEYWORD, ID, DATETIME
import os

# Путь к папке с индексом
INDEX_DIR = "indexdir"

# Определение схемы
# stored=True означает, что поле можно будет прочитать из результатов поиска
schema = Schema(
    path=ID(stored=True, unique=True),
    title=TEXT(stored=True),
    content=TEXT(stored=True),
    tags=KEYWORD(stored=True, commas=True),
    updated=DATETIME(stored=True)
)

if not os.path.exists(INDEX_DIR):
    os.mkdir(INDEX_DIR)
