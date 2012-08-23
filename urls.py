from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$',                       'dashboard.views.index',            name="dashboard-index"),
    url('^metric/([\w-]+)/$',       'dashboard.views.metric_detail',    name="metric-detail"),
    url('^metric/([\w-]+).json$',   'dashboard.views.metric_json',      name="metric-json"),
    url(r'^admin/', include(admin.site.urls)),

    #
    # openid / google auth
    #

    url(r'^login/$', 'django_openid_auth.views.login_begin', name='openid-login'),
    url(r'^login-complete/$', 'django_openid_auth.views.login_complete', name='openid-complete'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),

)
