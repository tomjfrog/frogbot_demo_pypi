from flask import Flask, request
import sqlalchemy
import sqlalchemy.orm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
engine = sqlalchemy.create_engine(...)
Base = sqlalchemy.orm.declarative_base()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:///:memory:"
db = SQLAlchemy(app)



class User(Base):
    __tablename__ = "users"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String)


@app.route("/users/<username>")
def show_user(username):
    session = sqlalchemy.orm.Session(engine)

    # BAD, normal SQL injection
    stmt1 = sqlalchemy.text("SELECT * FROM users WHERE username = '{}'".format(username))
    results = session.execute(stmt1).fetchall()

    # BAD, allows SQL injection
    username_formatted_for_sql = sqlalchemy.text("'{}'".format(username))
    stmt2 = sqlalchemy.select(User).where(User.username == username_formatted_for_sql)
    results = session.execute(stmt2).scalars().all()

    # GOOD, does not allow for SQL injection
    stmt3 = sqlalchemy.select(User).where(User.username == username)
    results = session.execute(stmt3).scalars().all()


    # All of these should be flagged by query
    t1 = sqlalchemy.text(username)
    results = session.execute(t1).fetchall()
    t2 = sqlalchemy.text(text=username)
    results = session.execute(t2).fetchall()
    t3 = sqlalchemy.sql.text(username)
    results = session.execute(t3).fetchall()
    t4 = sqlalchemy.sql.text(text=username)
    results = session.execute(t4).fetchall()
    t5 = sqlalchemy.sql.expression.text(username)
    results = session.execute(t5).fetchall()
    t6 = sqlalchemy.sql.expression.text(text=username)
    results = session.execute(t6).fetchall()
    t7 = sqlalchemy.sql.expression.TextClause(username)
    results = session.execute(t7).fetchall()
    t8 = sqlalchemy.sql.expression.TextClause(text=username)
    results = session.execute(t8).fetchall()

    # t9 = db.text(username)
    # results = session.execute(t9).fetchall()
    t10 = db.text(text=username)
    results = session.execute(t10).fetchall()
