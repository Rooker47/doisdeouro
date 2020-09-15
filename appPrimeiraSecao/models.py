from django.db import models
from django.db import utils
from django.utils import timezone


GRADUACAO = [
    ('TC PM', 'Ten Cel PM'),
    ('Maj PM', 'Maj PM'),
    ('Cap PM', 'Cap PM'),
    ('1° Ten PM', '1° Ten PM'),
    ('2° Ten PM', '2° Ten PM'),
    ('ST PM', 'Sub Ten PM'),
    ('1° Sgt PM', '1° Sgt PM'),
    ('2° Sgt PM', '2° Sgt PM'),
    ('3° Sgt PM', '3° Sgt PM'),
    ('Cb PM', 'Cb PM'),
    ('Sd PM', 'Sd PM'),
]

ESTADO = [
    ('PE', 'Pernambuco'),
    ('PB', 'Paraíba'),
    ('RN', 'Rio Grande do Norte'),
]

CIDADE = [
    ('Carpina', 'Carpina'),
    ('Paudalho', 'Paudalho'),
    ('Timbauba', 'Timbaúba'),
    ('Tracunhaem', 'Tracunhaém'),
    ('Lagoa do Carro', 'Lagoa do Carro'),
    ('Lagoa do Itaenga', 'Lagoa do Itaenga'),
    ('Buenos Aires', 'Buenos Aires'),
    ('Alianca', 'Aliança'),
    ('Camutanga', 'Camutanga'),
    ('Ferreiros', 'Ferreiros'),
    ('Macaparana', 'Macaparana'),
    ('Sao Vicente Ferrer', 'São Vicente Férrer'),
    ('Vicencia', 'Vicência'),
    ('Nazare da Mata', 'Nazaré da Mata'),
]

class Pessoa(models.Model):
    graduacao = models.CharField(max_length=12, verbose_name="graduação", choices=GRADUACAO)
    matricula = models.IntegerField(primary_key=True)
    nome_guerra = models.CharField(max_length=30, verbose_name="nome de guerra")

    def __str__(self):
        return "{} {}".format(self.graduacao, self.nome_guerra)


class Contato(models.Model):
    tel1 = models.CharField(max_length=16, verbose_name="telefone")
    tel2 = models.CharField(max_length=16, null=True, blank=True, verbose_name="telefone")
    email = models.EmailField(default=None, verbose_name="e-mail")
    idPessoaContato = models.OneToOneField(Pessoa, on_delete=models.CASCADE, verbose_name="identificação")

    def __str__(self):
        return "{}".format(self.idPessoaContato)


class Endereco(models.Model):
    endereco = models.CharField(max_length=50, verbose_name="endereço")
    cidade = models.CharField(max_length=30, choices=CIDADE)
    bairro = models.CharField(max_length=30)
    estado = models.CharField(max_length=2, choices=ESTADO, default='PE')
    idPessoaEndereco = models.OneToOneField(Pessoa, on_delete=models.CASCADE, verbose_name="identificação")

    def __str__(self):
        return "{}".format(self.idPessoaEndereco)
