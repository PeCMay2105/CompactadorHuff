from collections import Counter
import heapq

class Node:
    def __init__(self, frequencia, caractere=None):
        self.frequencia = frequencia
        self.caractere = caractere
        self.filhoEsquerda = None
        self.filhoDireita = None
    def __lt__(self,outro):
        return self.frequencia < outro.frequencia

def calcularFrequencia(string):
    return Counter(string)

def construirArvore(frequencias):
    heap = [Node(frequencia,valor) for valor,frequencia in frequencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        esquerda = heapq.heappop(heap)
        direita = heapq.heappop(heap)
        NovoNo = Node(esquerda.frequencia + direita.frequencia)
        NovoNo.filhoEsquerda = esquerda
        NovoNo.filhoDireita = direita
        heapq.heappush(heap,NovoNo)
    return heap[0]

def geradorDeCodigos(raiz):
    tabelaCodigos = {}
    def geradorDeCodigosRecursivo(no,codigo):
        if no is None:
            return
        if no.caractere is not None:
            tabelaCodigos[no.caractere] = codigo
        geradorDeCodigosRecursivo(no.filhoEsquerda,codigo + '0')
        geradorDeCodigosRecursivo(no.filhoDireita,codigo + '1')
    geradorDeCodigosRecursivo(raiz,"")
    return tabelaCodigos

def codificar(string,tabelaCodigos):
    return "".join(tabelaCodigos[caractere] for caractere in string)

def decodificar_texto(codigo,raiz):
    texto_decodificado = []
    no = raiz

    for elemento in codigo:
        if elemento == '0':
            no = no.filhoEsquerda
        else:
            no = no.filhoDireita
        
        if no.caractere is not None:
            texto_decodificado.append(no.caractere)
            no = raiz
    return "".join(texto_decodificado)
def Compactador(string):


    frequencia = calcularFrequencia(string)
    arvoreHuffman = construirArvore(frequencia)
    tabela_codigos = geradorDeCodigos(arvoreHuffman)
    stringCompactada = codificar(string,tabela_codigos)
    return stringCompactada,arvoreHuffman

def ascii_para_binario(texto):
    return ' '.join(format(ord(c), '08b') for c in texto)


texto = "exemplo de texto para compressao"
texto_codificado, raiz = Compactador(texto)
texto_binario = ascii_para_binario(texto)
print("Texto Codificado:", texto_codificado)

texto_decodificado = decodificar_texto(texto_codificado, raiz)
print("Texto Decodificado:", texto_decodificado)

print("Taxa de compressão: ", (len(texto_codificado)/len(texto_binario))*100,"%")
