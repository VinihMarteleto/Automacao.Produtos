# Automacao.Produtos

Projeto de automação para cadastro de produtos em um sistema web, implementado
com Python usando `pyautogui` para interação com a interface e `pandas` para
leitura da base de produtos (`produtos.csv`).

Conteúdo do repositório:

- `codigo.py` — script principal de automação (abre navegador, faz login e
	cadastra produtos a partir de `produtos.csv`).
- `auxiliar.py` — utilitário para identificar coordenadas do mouse e exemplo
	do formato da tabela.
- `produtos.csv` — base de dados de exemplo com colunas usadas pelo script.
- `RELEASE_NOTES.md` — notas da release v1.0.0.
- `LICENSE` — licença MIT.

Instalação e dependências

1. Instale Python 3.x.
2. Instale dependências:

```powershell
pip install pyautogui pandas
```

Uso

1. Ajuste as coordenadas em `codigo.py` conforme a sua resolução e posição dos
	 elementos na tela (use `auxiliar.py` para obter coordenadas com `pyautogui`).
2. Configure o navegador para que o campo de endereço receba o link ao abrir o
	 navegador (o script abre o Edge por atalho de teclado).
3. Execute:

```powershell
python codigo.py
```

O que foi feito neste repositório

- Inicializado repositório Git local e criado commit inicial com os arquivos do
	projeto.
- Adicionados e comitados `README.md` e `.gitignore`.
- Criado repositório remoto no GitHub: https://github.com/VinihMarteleto/Automacao.Produtos
- Push do branch `main` para o remoto.
- Adicionado e comitado `LICENSE` (MIT).
- Criada release `v1.0.0` com notas contidas em `RELEASE_NOTES.md`:
	https://github.com/VinihMarteleto/Automacao.Produtos/releases/tag/v1.0.0
- Criada e enviada a tag anotada `v1.0.0-signed` (tentativa de assinar localmente
	falhou por ausência de chave privada; a tag enviada é anotada).

Links úteis

- Repositório: https://github.com/VinihMarteleto/Automacao.Produtos
- Release v1.0.0: https://github.com/VinihMarteleto/Automacao.Produtos/releases/tag/v1.0.0
- Tag: https://github.com/VinihMarteleto/Automacao.Produtos/tree/v1.0.0-signed

Boas práticas e recomendações

- Nunca deixe credenciais em texto plano no código; utilize variáveis de
	ambiente ou um cofre de segredos.
- Preferir localizar elementos por seletores (Selenium, Playwright) em vez de
	coordenadas fixas quando possível — isso torna a automação mais robusta.
- Teste em uma janela/navegador com posição e escala de interface constantes.

Contribuição

Pull requests são bem-vindos. Abra um issue antes de implementar mudanças grandes
ou se quiser suporte para execução não interativa.

Licença

Este projeto está licenciado sob a licença MIT — ver arquivo `LICENSE`.
