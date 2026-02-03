#iniciar servidor(localhost) pelo cmd da pasta
#uvicorn main:app --reload (127.0.0.1:8000)


"""
Os códigos de status de resposta HTTP indicam se uma solicitação HTTP específica foi concluída com sucesso. As respostas são agrupadas em cinco classes:

Respostas informativas ( 100 - 199)
Respostas bem-sucedidas ( 200 - 299)
Mensagens de redirecionamento ( 300 - 399)
Respostas de erro do cliente ( 400 - 499)
Respostas de erro do servidor ( 500 - 599)

document
https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
"""


"""
404 error

O servidor não consegue encontrar o recurso solicitado. No navegador, 
isso significa que a URL não é reconhecida. Em uma API, isso também pode significar que o 
endpoint é válido, mas o recurso em si não existe.
"""