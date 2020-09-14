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

ARMA_ESPECIE = [
    ('Arma de fogo', 'Arma de fogo'),
    ('Colete', 'Colete'),
]

ARMA_TIPO = [
    ('Revr', 'Revólver'),
    ('Pst', 'Pistola'),
    ('Smtr', 'Submetralhadora'),
    ('Fz', 'Fuzil'),
]

PREFIXOS = [
    ('22000', 'operações'),
    ('22100', 'nazaré'),
    ('22115', 'CarpinaI'),
    ('22116', 'CarpinaII'),
]

# PESSOA ===============================================================================================================
class Pessoa(models.Model):
    graduacao = models.CharField(max_length=12, verbose_name="graduação", choices=GRADUACAO)
    matricula = models.IntegerField(primary_key=True)
    nome_guerra = models.CharField(max_length=30, verbose_name="nome de guerra")

    def __str__(self):
        return "{} {}".format(self.graduacao, self.nome_guerra)

# ARMA =================================================================================================================
class Arma(models.Model):
    especie = models.CharField(max_length=15, choices=ARMA_ESPECIE)
    tipo = models.CharField(max_length=15, choices=ARMA_TIPO)
    numero = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return "{} {}".format(self.tipo, self.numero)

# CONTATO ==============================================================================================================
class Contato(models.Model):
    tel1 = models.CharField(max_length=16, verbose_name="telefone")
    tel2 = models.CharField(max_length=16, null=True, blank=True, verbose_name="telefone")
    email = models.EmailField(default=None, verbose_name="e-mail")
    idPessoaContato = models.OneToOneField(Pessoa, on_delete=models.CASCADE, verbose_name="identificação")

    def __str__(self):
        return "{}".format(self.idPessoaContato)

# ENDEREÇO =============================================================================================================
class Endereco(models.Model):
    endereco = models.CharField(max_length=50, verbose_name="endereço")
    cidade = models.CharField(max_length=30, choices=CIDADE)
    bairro = models.CharField(max_length=30)
    estado = models.CharField(max_length=2, choices=ESTADO, default='PE')
    idPessoaEndereco = models.OneToOneField(Pessoa, on_delete=models.CASCADE, verbose_name="identificação")

    def __str__(self):
        return "{}".format(self.idPessoaEndereco)

# VIATURA ==============================================================================================================
class Viatura(models.Model):
    patrimonio = models.IntegerField(primary_key=True)
    placa = models.CharField(max_length=7)
    chassis = models.CharField(max_length=25)
    status = models.BooleanField(default=None, verbose_name='Ativada')

    def __str__(self):
        return "{}".format(self.patrimonio)

# GUARNIÇÕES ===========================================================================================================
class Guarnicao(models.Model):
    vtrPrefixo = models.CharField(max_length=9, primary_key=True, verbose_name="prefixo", choices=PREFIXOS)
    vtr = models.OneToOneField(Viatura, on_delete=models.CASCADE, verbose_name="patrimônio")
    condutor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    kmInicial = models.IntegerField(verbose_name="Km inicial")
    data = models.DateTimeField(default=timezone.now, auto_now=False, verbose_name="registro em")

    def __str__(self):
        return "{}".format(self.vtr)
