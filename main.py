import random

def número(a,b):
    carta = random.randint(a, b)
    print(f"Você tirou a carta {carta}")
    return carta

def pegarCarta():
    print("Você gostaria de pegar uma carta?")
    resposta = input().lower()
    if resposta.startswith("s"):
        return True
    else:
        return False
      
def jogo(User1, User2):
    User1Points = 0
    User2Points = 0
    
    def placar():
        print(f"\n{User1}: {User1Points} | {User2}: {User2Points}\n")
        
    while User1Points <= 21 and User2Points <= 21:
        placar()
        print(f"Vez de {User1}")
        
        if pegarCarta():
            User1Points += número(1, 13)
        else:
            placar()
            print(f"Vez de {User2}")
            
            if pegarCarta():
                User2Points += número(1,13)
            break
        
        placar()
        print(f"Vez de {User2}")
        
        if pegarCarta():
            User2Points += número(1, 13)
        else:
            break
        
    placar()
    
    if User1Points > 21 and User2Points > 21:
        print("Empate")
        return
    
    if User1Points > 21:
        print(f"{User2} ganhou")
        return
    elif User2Points > 21:
        print(f"{User1} ganhou")
        return
            
    if User1Points > User2Points:
        print(f"{User1} ganhou") 
    elif User2Points > User1Points:
        print(f"{User2} ganhou")
    else:
        print("Empate")
        
print("Digite o nome do Jogador 1")
print(">" ,end="")
User1 = input().capitalize()
print("Digite o nome do Jogador 2")
print(">" ,end="")
User2 = input().capitalize()

jogo(User1, User2)
