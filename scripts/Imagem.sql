
create TABLE `BASE`.`Venda`(
		id  MEDIUMINT NOT NULL AUTO_INCREMENT,
		contrato text
		,chip text
		,rastreador text
		,linha text
		,cliente text
		,cpfcnpj text
		,RGIE text
		,dataNascimento text
		,endereco text
		,bairro text
		,cidadeUF text
		,cep text
		,telefoneResidencial text
		,telefoneCelular text
		,email text
		,marca text
		,modelo text
		,cor text
		,placa text
		,panico1 text
		,panico2 text
		,valorRastreador text
		,valorBotao text
		,localvenda text
		,vendendorIndicacao text
		,localInstalacao text
		,instalador text
		,dataVenda text
		,dataInstalacao text
		,observacoes text
		,parcelas text
		,PagamentoDebito text
		,PagamentoCredito text
		,PagamentoEspecie text
		,PagamentoFinanciamento text
		,PagamentoOutros text
		,BotaoExtra text
		,BotaoExtraQuantidade text
		,carro text
		,moto text
		,caminhao text
		,outros text
		,qtdParcelas text
		, primary key(id)
)