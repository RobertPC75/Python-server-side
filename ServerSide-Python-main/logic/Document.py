class Document(object):

    def __init__(self, id_document: int, title: str = 'Title', number_pages: int, category: str = "Category", author: str = "Author":

        self._id_document= id_document
        self._title = title
        self._number_pages = number_pages
        self._category = category
        self._author = author



    @property
    def id_document(self) -> int:
        return self._id_document

    @id_document.setter
    def id_document(self, id_document: int):
        self._id_document = id_document

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def number_pages(self) -> int:
        return self._number_pages

    @number_pages.setter
    def number_pages(self, number_pages: int):
        self._number_pages = number_pages

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, category: str):
        self._category = category

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author: str):
        self._author = author

    def __str__(self):
        """ Returns str of document.
          :returns: sting document
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4})'.format(self.id_document, self.title, self.number_pages, self.category, self.author)

