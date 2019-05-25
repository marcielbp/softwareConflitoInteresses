__author__ = 'andremeireles'

import xml.etree.ElementTree as ET
import sys
from similarity import similar


ACCEPTABLE_SIMILARITY_LEVEL = 0.7
ANO_INICIO = 2012


def print_attr(element, attr, repeat_author=False):
    if attr in element.attrib:
        if len(element.attrib[attr]) > 0 :
            # print '     NOME-DO-ORIENTADOR-SANDUICHE: ', element.attrib['NOME-DO-ORIENTADOR-SANDUICHE']
            valor_attr = element.attrib[attr]
            if repeat_author or nome_candidato != valor_attr:
                for prof in banca:
                    sim_level = similar(prof.upper(), valor_attr.upper())
                    if sim_level > ACCEPTABLE_SIMILARITY_LEVEL:
                        print '-', valor_attr, ' => ', '{:.2f}'.format(sim_level) , '<= ', prof

banca_file = open(sys.argv[2])
banca = banca_file.read().splitlines()

# tree = ET.parse('marciel-barros.xml')
#tree = ET.parse('maria-elias.xml')
#print sys.argv[1]
tree = ET.parse(sys.argv[1])
#tree = ET.parse(arg)
#tree = ET.parse('Todos_XML/0603306945433479.zip.xml')

root = tree.getroot()

for child in root:
    # print ' ', child.tag
    if child.tag == 'DADOS-GERAIS':
        nome_candidato = child.attrib['NOME-COMPLETO']
        print 'CANDIDATO: ' + nome_candidato
        for dado_geral in child:
            # print '  ', dado_geral.tag
            if dado_geral.tag == 'FORMACAO-ACADEMICA-TITULACAO':
                # print '  ', dado_geral.tag
                for titulo in dado_geral:
                    # print '   ', titulo.tag
                    print_attr(titulo, 'NOME-DO-ORIENTADOR')

                    print_attr(titulo, 'NOME-ORIENTADOR-GRAD')

                    print_attr(titulo, 'NOME-COMPLETO-DO-ORIENTADOR')

                    print_attr(titulo, 'NOME-DO-CO-ORIENTADOR')

                    print_attr(titulo, 'NOME-ORIENTADOR-DOUT')

                    print_attr(titulo, 'NOME-DO-ORIENTADOR-CO-TUTELA')

                    print_attr(titulo, 'NOME-DO-ORIENTADOR-SANDUICHE')

    if child.tag == 'PRODUCAO-BIBLIOGRAFICA':
        for prod_bib in child:

            if prod_bib.tag == 'TRABALHOS-EM-EVENTOS' or prod_bib.tag == 'ARTIGOS-PUBLICADOS':
                for trab_evento in prod_bib:
                    for dados_trab in trab_evento:
                        if dados_trab.tag == 'DADOS-BASICOS-DO-TRABALHO':
                            if dados_trab.attrib['ANO-DO-TRABALHO'] <= ANO_INICIO:
                                break
                        if dados_trab.tag == 'DADOS-BASICOS-DO-ARTIGO':
                            if dados_trab.attrib['ANO-DO-ARTIGO'] <= ANO_INICIO:
                                break
                        if dados_trab.tag == 'AUTORES':
                            print_attr(dados_trab, 'NOME-COMPLETO-DO-AUTOR')

            if prod_bib.tag == 'LIVROS-E-CAPITULOS':
                for livros_cap in prod_bib:
                    if livros_cap.tag == 'LIVROS-PUBLICADOS-OU-ORGANIZADOS':
                        for livro in livros_cap:
                            for dados_livro in livro:
                                if dados_livro.tag == 'DADOS-BASICOS-DO-LIVRO':
                                    if dados_livro.attrib['ANO'] <= ANO_INICIO:
                                        break

                                if dados_livro.tag == 'AUTORES':
                                    print_attr(dados_livro, 'NOME-COMPLETO-DO-AUTOR')

                    if livros_cap.tag == 'CAPITULOS-DE-LIVROS-PUBLICADOS':
                        for capitulo in livros_cap:
                            for dados_capitulo in capitulo:
                                if dados_capitulo.tag == 'DADOS-BASICOS-DO-CAPITULO':
                                    if dados_capitulo.attrib['ANO'] <= ANO_INICIO:
                                        break
                                if dados_capitulo.tag == 'AUTORES':
                                    print_attr(dados_capitulo, 'NOME-COMPLETO-DO-AUTOR')

    if child.tag == 'PRODUCAO-TECNICA':
        for trab_tecnico in child:
            for dados_trab_tecnico in trab_tecnico:
                if dados_trab_tecnico.tag == 'DADOS-BASICOS-DO-TRABALHO-TECNICO':
                    if dados_trab_tecnico.attrib['ANO'] <= ANO_INICIO:
                        break

                if dados_trab_tecnico.tag == 'AUTORES':
                    print_attr(dados_trab_tecnico, 'NOME-COMPLETO-DO-AUTOR')
