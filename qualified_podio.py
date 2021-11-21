def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
    # Implemente aqui a lógica da função
    podio = ''
    list2 = [nome_corredor1, nome_corredor2, nome_corredor3]
    list = [tempo_chegada1, tempo_chegada2, tempo_chegada3]
    list = sorted(list)
    for i, x in enumerate(list):
        podio += f'{i+1} - {list2[i]} - {x} minutos\n'
    return podio
    

tempo_chegada1 = 120
tempo_chegada2 = 90
tempo_chegada3 = 110
nome_corredor1 = 'a'
nome_corredor2 = 'b'
nome_corredor3 = 'c'
print(podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3))