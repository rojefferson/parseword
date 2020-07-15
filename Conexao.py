import mysql.connector

class Conexao:
  def __init__(self):
      self.mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="88461434",
      database="BASE"
      )
 

  
  def insertVenda(self,venda):
      mycursor = self.mydb.cursor()
      sql = "INSERT INTO Venda (contrato ,chip ,rastreador ,linha ,cliente ,cpfcnpj ,RGIE,dataNascimento ,endereco ,bairro ,cidadeUF ,cep ,telefoneResidencial ,telefoneCelular ,email ,marca ,modelo ,cor ,placa ,panico1 ,panico2 ,valorRastreador ,valorBotao ,localvenda ,vendendorIndicacao ,localInstalacao ,instalador ,dataVenda ,dataInstalacao ,observacoes  ,tipoPagamento ,BotaoExtra ,BotaoExtraQuantidade ,tipoVeiculo ,qtdParcelas) VALUES (%s, %s ,%s,%s, %s ,%s,%s,%s,%s, %s ,%s ,%s ,%s ,%s,%s, %s ,%s,%s, %s ,%s,%s,%s,%s, %s ,%s ,%s ,%s ,%s,%s, %s ,%s,%s, %s ,%s,%s)"
      val =  (venda.contrato ,venda.chip ,venda.rastreador ,venda.linha ,venda.cliente ,venda.cpfcnpj ,venda.RGIE,venda.dataNascimento ,venda.endereco ,venda.bairro ,venda.cidadeUF ,venda.cep ,venda.telefoneResidencial ,venda.telefoneCelular ,venda.email ,venda.marca ,venda.modelo ,venda.cor ,venda.placa ,venda.panico1 ,venda.panico2 ,venda.valorRastreador ,venda.valorBotao ,venda.localvenda ,venda.vendendorIndicacao ,venda.localInstalacao ,venda.instalador ,venda.dataVenda ,venda.dataInstalacao ,venda.observacoes ,venda.tipoPagamento ,venda.BotaoExtra ,venda.BotaoExtraQuantidade ,venda.tipoVeiculo ,venda.qtdParcelas,)
      mycursor.execute(sql, val)
      self.mydb.commit()
      mycursor.close()


