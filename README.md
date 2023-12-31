# POO - Programação orientada a objetos
## Mapa Mental
   ![plot](./imgs/Mind%20Map.jpg)

## Introdução - UML
   Unified Modeling Language é uma linguagem de notação destinada à modelação e documentação das fases de desenvolvimento de softwares orientados a objetos
   ![plot](./imgs/UML%20Diagram.jpg)
## Relações - UML
   * **Associação**: Um relacionamento entre dois elementos que mostra que os objetos de um clasificador (Classe, Interface ou Nó) conectam-se e podem navegar em objetos de um outro classificador. Conecta dois classificadores, o principal(Fornecedor) e o secundário (cliente)
   * **Herança**: É uma hierarquia de abstrações na qual uma subclasse herda a estrutura de uma ou mais superclasses
   * **Realização/Implementação**: É uma relacionamento que existe entre dois elementos e se dá quando um deles deve realizar, ou implementar, o comportamento que o outro especifica. O modelo que especifica é o fornecedor e o elemento que implementa é o cliente
   * **Dependência**: Indica que as alteraçõess em um elemento do modelo (fornecedor/independente) podem causar alterações em um outro modelo (cliente/dependente). Obs: O fornecedor não é afetado com mudanças no cliente
   * **Agregação**: Descreve um classificador como uma parte de, ou como um subordinado a outro classificador
   * **Composição**: É um tipo de agregação onde o classificador da parte é dependente da existência do classicador todo
![plot](./imgs/Relações.jpg)
## Exemplo de Projeto- UML
   Outros diagramas UML úteis:
   * **Estruturais**\
     Classes\
     Objetos\
     Componentes\
     Implantação
   * **Comportamentais**\
     Sequência\
     Atividades\
     Máquina de Estados\
![plot](./imgs/Exemplo.jpg)
## Linguagem Interpretada x Compilada
   * Meados de 1940: surgimento da linguagem de máquina
      * 0100 0011 1010 1111 0000 1010 0001 0011
   * Meados de 1948: surgimento da linguagem de montagem
     * ADD AX, BX
   * Linguagem de alto nível:
      * FORTRAN (1967): compilada
      * LISP (1958): interpretada
      * Simula-67, Smaltalk-80: orientação a objetos
      * C, C++, Objective-C
![plot](./imgs/CompInter.jpg)
### Linguagem Interpretada
Os interpretadores fazem a leitura de linha por linha, executando uma por uma. Ou seja, o código fonte é convertido diretamente para a linguagem de máquina no interpretador.\
![plot](./imgs/Inter.jfif)\
### Linguagem Compilada
Os compiladores são responsáveis por transformar os códigos fontes em códigos objetos, em linguagem de máquina. Para isso, eles convertem primeiro para a linguagem de montagem (Assembly) para depois transformar em linguagem de máquina.\
![plot](./imgs/Comp.png)
### Linguagem Híbrida
Java nasceu em 1995 com a ideia de possibilitar com que os códigos fossem executados por quaisquer sistemas operacionais por meio da compilação e da interpretação\
![plot](./imgs/Hibrida.gif)

## Referências
    - TecnoBlog: https://tecnoblog.net/responde/o-que-e-uml/
    - Coursera: "Laboratório de Programação Orientada a Objetos - Parte 1 (USP)"
    - IBM: https://www.ibm.com/docs/pt-br/rsas/7.5.0?topic=SS4JE2_7.5.5/com.ibm.xtools.modeler.doc/topics/rreltyp.htm
