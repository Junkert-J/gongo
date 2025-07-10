import pyttsx3
import time
from datetime import datetime, timedelta

# A função 'falar' continua a mesma
def falar(texto):
    """Usa a biblioteca pyttsx3 para converter texto em fala."""
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# --- NOVA FUNÇÃO DE CÁLCULO ---
def calcular_proximo_horario_fixo(agora, intervalo):
    """
    Calcula o próximo horário de alerta baseado em slots fixos na hora.
    Ex: Se o intervalo é 10, os alertas sÃ£o em :00, :10, :20, :30, etc.
    """
    # 1. Calcula qual seria o minuto alvo no próximo "slot"
    # A matemática: (minuto_atual // intervalo + 1) * intervalo
    # Ex: min 34, int 10 -> (34 // 10 + 1) * 10 -> (3 + 1) * 10 -> 40. O alvo é :40.
    # Ex: min 8, int 15 -> (8 // 15 + 1) * 15 -> (0 + 1) * 15 -> 15. O alvo é :15.
    minuto_alvo = ((agora.minute // intervalo) + 1) * intervalo
    
    # 2. Cria uma cópia do horário atual para modificar
    proximo_horario = agora

    # 3. Trata o caso de virar a hora (ex: alvo é o minuto 60)
    if minuto_alvo >= 60:
        # AvanÃ§a para a próxima hora e zera os minutos/segundos
        proximo_horario = proximo_horario + timedelta(hours=1)
        proximo_horario = proximo_horario.replace(minute=0, second=0, microsecond=0)
    else:
        # Apenas ajusta para o minuto alvo e zera os segundos
        proximo_horario = proximo_horario.replace(minute=minuto_alvo, second=0, microsecond=0)
        
    return proximo_horario

# --- SEÇÃO DE INPUT MODIFICADA ---
opcoes_validas = [10, 15, 30, 60]
while True:
    try:
        intervalo_minutos = int(input(f"Qual o intervalo do alerta? Escolha entre {opcoes_validas}: "))
        if intervalo_minutos in opcoes_validas:
            break # Sai do loop se a escolha for válida
        else:
            print("Opção inválida. Por favor, escolha um dos valores da lista.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um nÃºmero.")

mensagem_customizada = input("Qual a mensagem que vocÃª quer ouvir? (Use {hora} e {minuto}) \n> ")

# --- LÃ“GICA PRINCIPAL FINAL ---

print(f"\nOk! Sincronizando alertas para cada {intervalo_minutos} minutos dentro da hora.")
print("Pressione Ctrl+C para parar.")

# Calcula o primeiro alerta usando a nova função
agora = datetime.now()
proximo_alerta = calcular_proximo_horario_fixo(agora, intervalo_minutos)
print(f"O próximo alerta será às {proximo_alerta.strftime('%H:%M:%S')}.")

try:
    while True:
        if datetime.now() >= proximo_alerta:
            hora_formatada = proximo_alerta.strftime('%H')
            minuto_formatado = proximo_alerta.strftime('%M')
            
            mensagem_final = mensagem_customizada.format(hora=hora_formatada, minuto=minuto_formatado)
            
            print(f"Anunciando: '{mensagem_final}'")
            falar(mensagem_final)
            
            # Calcula o próximo alerta a partir do que acabou de tocar
            proximo_alerta = calcular_proximo_horario_fixo(proximo_alerta, intervalo_minutos)
            print(f"Próximo alerta sincronizado para as {proximo_alerta.strftime('%H:%M:%S')}.")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nAlerta sincronizado encerrado.")
