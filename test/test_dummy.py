Se você ainda não tem um cluster Amazon EKS configurado, você pode seguir os passos abaixo para criar um12:

Instale e configure a AWS CLI: A AWS CLI é uma ferramenta de linha de comando para trabalhar com os serviços da AWS, incluindo o Amazon EKS2. Para instalar a versão mais recente, consulte Instalar ou atualizar para a versão mais recente da AWS CLI no AWS Command Line Interface Guia do usuário.
Crie uma chave de acesso da AWS: Para provisionar recursos na AWS com base na linha de comando, você precisará obter um ID de chave de acesso da AWS e uma chave secreta para usar na linha de comando2.
Configure a AWS CLI: Depois de instalar a AWS CLI, execute as etapas a seguir para configurá-la2.
Crie um cluster do Amazon EKS: Para criar um cluster do Amazon EKS, você precisa usar a console da AWS ou a linha de comando da AWS (AWS CLI) para configurar as credenciais da sua conta e criar um cluster do EKS1.
Configure o acesso ao cluster: Após criar o cluster, você precisa configurar o acesso ao cluster para que possa gerenciá-lo usando o Kubernetes CLI

Configure as credenciais da AWS: No seu repositório do GitHub, vá para Settings > Secrets e adicione os seguintes segredos:
AWS_ACCESS_KEY_ID: a chave de acesso do seu usuário IAM da AWS.
AWS_SECRET_ACCESS_KEY: a chave de acesso secreta do seu usuário IAM da AWS.