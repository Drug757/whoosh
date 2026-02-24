from engine import SearchEngine
from datetime import datetime

def run_demo():
    engine = SearchEngine()

    # 1. Добавляем тестовые данные
    print("Индексация документов...")
    engine.add_document(
        u"/docs/python_intro.txt", 
        u"Введение в Python",
        u"Python — это мощный язык программирования. Он прост в изучении и эффективен.",
        u"python,обучение",
        datetime.now()
    )
    
    engine.add_document(
        u"/docs/whoosh_guide.txt", 
        u"Гайд по Whoosh",
        u"Whoosh позволяет создавать быстрые поисковые движки на Python без лишних зависимостей.",
        u"search,python,library",
        datetime.now()
    )

    # 2. Тестируем поиск
    print("\n--- Тест 1: Поиск по слову 'Python' ---")
    engine.search("Python")

    print("\n--- Тест 2: Поиск с опечаткой 'Pyton' ---")
    engine.search("Pyton")

    print("\n--- Тест 3: Сложный запрос ---")
    engine.search("эффективен")

if __name__ == "__main__":
    run_demo()
