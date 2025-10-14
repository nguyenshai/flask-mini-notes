from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

from app.models import User, Note

def test_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

        u1 = User(username='test_user', email='test@example.com', password='123456')
        db.session.add(u1)
        db.session.commit()

        note = Note(content='First note', author=u1)
        db.session.add(note)
        db.session.commit()

        print(User.query.all())
        print(Note.query.all())

test_db()

if __name__ == "__main__":
    app.run(debug=True)