<p align="center">
<img align="center" src="https://miro.medium.com/max/2625/1*Dd0-ftvJxAcSdSZHgNrz0w.png" width=200 height=105>
<h1 align="center">OCR Python</h1>
  <br>
  <p align="center">Programa de Optical Character Recognition (OCR) para reconhecer e extrair textos em imagens e fotos.
  <br>
  Acesse o programa: https://share.streamlit.io/guilhermedonizetti/ocr_python/main.py
 </p>
 </p>
 <br>
 <b>Objetivo: </b>O programa visa receber uma imagem como entrada, reconhecer os caracteres contidos nela e extrair esses caracteres. Uma vez que o texto foi extraído, o programa aponta quantos por cento de palavras, boas ou más, existem no texto da imagem com base num pequeno conjunto de palavras pré-registradas. Por fim, o programa busca encontrar CPF e datas.
 <br><br>
 <b>Ferramentas:</b><br>
 :heavy_check_mark: Pytesseract - biblioteca Python para aplicação OCR, documentação (https://pypi.org/project/pytesseract/).<br>
 :heavy_check_mark: Streamlit - framework Python para construção da página web, documentação (https://docs.streamlit.io/en/stable/).<br>
 <br>
 <b>Funcionamento: </b> O programa vai acessar as imagens em seu dispositivo, deve-se observar alguns pontos:<br>
 :point_right: O programa interpreta textos em Português :brazil: ou idiomas com alfabeto similar (ex.: :us:).<br>
 :point_right: O resultado depende da qualidade da imagem.<br>
 :point_right: É mais assertivo a imagem estar na rotação cujo o texto fique vertical
 <br><br>
 Quando os caracteres forem reconhecidos, eles serão exibidos logo abaixo da imagem e ao lado esquerdo da página surge a opção de <code>Analisar texto</code>. Se essa opção for selecionada o programa vai buscar:<br><br>
 :green_circle: <b>CPF: </b> o padrão de CPF para ser encontrado é exatamente xxx.xxx.xxx-xx (incluindo pontos e traço).<br>
 :green_circle: <b>Data: </b> o padrão de data para ser encontrado é exatamente xx/xx/xxxx (07/09/2020 sim, 07 de Setembro de 2020 não).<br>
 :green_circle: <b>Palavras boas e más: </b> as palavras encontradas na imagem serão verificadas se estão no conjunto de palavras boas e más. O percentual que será exibido no resultado ignora o fato de que as palavras sejam repetidas.
 
 <br><br>
 Para mais informações sobre o código: https://guilhermedonizettiads.medium.com/ocr-com-pytesseract-e-streamlit-15663ab85925
 
 
 <br><br>
 
 <p align="center">
 Streamlit, Tesseract, Python, Optical Character Recognition (OCR).
 </p>
