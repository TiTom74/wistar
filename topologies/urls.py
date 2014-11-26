from django.conf.urls import patterns, url
from topologies import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^create/$', views.create, name='create'),
    url(r'^error/$', views.error, name='error'),
    url(r'^dumpKvm/(?P<topo_id>\d+)/$', views.dumpKvm, name='dumpKvm'),
    url(r'^deploy/(?P<topo_id>\d+)/$', views.deploy, name='deploy'),
    url(r'^clone/(?P<topo_id>\d+)/$', views.clone, name='clone'),
    url(r'^delete/(?P<topo_id>\d+)/$', views.delete, name='delete'),
    url(r'^(?P<topo_id>\d+)/$', views.detail, name='detail'),
    url(r'^manageKvm/$', views.manageKvm, name='manageKvm'),
    url(r'^manageKvm/viewDomain/(?P<domain_id>[^/]+)$', views.viewDomain, name='viewDomain'),
    url(r'^manageKvm/startDomain/(?P<domain_id>[^/]+)$', views.startDomain, name='startDomain'),
    url(r'^manageKvm/stopDomain/(?P<domain_id>[^/]+)$', views.stopDomain, name='stopDomain'),
    url(r'^manageKvm/undefineDomain/(?P<domain_id>[^/]+)$', views.undefineDomain, name='undefineDomain'),
    url(r'^manageKvm/viewNetwork/(?P<network_name>[^/]+)$', views.viewNetwork, name='viewNetwork'),
    url(r'^manageKvm/startNetwork/(?P<network_name>[^/]+)/$', views.startNetwork, name='startNetwork'),
    url(r'^manageKvm/stopNetwork/(?P<network_name>[^/]+)/$', views.stopNetwork, name='stopNetwork'),
    url(r'^manageKvm/undefineNetwork/(?P<network_name>[^/]+)/$', views.undefineNetwork, name='undefineNetwork'),
)