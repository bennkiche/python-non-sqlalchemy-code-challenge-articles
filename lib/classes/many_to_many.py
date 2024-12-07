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
        """Returns the list of articles written by this author."""
        return self._articles

    def magazines(self):
        """Returns the list of magazines associated with this author."""
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        """Creates a new article and associates it with the author and magazine."""
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

        # Create and associate the article with the author and the magazine
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        """Returns a list of unique topic areas (magazine categories) for this author."""
        categories = list(set(magazine.category for magazine in self.magazines()))
        return categories if categories else None




class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        
        self._name = name  # Internal attribute to store name
        self._category = category  # Internal attribute to store category
        self._articles = []  # List to store associated articles

    @property
    def name(self):
        """Returns the name of the magazine."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Allows changing the name if it's a valid string between 2 and 16 characters."""
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        """Returns the category of the magazine."""
        return self._category

    @category.setter
    def category(self, new_category):
        """Allows changing the category if it's a non-empty string."""
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = new_category

    def articles(self):
        """Returns all articles associated with the magazine."""
        return self._articles

    def contributors(self):
        """Returns a list of unique authors who contributed to the magazine."""
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        """Returns a list of titles of all articles for the magazine or None if no articles."""
        return [article.title for article in self._articles] or None

    def contributing_authors(self):
        """Returns a list of authors who have written more than 2 articles for the magazine."""
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        return [author for author, count in author_counts.items() if count > 2] or None

    @staticmethod
    def top_publisher():
        """Returns the magazine with the most articles or None if no articles."""
        if not hasattr(Magazine, "all") or not hasattr(Article, "all"):
            return None
        magazine_articles = {}
        for article in Article.all:
            magazine = article.magazine
            magazine_articles[magazine] = magazine_articles.get(magazine, 0) + 1
        return max(magazine_articles, key=magazine_articles.get, default=None)


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Invalid author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Invalid magazine")
        if not (isinstance(title, str) and 5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

        self._title = title
        self._author = author
        self._magazine = magazine

        self.__class__.all.append(self)
        self._author.articles().append(self)
        self._magazine._articles.append(self)

    @property
    def title(self):
        """The title of the article is immutable."""
        return self._title

    @property
    def author(self):
        """Returns the author of the article."""
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("New author must be an instance of Author")
        self._author.articles().remove(self)
        self._author = new_author
        new_author.articles().append(self)

    @property
    def magazine(self):
        """Returns the magazine of the article."""
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("New magazine must be an instance of Magazine")
        self._magazine._articles.remove(self)
        self._magazine = new_magazine
        new_magazine._articles.append(self)

