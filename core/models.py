from django.db import models

class DadosCliente(models.Model):
    DISTRIBUIDORAS =[
        ('AME','AME'),
        ('Boa Vista','Boa Vista'),
        ('CASTRO - DIS','CASTRO - DIS'),
        ('CEA','CEA'),
        ('CEBDIS','CEBDIS'),
        ('CEDRAP','CEDRAP'),
        ('CEDRI','CEDRI'),
        ('CEEE-D','CEEE-D'),
        ('CEGERO','CEGERO'),
        ('CEJAMA','CEJAMA'),
        ('CELESC-DIS','CELESC-DIS'),
        ('CELETRO','CELETRO'),
        ('CELG-D','CELG-D'),
        ('CELPE','CELPE'),
        ('CEMIG-D','CEMIG-D'),
        ('CEMIRIM','CEMIRIM'),
        ('CEPRAG','CEPRAG'),
        ('CERAÇÁ','CERAÇÁ'),
        ('CERAL ANITÁPOLIS','CERAL ANITÁPOLIS'),
        ('CERAL ARAPOTI','CERAL ARAPOTI'),
        ('CERAL ARARUAMA','CERAL ARARUAMA'),
        ('CERBRANORTE','CERBRANORTE'),
        ('CERCI','CERCI'),
        ('CERCOS','CERCOS'),
        ('CEREJ','CEREJ'),
        ('CERES','CERES'),
        ('CERFOX','CERFOX'),
        ('CERGAL','CERGAL'),
        ('CERGAPA','CERGAPA'),
        ('CERGRAL','CERGRAL'),
        ('CERILUZ','CERILUZ'),
        ('CERIM','CERIM'),
        ('CERIPA','CERIPA'),
        ('CERIS','CERIS'),
        ('CERMC','CERMC'),
        ('CERMISSÕES','CERMISSÕES'),
        ('CERMOFUL','CERMOFUL'),
        ('CERNHE','CERNHE'),
        ('CERON','CERON'),
        ('CERPALO','CERPALO'),
        ('CERPRO','CERPRO'),
        ('CERR','CERR'),
        ('CERRP','CERRP'),
        ('CERSAD DISTRIBUIDORA','CERSAD DISTRIBUIDORA'),
        ('CERSUL','CERSUL'),
        ('CERTAJA','CERTAJA'),
        ('CERTEL ENERGIA','CERTEL ENERGIA'),
        ('CERTHIL','CERTHIL'),
        ('CERTREL','CERTREL'),
        ('CERVAM','CERVAM'),
        ('CETRIL','CETRIL'),
        ('CFLO','CFLO'),
        ('CHESP','CHESP'),
        ('CNEE','CNEE'),
        ('COCEL','COCEL'),
        ('CODESAM','CODESAM'),
        ('COELBA','COELBA'),
        ('COOPERA','COOPERA'),
        ('COOPERALIANÇA','COOPERALIANÇA'),
        ('COOPERCOCAL','COOPERCOCAL'),
        ('COOPERLUZ','COOPERLUZ'),
        ('COOPERMILA','COOPERMILA'),
        ('COOPERNORTE','COOPERNORTE'),
        ('COOPERSUL','COOPERSUL'),
        ('COOPERZEM','COOPERZEM'),
        ('COORSEL','COORSEL'),
        ('COPEL-DIS','COPEL-DIS'),
        ('COPREL','COPREL'),
        ('COSERN','COSERN'),
        ('CPFL Jaguari','CPFL Jaguari'),
        ('CPFL Leste Paulista','CPFL Leste Paulista'),
        ('CPFL Mococa','CPFL Mococa'),
        ('CPFL Santa Cruz','CPFL Santa Cruz'),
        ('CPFL Sul Paulista','CPFL Sul Paulista'),
        ('CPFL- PIRATININGA','CPFL- PIRATININGA'),
        ('CPFL-PAULISTA','CPFL-PAULISTA'),
        ('CRELUZ-D','CRELUZ-D'),
        ('CRERAL','CRERAL'),
        ('DCELT','DCELT'),
        ('DEMEI','DEMEI'),
        ('DMED','DMED'),
        ('EBO','EBO'),
        ('EDEVP','EDEVP'),
        ('EDP ES','EDP ES'),
        ('EDP SP','EDP SP'),
        ('EEB','EEB'),
        ('EFLJC','EFLJC'),
        ('EFLUL','EFLUL'),
        ('ELEKTRO','ELEKTRO'),
        ('ELETROACRE','ELETROACRE'),
        ('ELETROCAR','ELETROCAR'),
        ('ELETROPAULO','ELETROPAULO'),
        ('ELFSM','ELFSM'),
        ('EMG','EMG'),
        ('EMS','EMS'),
        ('EMT','EMT'),
        ('ENEL CE','ENEL CE'),
        ('ENEL RJ','ENEL RJ'),
        ('ENF','ENF'),
        ('EPB','EPB'),
        ('Equatorial AL','Equatorial AL'),
        ('Equatorial MA','Equatorial MA'),
        ('Equatorial PA','Equatorial PA'),
        ('Equatorial PI','Equatorial PI'),
        ('ESE','ESE'),
        ('ESS','ESS'),
        ('ETO','ETO'),
        ('FORCEL','FORCEL'),
        ('HIDROPAN','HIDROPAN'),
        ('LIGHT','LIGHT'),
        ('MUXENERGIA','MUXENERGIA'),
        ('RGE','RGE'),
        ('RGE SUL','RGE SUL'),
        ('SULGIPE','SULGIPE'),
        ('UHENPAL','UHENPAL'),
      
    ]
    
    GRUPO_TARIFARIO = [
        ('A1','A1'),
        ('A2','A2'),
        ('A3','A3'),
        ('A3a','A3a'),
        ('A4','A4'),
        ('A4a','A4a'),
        ('A4b','A4b'),
        ('AS','AS'),
        ('B','B'),
        ('B1','B1'),
        ('B2','B2'),
        ('B3','B3'),
        ('B4','B4'),

    ]
    
    distribuidoras = models.CharField(max_length=150,choices=DISTRIBUIDORAS,default=None)
    grupo_tarifario = models.CharField(max_length=20,choices=GRUPO_TARIFARIO,default=None)
    consumo_ponta = models.DecimalField(max_digits=50,decimal_places=5)
    consumo_fora_ponta = models.DecimalField(max_digits=50,decimal_places=5)
    demanda_contratada = models.DecimalField(max_digits=50,decimal_places=5)
    nome_cliente = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    telefone = models.CharField(max_length=100, null=True,blank=True)
    
    def __str__(self):
        return self.nome_cliente
    
    
class MinhasFaturas(models.Model):
    title = models.CharField(max_length=20)
    arq = models.FileField(upload_to='img')
    
    def __str__(self):
        return self.title

