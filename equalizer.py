import os
from pydub import AudioSegment

def normalizar_volume(pasta_entrada, pasta_saida, volume_alvo=-20.0):
    # Cria a pasta de saída se ela não existir
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Percorre todos os arquivos na pasta de origem
    for arquivo in os.listdir(pasta_entrada):
        if arquivo.endswith(".mp3"):
            caminho_completo = os.path.join(pasta_entrada, arquivo)
            print(f"Processando: {arquivo}")

            # Carrega a música
            musica = AudioSegment.from_mp3(caminho_completo)

            # Calcula a diferença entre o volume atual da música (dBFS) e o alvo
            diferenca = volume_alvo - musica.dBFS

            # Aplica a diferença (aumenta se for mais baixa que o alvo, diminui se for mais alta)
            musica_normalizada = musica.apply_gain(diferenca)

            # Salva o novo arquivo na pasta de saída
            caminho_saida = os.path.join(pasta_saida, arquivo)
            musica_normalizada.export(caminho_saida, format="mp3", bitrate="192k")
            
    print("Processo finalizado! Todas as músicas estão no mesmo volume.")

# Substitua pelos caminhos reais do seu computador
pasta_origem = r"C:\Caminho\Para\Suas\Musicas"
pasta_destino = r"C:\Caminho\Para\Musicas_Normalizadas"

normalizar_volume(pasta_origem, pasta_destino)
