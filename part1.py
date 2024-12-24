from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Создаем форму для редактирования профиля:
class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Save Changes')

# Главная страница с формой редактирования профиля
@app.route('/', methods=['GET', 'POST'])
def index():
    form = EditProfileForm()
    if form.validate_on_submit():  # Проверка, прошла ли форма валидацию
        username = form.username.data
        email = form.email.data
        password = form.password.data
        # Обычно здесь происходит сохранение изменений в базе данных
        # Пример: user.username = username; db.session.commit()
        return redirect(url_for('profile', username=username))
    return render_template('index.html', form=form)

# Страница с профилем пользователя
@app.route('/profile/<username>')
def profile(username):
    return f'Profile of {username}'

if __name__ == '__main__':
    app.run(debug=True)
