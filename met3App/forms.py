from django.contrib.auth.forms import AuthenticationForm

class FormLogin(AuthenticationForm):
	def __init__(self, *args, **kwargs):
			super(FormLogin, self).__init__(*args,**kwargs)

			self.fields['username'].widget.attrs['class']= 'fsorm-control'
			self.fields['username'].widget.attrs['id']= 'exampleInputEmail1'
			self.fields['username'].widget.attrs['aria-describedby']= 'emailHelp'
			self.fields['username'].widget.attrs['placeholder']= 'Nombre de usuario'

			self.fields['password'].widget.attrs['class']= 'form-control'
			self.fields['password'].widget.attrs['id']= 'exampleInputPassword1'
			self.fields['password'].widget.attrs['placeholder']= 'Password'
