from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signin/', views.signin_Page, name = 'signin_Page'),
    path('login/', views.login_page, name= 'login_page'),
    path('logout/', views.logoutpage, name= 'logout_page'),
    path('accoutn/<int:id>', views.accountpage, name = 'accountpage'),
    path('add_to_cart/<int:id1>,<int:id2>', views.add_to_cart , name = 'add_to_cart'),
    path('mycart/<int:id>', views.mycart, name = 'mycart'),
    path('veg_page/', views.veg_page, name = 'veg_page'),
    path('topoffer_page/', views.topoffer_page, name = 'topoffer_page'),
    path('todaydeal_page/', views.todaydeal_page, name = 'todaydeal_page'),
    path('address/', views.address, name = 'address'),
    path('payment/', views.payment, name = 'payment'),
    path('fruit_page/', views.fruit_page, name = 'fruit_page'),
    path('toy_page/', views.toy_page, name = 'toy_page'),
    path('house_page/', views.house_page, name = 'house_page'),
    path('school_page/', views.school_page, name = 'school_page'),
    path('spices_page/', views.spices_page, name = 'spices_page'),
    path('payment/', views.payment, name = 'payment'),
    path('cookingessential_page/', views.cookingessential_page, name = 'cookingessential_page'),
    path('personalcare_page/', views.personalcare_page, name = 'personalcare_page'),
    path('cleaning_page/', views.cleaning_page, name = 'cleaning_page'),
    path('beverges_page/', views.beverges_page, name = 'beverges_page'),
    path('packagedfood_page/', views.packagedfood_page, name = 'packagedfood_page'),
    path('pantry_page/', views.pantry_page, name='pantry_page'),
    path('stationery_page/', views.stationery_page, name='stationery_page'),
    path('delete/<int:id>', views.del_cart, name = 'del_cart'),
    path('update/<int:id>', views.update_account, name = 'update'),
    path('checkout/<int:id>', views.checkout, name='checkout'),
    path('product_detail/<int:id>' ,views.product_detail, name='product_detail')

]

