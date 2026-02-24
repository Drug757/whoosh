from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser, MultifieldParser, GroupHighlighting
from whoosh import scoring
from config import INDEX_DIR, schema
import os

class SearchEngine:
    def __init__(self):
        if os.path.exists(INDEX_DIR) and os.listdir(INDEX_DIR):
            self.ix = open_dir(INDEX_DIR)
        else:
            self.ix = create_in(INDEX_DIR, schema)

    def add_document(self, path, title, content, tags, updated_dt):
        """Добавляет или обновляет документ в индексе."""
        writer = self.ix.writer()
        writer.update_document(
            path=path,
            title=title,
            content=content,
            tags=tags,
            updated=updated_dt
        )
        writer.commit()

    def search(self, user_query):
        """Выполняет поиск по заголовку и контенту."""
        with self.ix.searcher(weighting=scoring.BM25F()) as searcher:
            # Ищем сразу по двум полям
            parser = MultifieldParser(["title", "content"], self.ix.schema)
            query = parser.parse(user_query)
            
            results = searcher.search(query, limit=10, terms=True)
            
            # Логика исправлений
            corrected = searcher.suggest_phrase("content", user_query)
            
            print(f"\nНайдено результатов: {len(results)}")
            if corrected.string != user_query and len(results) == 0:
                print(f"Возможно, вы имели в виду: '{corrected.string}'?")

            for hit in results:
                print("-" * 20)
                print(f"Заголовок: {hit['title']}")
                print(f"Путь: {hit['path']}")
                # Генерируем фрагмент текста с подсветкой (snippet)
                snippet = hit.highlights("content")
                print(f"Фрагмент: ...{snippet}...")
