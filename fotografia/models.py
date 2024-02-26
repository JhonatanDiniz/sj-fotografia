from django.db import models

class Corretor(models.Model):
    AGENCIAS = (
        ('AC', 'Águas Claras'),
        ('AS', 'Asa Sul'),
        ('GU', 'Guará')
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    agencia = models.CharField(max_length=2, null=False, blank=False, choices=AGENCIAS)
    telefone = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f"Corretor [nome={self.nome}]"
    
    def get_name_agencia(self):
        for code, name in self.AGENCIAS:
            if code == self.agencia:
                return name
        return "Agência não encontrada"
    
    class Meta:
        verbose_name_plural = "Corretores"