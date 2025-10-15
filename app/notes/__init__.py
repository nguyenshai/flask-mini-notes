from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import User, Note

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # Display all notes of the logged-in user
    user_notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template('home.html', user=current_user, notes=user_notes)

@notes_bp.route('/add_note', methods=['POST'])
@login_required
def add_note():
    content = request.form.get('content')

    # Prevent adding empty notes
    if not content or content.strip() == '':
        flash('Note cannot be empty', category='error')
    else:
        # Create new note linked to the current user
        new_note = Note(content=content, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added successfully', category='success')

    return redirect(url_for('notes.home'))

@notes_bp.route('/delete/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    # Find note by id
    note = Note.query.get_or_404(note_id)

    # Ensure only the owner can delete their note
    if note.user_id != current_user.id:
        flash('Unauthorized action', category='error')
    else:
        db.session.delete(note)
        db.session.commit()
        flash('Note deleted successfully', category='info')

    return redirect(url_for('notes.home'))
