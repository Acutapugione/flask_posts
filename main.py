from db import Session, Author, Post, Comment, down, up
from sqlalchemy import select

down()
up()

with Session.begin() as session:
    author = Author("Vasya", "vasya228@gmail.com", "i_am_motherfugger")
    posts = [Post(f"title #{x}", f"content #{x}") for x in range(10)]
    author.posts.extend(posts)
    session.add(author)


with Session.begin() as session:
    with session.no_autoflush:
        smth = select(Author)

        author = session.scalar(smth.limit(1))
        for post in author.posts:
            comment = Comment("AC/DC rules", "vasya approved")
            author.comments.append(comment)
            post.comments.append(comment)
    session.add(comment)
