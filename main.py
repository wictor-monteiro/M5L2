import pyttsx3
engine = pyttsx3.init()
# Configurando parâmetros
engine.setProperty('rate', 150)  # Velocidade da fala
engine.setProperty('volume', 0.9)  # Volume
# Selecionando uma voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 - masculino, 1 - feminino (dependendo do sistema)
# Texto para vocalizar
text = "Olá mundo, será?"
# Vocalizando o texto
engine.say(text)
# Executando a síntese
engine.runAndWait()