from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Informações de autenticação, se necessário
auth_provider = PlainTextAuthProvider(username='seu_usuario', password='sua_senha')

# Conectando ao cluster
cluster = Cluster(['endereco_do_servidor_cassandra'], auth_provider=auth_provider)
session = cluster.connect()

# Selecionando um keyspace (se aplicável)
session.set_keyspace('nome_do_seu_keyspace')

# Teste de conexão executando uma query
result = session.execute("SELECT release_version FROM system.local")
for row in result:
    print("Versão do Cassandra:", row.release_version)

# Fechando a conexão
cluster.shutdown()
