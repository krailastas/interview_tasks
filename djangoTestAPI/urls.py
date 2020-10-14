from django.conf import settings
from django.urls import path
from graphene_django.views import GraphQLView


urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True)),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
