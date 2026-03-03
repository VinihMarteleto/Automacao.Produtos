import pyautogui
import time

pyautogui.PAUSE = 1 # Define o link do site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # Substitua pelo link do site que deseja acessar
# Abre o navegador Edge
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter')
# Espera a página carregar
time.sleep(1) # Aguarda 2 segundos para garantir que a página tenha carregado
# Clica no campo de email
pyautogui.click(x=1461, y=380) # Substitua as coordenadas pelo local do campo de email
pyautogui.write('vinihmarteleto@gmail.com') 
# Clica no campo de senha
pyautogui.press("tab") # Substitua as coordenadas pelo local do campo de senha
pyautogui.write('123456')
# Clica no botão de login
pyautogui.press("tab") # Substitua as coordenadas pelo local do botão de login
pyautogui.press("enter")
time.sleep(1) # Aguarda 2 segundos para garantir que o campo de senha esteja visível # Aguarda 2 segundos para garantir que o campo de senha esteja visível
# abrir a basse de dados
import pandas
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
#cadastrar um novo produto
    pyautogui.click(x=1197, y=261) # Substitua as coordenadas pelo local do campo de email
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") 

    #marca 
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    #categorria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    

    #preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
   
    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)  
    pyautogui.press("tab")
    
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000) # Rola a página para cima após cada cadastro
    