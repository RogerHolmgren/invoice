from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('customers', __name__, url_prefix='/customers')

@bp.route('/')
def index():
    db = get_db()
    customers = db.execute(
        'SELECT id, name, address, created'
        ' FROM customer'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('customers/index.html', customers=customers)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        error = None

        if not name:
            error = 'Måste ha namn.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO customer (name, address)'
                ' VALUES (?, ?)',
                (name, address)
            )
            db.commit()
            return redirect(url_for('customers.index'))

    return render_template('customers/create.html')

def get_post(id):
    return get_db().execute(
                'SELECT id, name, address, created'
                ' FROM customer'
                ' WHERE id = ?',
                (id,)
            ).fetchone()


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    cust = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE customer SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('customers.index'))

    return render_template('customers/update.html', cust=cust)

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM customer WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('customers.index'))



@bp.before_app_request
def load_hardcoded_user():
    g.user = get_db().execute(
        'SELECT * FROM user WHERE id = ?', (1,)
    ).fetchone()