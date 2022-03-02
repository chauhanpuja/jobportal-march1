from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('about', views.about,name="about"),
    path('category=<str:slug>',views.category,name="category"),
    path('detail/<str:slug>',views.detail,name="detail"),
    path('service_detail/<str:slug>',views.service_detail,name="servic_detail"),
    # path('category/<str:slug>', views.category,name="category"),
    # path('category=<int:id>', views.category,name="category"),
    path('current_job_oppening', views.job_oppening,name="job_oppening"),
    path('contact', views.contact,name="contact"),
    path('apply', views.apply,name="apply"),
    path('userlogin', views.userlogin,name="userlogin"),
    path('signup', views.signup,name="signup"),
    path('userlogout', views.userlogout,name="userlogout"),
    path('resume', views.resume,name="resume"),
    path('search', views.search,name="search"),
    path('candidate_applied', views.candidate_applied,name="candidate_applied"),
    path('apply_job/<int:id>', views.apply_job,name="apply_job"),
    path('user_signup', views.user_signup,name="user_signup"),
    path('recruiter_signup', views.recruiter_signup,name="recruiter_signup"),
    path('admin_login', views.admin_login,name="admin_login"),
    path('user_login', views.user_login,name="user_login"),
    path('recruiter_login', views.recruiter_login,name="recruiter_login"),
   
    path('admin_home', views.admin_home,name="admin_home"),
    path('user_home', views.user_home,name="user_home"),
    path('recruiter_home', views.recruiter_home,name="recruiter_home"),
    path('add_job', views.add_job,name="add_job"),
    path('view_users', views.view_users,name="view_users"),
    path('delete_user/<str:user>', views.delete_user,name="delete_user"),
    path('delete_recruiter/<str:user>', views.delete_recruiter,name="delete_recruiter"),
    path('view_recruiters', views.view_recruiters,name="view_recruiters"),
    path('recruiter_pending', views.recruiter_pending,name="recruiter_pending"),
    path('recruiter_accept', views.recruiter_accept,name="recruiter_accept"),
    path('recruiter_reject', views.recruiter_reject,name="recruiter_reject"),

    path('change_status/<int:id>', views.change_status,name="change_status"),

    
    
]