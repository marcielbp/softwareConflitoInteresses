# softwareConflitoInteresses
Este software verifica conflito de interesses entre pesquisadores utilizando a plataforma Lattes. O software pode ser utilizado para composição de banca de concurso público ou verificaço manual de rede de colaboradores em trabalhos acadêmicos.

## Utilização
No arquivo [app.py](https://github.com/marcielbp/softwareConflitoInteresses/blob/master/app.py) o valor *ANO_INICIO* determina o primeiro ano da busca por conflito de interesses. Mude esse valor para o período desejado.

É necessário fazer o download de todos os currículos [Lattes](http://lattes.cnpq.br/) em formato *XML*. O script de terminal Linux [unzipCVLattes](https://github.com/marcielbp/softwareConflitoInteresses/blob/master/unzipCVLattes.sh) automatiza o processo de extração dos arquivos XML em pastas, uma a uma.

Modifique o arquivo [candidatos.txt](https://github.com/marcielbp/softwareConflitoInteresses/blob/master/candidatos.txt) com os nomes dos candidatos os quais se deseja verificar se possuem trabalhos publicados com os membros da banca. Os curriculos Lattes dos membros da banca devem ter sido previamente extraídos nas pastas usando o script [unzipCVLattes](https://github.com/marcielbp/softwareConflitoInteresses/blob/master/unzipCVLattes.sh) a fim de se verificar o conflito.

O exemplo de como ficará a estrutura do folder as baixar os curriculos em *XML* e os [extrair](https://github.com/marcielbp/softwareConflitoInteresses/blob/master/unzipCVLattes.sh) é mostrada [neste link](https://github.com/marcielbp/softwareConflitoInteresses/blob/master/image.png).

Ao executar o arquivo [testSimilarity.sh](https://github.com/marcielbp/softwareConflitoInteresses/blob/master/testSimilarity.sh), a saída em console irá verificar para cada candidato, um a um, se há trabalhos com co-autoria ou existe orientação com os pesquisadores cujos curriculos foram baixados. Caso haja alguma similaridade, o *software* exibe a semelhança em console e dá uma nota de similaridade, a fim do usuário decidir se há conflito ou não.
