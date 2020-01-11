from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test_template/$', views.test_template, name='test_template'),
  url(r'^musicos/$', views.musicos, name='list_musicos'),
  url(r'^grupos/$', views.grupos, name='list_grupos'),
  url(r'^albums/$', views.albums, name='list_albums'),
  url(r'^add_musico/$', views.add_musico, name='add_musico'),
  url(r'^add_grupo/$', views.add_grupo, name='add_grupo'),
  url(r'^add_album/$', views.add_album, name='add_album'),
  path('edit_musico/<int:pk>', views.update_musico),
  path('edit_grupo/<int:pk>', views.update_grupo),
  path('edit_album/<int:pk>', views.update_album),
  path('delete_musico/<int:pk>', views.delete_musico),
  path('delete_grupo/<int:pk>', views.delete_grupo),
  path('delete_album/<int:pk>', views.delete_album),
  url(r'^info_musicos/$', views.info_musicos, name='info_musicos'),
  url(r'^info_grupos/$', views.info_grupos, name='info_grupos'),
  url(r'^info_albums/$', views.info_albums, name='info_albums'),
  path('detail_musico/<int:pk>', views.detail_musico),
]
