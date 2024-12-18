class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("title must be a string between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine

    @property
    def title(self):
        return self._title  # No setter, making it immutable


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name  # No setter, making it immutable

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("category must be a non-empty string")

        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (2 <= len(new_name) <= 16):
            self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        if not self.articles():
            return None
        authors = [article.author for article in self.articles()]
        result = list(set(author for author in authors if authors.count(author) > 2))
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)
