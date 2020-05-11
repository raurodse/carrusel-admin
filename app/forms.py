from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import Input
from wtforms.widgets.core import HTMLString, html_params, escape


class SliderWidget(Input):
    def __call__(self,field,**kargs):
        kargs.setdefault('type','range')
        self.input_type = 'range'
        return super(SliderWidget,self).__call__(field, **kargs)


class SliderField(DecimalField):
    widget = SliderWidget()


class ColorWidget(Input):
    def __call__(self,field,**kargs):
        kargs.setdefault('type','color')
        self.input_type = 'color'
        return super(ColorWidget,self).__call__(field, **kargs)


class ColorField(StringField):
    widget = ColorWidget()


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class CarruselSettingsForm(FlaskForm):
    slide_timeout = SliderField('Timeout slide',default=0)
    transition = SelectField('Transition',choices=[('fade','Fade'),('pushleft','Push left'),('pushright','Push right'),('pushup','Push up'),('pushdown','Push down')])
    background_color = ColorField('Background color image')
    background_image = FileField('Background image')
    title_size = SelectField('Title size',choices=[('8','8 px'),('9','9 px'),('10','10 px'),('11','11 px'),('12','12 px'),('13','13 px'),('14','14 px'),('15','15 px'),('16','16 px'),('18','18 px'),('20','20 px')])
    description_size = SelectField('Description size',choices=[('8','8 px'),('9','9 px'),('10','10 px'),('11','11 px'),('12','12 px'),('13','13 px'),('14','14 px'),('15','15 px'),('16','16 px'),('18','18 px'),('20','20 px')])
    fullscreen = BooleanField('Fullscreen videos')
    submit = SubmitField('Save')



