from django.apps import AppConfig


# class PostsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'posts'

class PostsConfig(AppConfig):
    name = 'posts'

    def ready(self):
        import posts.signals
