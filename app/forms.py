from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField
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
    slide_timeout = SliderField('Timeout slide')
    background_color = ColorField('Background color image')
    background_image = FileField('Background image')
    submit = SubmitField('Save')



