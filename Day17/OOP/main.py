class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        # Increasing the followers attribute of the followed account by one
        user.followers += 1
        # Increasing the following attribute of the currect account by one
        self.following += 1


user_1 = User("001", "zoard")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)