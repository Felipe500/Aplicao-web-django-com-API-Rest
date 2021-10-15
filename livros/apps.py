from django.apps import AppConfig


class LivrosConfig(AppConfig):
    
    name = 'livros'
    def ready(self):
        import livros.signals
