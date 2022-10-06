import boto3

#cria o serviço com suas credenciais sa aws
client = boto3.client(
  service_name="sns",
  region_name='***regiao so seu serviço***',
  aws_access_key__id='***sua access key***',
  aws_secret_access_key='***sua secret_key**8'
)

#envia o sns para o numero desejado 
client.publish(
  PhoneNumber="+5514numero",
  Menssage="Hello word"
)
