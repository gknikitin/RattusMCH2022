from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

# Получение текса, передача в нейросетевой классификатор

class OriginalTextForm(FlaskForm):
	original_text = TextAreaField('Original Text', validators=[Length(min=20, max=10000)], render_kw={'placeholder': 'Введите текст..'})
	generate = SubmitField('Генерировать текст')
	predict = SubmitField('Анализировать')
