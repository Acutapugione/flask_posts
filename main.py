from db import Session, Author, Post, Comment, down, up, CRUD, engine
from sqlalchemy import select

down()
up()


author = Author("Vasya", "vasya228@gmail.com", "i_am_motherfugger")
posts = [Post(f"title #{x}", f"content #{x}") for x in range(10)]
author.posts.extend(posts)
Session.add(author)


smth = select(Author)

author = Session.scalar(smth.limit(1))
print(author.nickname)
with Session.no_autoflush:
    for post in author.posts:
        comment = Comment("AC/DC rules", "vasya approved")
        author.comments.append(comment)
        post.comments.append(comment)
Session.add(comment)
crud = CRUD()

for author in crud.get_list(Author):
    print(author.nickname)
