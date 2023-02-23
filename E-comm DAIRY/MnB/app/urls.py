from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm ,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
   path("",views.home, name='home'),
   path("about/",views.aboutUs, name='about'),
   path("contact/",views.contactUs, name='contact'),
   path("category/<slug:val>",views.categoryView.as_view(), name='category'),
   path("category-title/<val>",views.categoryTitle.as_view(), name='category-title'),
   path("product-detail/<int:pk>",views.productView.as_view(), name='product-detail'),
   path("profile/",views.ProfileView.as_view(), name='profile'),
   path("address/",views.address, name='address'),
   path("updateAddress/<int:pk>",views.updateAddress.as_view(),name='updateAddress'),


#login-autentication
   path("customerReg",views.customerRegistrationView.as_view(), name='customerReg'),
   path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),name='login'),
   path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name= 'app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
   path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
   path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
   path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name= 'password_reset'),
   path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name= 'password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name= 'password_reset_confirm'),
   path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name= 'password_reset_confirm'),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)