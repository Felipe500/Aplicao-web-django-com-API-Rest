from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Leitor

def cliente_profile(sender, instance, created, **kwargs):
	if created:
		if not Group.objects.filter(name='leitor').exists():
			print("criando grupo leitor")
			Group.objects.create(nome='leitor')
		group = Group.objects.get(name='leitor')
		instance.groups.add(group)
		Leitor.objects.create(
			user=instance,
			name=instance.username,
			)
		print('perfil criado com sucesso!')

post_save.connect(cliente_profile, sender=User)