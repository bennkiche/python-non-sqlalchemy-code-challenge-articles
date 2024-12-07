class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        self._articles = []
        
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list(set(article.magazine for article in self._articles))
    
    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Invalid magazine")
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article
    
    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines())) or None


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Magazine name must be between 2 and 16 characters")
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")
        self._articles = []
        self.__class__.all_magazines.append(self)
        
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
    def articles(self):
        return self._articles
    
    def contributors(self):
        return list(set(article.author for article in self._articles))
    
    def article_titles(self):
        return [article.title for article in self._articles] or None
    
    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            authors_count[article.author] = authors_count.get(article.author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2] or None
    
    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()))


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author) or not isinstance(magazine, Magazine):
            raise ValueError("Invalid author or magazine")
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be between 5 and 50 characters")
        self._author = author
        self._magazine = magazine
        self._author.articles().append(self)
        self._magazine._articles.append(self)
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine

