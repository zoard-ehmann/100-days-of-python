class Post:

    def __init__(self, post: dict):
        self.id = post['id']
        self.title = post['title']
        self.subtitle = post['subtitle']
        self.body = post['body']
        self.date = post['date']
        self.author = post['author']