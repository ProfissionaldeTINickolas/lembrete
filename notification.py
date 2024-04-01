import datetime
from plyer import notification

# Solicita ao usuário a data da última vacinação
data_vacina = input("Digite a data da última vacinação (dd/mm/yyyy): ")
dia, mes, ano = map(int, data_vacina.split('/'))
data_vacina = datetime.date(ano, mes, dia)

# Calcula a data da próxima vacinação
proxima_vacina = data_vacina + datetime.timedelta(days=180)

# Exibe uma notificação
notification.notify(
    title="Lembrete de Vacinação",
    message=f"A próxima vacinação de Hepatite B será em {proxima_vacina.strftime('%d/%m/%Y')}",
    timeout=10
)

#Este script irá solicitar ao usuário a data da última vacinação, calcular a data da próxima vacinação (6 meses depois) e exibir uma notificação com essa data.

#Por favor, note que você precisará instalar a biblioteca plyer se ainda não o fez. Você pode fazer isso usando o seguinte comando: pip install plyer
