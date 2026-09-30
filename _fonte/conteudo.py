# Conteúdo do site catarinaleitao.net
# Um projecto por entrada, pela ordem da grelha.
# Imagens: "wp/..." = pasta uploads do WordPress; "dr/..." = pastas do Drive; "ex/..." = enviadas à parte.
# Cada imagem: (origem, legenda PT, legenda EN, fotografia ou None)
# "rever": campos traduzidos ou escritos de novo, a confirmar antes de publicar.

VISTA_CCC_PT = "Vista da exposição <cite>ECO·NOMIA: As Regras da Casa</cite>, Centro Cultural de Cascais, 2026."
VISTA_CCC_EN = "Installation view, <cite>ECO·NOMIA: As Regras da Casa</cite>, Centro Cultural de Cascais, 2026."
DENDRO_2026_PT = "<cite>Dendrograma | Tree-kit</cite>, 2016–26, madeira, alumínio, tinta vinílica, velcro, dimensões variáveis. Vista da exposição <cite>ECO·NOMIA</cite>, Centro Cultural de Cascais, 2026."
DENDRO_2026_EN = "<cite>Dendrogram | Tree-kit</cite>, 2016–26, wood, aluminum, vinyl paint, velcro, variable dimensions. Installation view, <cite>ECO·NOMIA</cite>, Centro Cultural de Cascais, 2026."
JL = "Júlia Lomba"

def nf(letra, mat_pt, mat_en, dim_pt, dim_en, extra_pt="", extra_en=""):
    return (f"<cite>Naturfatura {letra}</cite>, 2023, {mat_pt}, {dim_pt}{extra_pt}.",
            f"<cite>Naturfatura {letra}</cite>, 2023, {mat_en}, {dim_en}{extra_en}.")

NF = {
 "A": nf("A","madeira, vinil, MDF e aerosol","wood, vinyl, MDF and spray paint","190x52x23,5 cm","190x52x23.5 cm"),
 "B": nf("B","madeira, vinil, feltro, tecido, plástico, cimento, tinta acrílica e aerosol","wood, vinyl, felt, fabric, plastic, cement, acrylic paint and spray paint","232x70x30 cm","232x70x30 cm"),
 "D": nf("D","madeira, vinil, tecido, plástico, cimento, tinta acrílica e aerosol","wood, vinyl, fabric, plastic, cement, acrylic paint and spray paint","224x70x38 cm","224x70x38 cm"),
 "E": nf("E","madeira, tinta acrílica e aerosol","wood, acrylic paint and spray paint","160x112x25 cm","160x112x25 cm"),
 "F": nf("F","madeira, vinil, plástico, cimento, tinta acrílica e aerosol","wood, vinyl, plastic, cement, acrylic paint and spray paint","210x65x65 cm","210x65x65 cm"),
 "H": nf("H","madeira, vinil, MDF, tecido, plástico, cimento, tinta acrílica e aerosol","wood, vinyl, MDF, fabric, plastic, cement, acrylic paint and spray paint","200x40x82 cm","200x40x82 cm"),
 "I": nf("I","madeira, MDF, feltro, tecido, plástico, cimento, tinta acrílica e aerosol","wood, MDF, felt, fabric, plastic, cement, acrylic paint and spray paint","180x130x40 cm","180x130x40 cm"),
 "J": nf("J","madeira e aerosol","wood and spray paint","62x43x32 cm","62x43x32 cm"),
 "L": nf("L","vinil, plástico, MDF e aerosol","vinyl, plastic, MDF and spray paint","145x23x10 cm","145x23x10 cm"),
 "M": nf("M","madeira, tecido, vinil, MDF, feltro, plástico, tinta acrílica e aerosol","wood, fabric, vinyl, MDF, felt, plastic, acrylic paint and spray paint","dimensões variáveis","variable dimensions"),
}
def ap(n, dim_pt, dim_en, extra_pt="", extra_en=""):
    return (f"<cite>Apontamentos Naturfatura #{n}</cite>, 2023, aguarela, acrílico e corte sobre papel, {dim_pt}{extra_pt}.",
            f"<cite>Apontamentos Naturfatura #{n}</cite>, 2023, watercolor, acrylic and cutouts on paper, {dim_en}{extra_en}.")
VISTA_NF_PT = "Vista da exposição <cite>Naturfatura</cite>, Carlos Carvalho Arte Contemporânea, Lisboa, 2023."
VISTA_NF_EN = "Installation view, <cite>Naturfatura</cite>, Carlos Carvalho Arte Contemporânea, Lisbon, 2023."

def thicket(n, ano, dim):
    return (f"<cite>Thicket #{n}</cite>, {ano}, tinta sobre papel, {dim.replace('.',',')}.",
            f"<cite>Thicket #{n}</cite>, {ano}, ink on paper, {dim}.")

def ns(t, ano, dim, foto=None):
    return (f"<cite>{t}</cite>, {ano}, aguarela sobre papel, {dim.replace('.',',')}.",
            f"<cite>{t}</cite>, {ano}, watercolor on paper, {dim}.")

def sn(t, mat_pt, mat_en, dim):
    return (f"<cite>{t}</cite>, 2011, {mat_pt}, {dim}.", f"<cite>{t}</cite>, 2011, {mat_en}, {dim}.")
AG = ("aguarela sobre papel", "watercolor on paper")
AGS = ("aguarela e tinta sumi sobre papel", "watercolor and sumi ink on paper")

def ss(n, det=False):
    d_pt = ", pormenor" if det else ""
    d_en = ", detail" if det else ""
    return (f"<cite>Survival Systems – Urban Action Catalog 2003–2004</cite>, página {n}{d_pt}.",
            f"<cite>Survival Systems – Urban Action Catalog 2003–2004</cite>, page {n}{d_en}.")

PROJECTOS = [

# ------------------------------------------------------------------
dict(
 slug="eco-nomia", ano="2026",
 titulo=dict(pt="ECO·NOMIA: As Regras da Casa", en="ECO·NOMIA: As Regras da Casa"),
 grelha=dict(pt="ECO·NOMIA", en="ECO·NOMIA"),
 onde=dict(pt="Centro Cultural de Cascais, Fundação D. Luís I, 2026",
           en="Centro Cultural de Cascais, Fundação D. Luís I, 2026"),
 texto=dict(
  pt=["Desenhos da série <cite>Morfometrias</cite>, esculturas <cite>Naturfatura</cite>, três impressões de grande formato e o <cite>Dendrograma</cite>, numa nova configuração, partilharam o piso 0 da Fundação D. Luís I numa lógica de consociação: formas e matérias distintas a coabitar a mesma casa.",
      "O catálogo digital, com textos de Salvato Teles de Menezes e Inês Ferreira-Norman e o registo fotográfico das obras, pode ser consultado <a href=\"https://online.fliphtml5.com/kyoil/thek/#p=1\">aqui</a>."],
  en=["Drawings from the <cite>Morfometrias</cite> series, <cite>Naturfatura</cite> sculptures, three large-format prints and the <cite>Dendrogram</cite>, in a new configuration, shared the ground floor of the Fundação D. Luís I on the principle of consociation: distinct forms and materials cohabiting the same house.",
      "The digital catalogue, with texts by Salvato Teles de Menezes and Inês Ferreira-Norman and photographs of the works, can be viewed <a href=\"https://online.fliphtml5.com/kyoil/thek/#p=1\">here</a>."]),
 imagens=[
  ("dr/CatarinaLeitao-Eco-nomia-CCC-01.jpg", VISTA_CCC_PT, VISTA_CCC_EN, JL),
  ("dr/CatarinaLeitao-Eco-nomia-CCC-05.jpg", VISTA_CCC_PT, VISTA_CCC_EN, JL),
  ("dr/CatarinaLeitao-Eco-nomia-CCC-02.jpg", VISTA_CCC_PT, VISTA_CCC_EN, JL),
  ("dr/CatarinaLeitao-Eco-nomia-CCC-04.jpg", VISTA_CCC_PT, VISTA_CCC_EN, JL),
  ("dr/CatarinaLeitao-Eco-nomia-CCC-03.jpg", "Pormenor.", "Detail.", JL),
  ("dr/CatarinaLeitao-Eco-nomia-CCC-03-a.jpg", VISTA_CCC_PT, VISTA_CCC_EN, JL),
  ("dr/CatarinaLeitao-Eco-nomia-CCC-06.jpg", VISTA_CCC_PT, VISTA_CCC_EN, JL),
  ("dr/CatarinaLeitao-Eco-nomia-CCC-07.jpg", VISTA_CCC_PT, VISTA_CCC_EN, JL),
  ("dr/CatarinaLeitao-Eco-nomia-CCC-08.jpg", VISTA_CCC_PT, VISTA_CCC_EN, JL),
  ("dr/CatarinaLeitao-Eco-nomia-CCC-09.jpg", DENDRO_2026_PT, DENDRO_2026_EN, JL),
  ("dr/CatarinaLeitao-Eco-nomia-CCC-10.jpg", "<cite>Dendrograma | Tree-kit</cite>, pormenor.", "<cite>Dendrogram | Tree-kit</cite>, detail.", JL),
  ("dr/CatarinaLeitao-catalogo.png", "Capa do catálogo digital.", "Cover of the digital catalogue.", None),
 ],
 rever=["texto EN", "crédito Júlia Lomba em todas as fotografias", "legendas das peças de chão (só 'vista da exposição')"],
),

# ------------------------------------------------------------------
dict(
 slug="jardim-portatil", ano="2026",
 titulo=dict(pt="Jardim Portátil NF.3.0", en="Jardim Portátil NF.3.0"),
 onde=dict(pt="Espaço Cubo, Galeria Fernando Santos, Porto, 21.03–30.05.2026",
           en="Espaço Cubo, Galeria Fernando Santos, Porto, 21.03–30.05.2026"),
 texto=dict(
  pt=["<cite>Jardim Portátil NF.3.0</cite> ocupou o Espaço Cubo da Galeria Fernando Santos, no Porto, entre 21 de Março e 30 de Maio de 2026. Com a instalação foram mostradas três esculturas de parede da série <cite>Naturfatura 04</cite>."],
  en=["<cite>Jardim Portátil NF.3.0</cite> (Portable Garden NF.3.0) occupied the Espaço Cubo at Galeria Fernando Santos, Porto, from 21 March to 30 May 2026. Three wall sculptures from the <cite>Naturfatura 04</cite> series were shown alongside the installation."]),
 imagens=[
  ("dr/Leitao-Cat-JardimPortatil-Hi.jpg",
   "<cite>Jardim Portátil NF.3.0</cite>, 2026, madeira, vinil, tecido, alcatifa industrial, cimento, tinta vinílica, dimensões variáveis.",
   "<cite>Jardim Portátil NF.3.0</cite>, 2026, wood, vinyl, fabric, industrial carpet, cement, vinyl paint, variable dimensions.", None),
  ("wp/2026/03/PX6zxsdg.jpg", "Cartaz da exposição.", "Exhibition poster.", None),
 ],
 rever=["texto PT e EN (escrito de novo, só factual)", "tradução do título entre parênteses no EN"],
),

# ------------------------------------------------------------------
dict(
 slug="naturfatura-3-0", ano="2026",
 titulo=dict(pt="Naturfatura 3.0", en="Naturfatura 3.0"),
 onde=dict(pt="Mupi Gallery, Maus Hábitos, Porto, 2026. Ciclo <cite>Nas Margens</cite>, curadoria de João Baeta",
           en="Mupi Gallery, Maus Hábitos, Porto, 2026. <cite>Nas Margens</cite> series, curated by João Baeta"),
 texto=dict(
  pt=["Três impressões de grande formato da série <cite>Naturfatura 3.0</cite>, mostradas nas caixas de luz da Mupi Gallery, no Maus Hábitos."],
  en=["Three large-format prints from the <cite>Naturfatura 3.0</cite> series, shown in the lightboxes of the Mupi Gallery at Maus Hábitos, Porto."]),
 imagens=[
  ("wp/2026/01/Naturfatura3-Mupi-web.jpg",
   "<cite>Naturfatura 3.0 #1–#3</cite>, 2025, impressão a jacto de tinta sobre backlite, 175x120 cm (cada). Vista na Mupi Gallery, Maus Hábitos, Porto, 2026.",
   "<cite>Naturfatura 3.0 #1–#3</cite>, 2025, inkjet print on backlit film, 175x120 cm (each). Installation view, Mupi Gallery, Maus Hábitos, Porto, 2026.", None),
  ("wp/2026/01/Mupi-poster-XL.jpg", "Cartaz da exposição.", "Exhibition poster.", None),
 ],
 rever=["texto PT e EN (escrito de novo, só factual)", "imagens em baixa resolução (1080 px): há melhores?"],
),

# ------------------------------------------------------------------
dict(
 slug="naturfatura", ano="2023",
 titulo=dict(pt="Naturfatura", en="Naturfatura"),
 onde=dict(pt="Carlos Carvalho Arte Contemporânea, Lisboa, 15.04–01.07.2023. Curadoria de João Silvério",
           en="Carlos Carvalho Arte Contemporânea, Lisbon, 15.04–01.07.2023. Curated by João Silvério"),
 texto=dict(
  pt=["<cite>Naturfatura</cite> é uma exposição composta por uma série de trabalhos escultóricos e um conjunto de desenhos de grande formato. As obras de <cite>Naturfatura</cite> inserem-se numa prática através da qual tenho vindo a propor a ideia de uma continuidade absoluta e não-hierárquica entre os conceitos de humano, natureza, artifício e cultura.",
      "Em <cite>Naturfatura</cite>, os desenhos representam anotações possíveis e constituem-se como fabulações sobre uma ideia de observação científica nas quais fundo formas, noções e sensações dos universos do orgânico, do manufacturado, da geologia e da botânica. Por sua vez, as esculturas dão continuidade à exploração destes elementos, expandindo os desenhos em construções híbridas que materializam misturas e estabelecem um diálogo com a corporalidade do espaço."],
  en=["<cite>Naturfatura</cite> brings together a series of sculptural works and a group of large-format drawings. They belong to a practice through which I have been proposing an absolute, non-hierarchical continuity between the concepts of the human, nature, artifice and culture.",
      "In <cite>Naturfatura</cite>, the drawings stand as possible annotations: fabulations on an idea of scientific observation in which I fuse forms, notions and sensations from the worlds of the organic, the manufactured, geology and botany. The sculptures carry this exploration further, expanding the drawings into hybrid constructions that give material form to these mixtures and enter into dialogue with the physical presence of the space."]),
 imagens=[
  ("wp/2023/10/2023-Naturfatura-vistas-8-1.jpg", VISTA_NF_PT, VISTA_NF_EN, None),
  ("wp/2023/10/Naturfatura-B-03.jpg", *NF["B"], None),
  ("wp/2023/10/2023-Naturfatura-vistas-14.jpg", VISTA_NF_PT, VISTA_NF_EN, None),
  ("wp/2023/10/2023-Naturfatura-vistas-18.jpg", VISTA_NF_PT, VISTA_NF_EN, None),
  ("wp/2023/10/Naturfatura-A-01.jpg", *NF["A"], None),
  ("wp/2023/10/Naturfatura-B-01.jpg", *NF["B"], None),
  ("wp/2023/10/Naturfatura-D-01.jpg", *NF["D"], None),
  ("wp/2023/10/Naturfatura-H-01.jpg", *NF["H"], None),
  ("wp/2023/10/Naturfatura-F-004.jpg", *NF["F"], None),
  ("wp/2023/10/Naturfatura-F-005.jpg", *NF["F"], None),
  ("wp/2023/10/Naturfatura-I-01.jpg", *NF["I"], None),
  ("wp/2023/10/Naturfatura-E-02.jpg", *NF["E"], None),
  ("wp/2023/10/Naturfatura-J-01.jpg", *NF["J"], None),
  ("wp/2023/10/Naturfatura-L-01.jpg", *NF["L"], None),
  ("wp/2023/10/Naturfatura-M-03.jpg", *NF["M"], None),
  ("wp/2023/10/Naturfatura-M-05.jpg", *NF["M"], None),
  ("wp/2023/10/Naturfatura-M-15.jpg", *NF["M"], None),
  ("wp/2023/10/Naturfatura-L-03.jpg", *NF["L"], None),
  ("wp/2023/10/Apontamentos-Naturfatura-05.jpg", *ap("05","110x151 cm","110x151 cm"), None),
  ("wp/2023/10/Apontamentos-Naturfatura-06.jpg", *ap("06","110x152,5 cm","110x152.5 cm"), None),
  ("wp/2023/10/Apontamentos-Naturfatura-02-vista1.jpg", *ap("02","110,5x151 cm","110.5x151 cm"), None),
 ],
 rever=["texto EN", "legendas atribuídas pela letra no nome do ficheiro", "créditos fotográficos"],
),

# ------------------------------------------------------------------
dict(
 slug="as-possibilidades-de-uma-paisagem", ano="2020–21",
 titulo=dict(pt="As possibilidades de uma paisagem", en="As possibilidades de uma paisagem"),
 onde=dict(pt="Galeria do Parque, Vila Nova da Barquinha, 06.11.2020–30.01.2021. Curadoria de João Pinharanda",
           en="Galeria do Parque, Vila Nova da Barquinha, 06.11.2020–30.01.2021. Curated by João Pinharanda"),
 texto=dict(
  pt=["Exposição individual na Galeria do Parque, em Vila Nova da Barquinha, com curadoria de João Pinharanda. O catálogo, com texto do curador, pode ser descarregado <a href=\"{raiz}docs/as-possibilidades-de-uma-paisagem-catalogo.pdf\">aqui</a> (PDF, 1,8 MB)."],
  en=["Solo exhibition (<cite>The Possibilities of a Landscape</cite>) at Galeria do Parque, Vila Nova da Barquinha, curated by João Pinharanda. The catalogue, with a text by the curator, can be downloaded <a href=\"{raiz}docs/as-possibilidades-de-uma-paisagem-catalogo.pdf\">here</a> (PDF, 1.8 MB)."]),
 docs=[("wp/2020/11/Leitao_catalogo.pdf", "docs/as-possibilidades-de-uma-paisagem-catalogo.pdf")],
 imagens=[(f"wp/{p}", "Vista da exposição <cite>As possibilidades de uma paisagem</cite>, Galeria do Parque, Vila Nova da Barquinha, 2020.",
           "Installation view, <cite>As possibilidades de uma paisagem</cite>, Galeria do Parque, Vila Nova da Barquinha, 2020.", None)
          for p in ["2021/10/2020-barquinha-vista2.jpg","2020/12/Leita-vnbarquinha.jpg","2021/10/2020-barquinha-vista6.jpg",
                    "2021/10/2020-barquinha-vista7.jpg","2021/10/2020-barquinha-vista5.jpg","2021/10/2020-barquinha-vista4.jpg"]],
 rever=["texto PT e EN (escrito de novo, só factual)", "confirmar que o catálogo tem texto de João Pinharanda (a CV diz 'texto de João Pinharanda')", "legendas das obras (só 'vista da exposição')"],
),

# ------------------------------------------------------------------
dict(
 slug="orografias", ano="2018–19",
 titulo=dict(pt="Orografias", en="Orografias"),
 onde=dict(pt="Giefarte, Lisboa, 2019. Curadoria de Maria do Mar Fazenda",
           en="Giefarte, Lisbon, 2019. Curated by Maria do Mar Fazenda"),
 texto=dict(
  pt=["Exposição individual na Giefarte, em Lisboa, com curadoria de Maria do Mar Fazenda. O catálogo, editado pela Giefarte e pela Documenta, inclui o texto da curadora, <cite>Cadernos de campo e contracampo</cite>."],
  en=["Solo exhibition at Giefarte, Lisbon, curated by Maria do Mar Fazenda. The catalogue, published by Giefarte and Documenta, includes the curator's essay <cite>Field and Counter-Field Notebooks</cite>."]),
 textos=["mdmf-orografias"],
 imagens=[
  ("wp/2019/06/orografias-web.jpg", "<cite>Orografias</cite>, 2018, 460x110 cm.", "<cite>Orografias</cite>, 2018, 460x110 cm.", None),
  ("wp/2019/09/triptico-03-109x151cm-1.jpg", "<cite>Orografias 1/3</cite>, 2018.", "<cite>Orografias 1/3</cite>, 2018.", None),
  ("wp/2019/09/triptico-02-109x151cm-1.jpg", "<cite>Orografias 2/3</cite>, 2018.", "<cite>Orografias 2/3</cite>, 2018.", None),
  ("wp/2019/09/triptico-01-109x151cm-1.jpg", "<cite>Orografias 3/3</cite>, 2018.", "<cite>Orografias 3/3</cite>, 2018.", None),
  ("wp/2019/09/orografias34-38x48cm.jpg", "<cite>Orografias #34</cite>, 2019.", "<cite>Orografias #34</cite>, 2019.", None),
  ("wp/2019/09/orografias29-38x48cm.jpg", "<cite>Orografias #29</cite>, 2019.", "<cite>Orografias #29</cite>, 2019.", None),
  ("wp/2019/08/orografias21-38x48cm-1.jpg", "<cite>Orografias #21</cite>, 2018.", "<cite>Orografias #21</cite>, 2018.", None),
  ("wp/2019/06/2019-0rografias-cat-web.jpg", "Catálogo da exposição, Giefarte/Documenta, Lisboa, 2019.", "Exhibition catalogue, Giefarte/Documenta, Lisbon, 2019.", None),
 ],
 rever=["texto PT e EN (escrito de novo, só factual)", "legendas sem técnica: os nomes dos ficheiros sugerem 109x151 cm (tríptico) e 38x48 cm", "título EN do ensaio (no site antigo: 'Field and counter-field')"],
),

# ------------------------------------------------------------------
dict(
 slug="caixa-de-desenho", ano="2017–18",
 titulo=dict(pt="Caixa de Desenho", en="Drawing Box"),
 onde=dict(pt="Quase Galeria, Porto, 2017 · Drawing Room, Madrid, 2018 · Fundação Eugénio de Almeida, Évora, 2019",
           en="Quase Galeria, Porto, 2017 · Drawing Room, Madrid, 2018 · Fundação Eugénio de Almeida, Évora, 2019"),
 texto=dict(
  pt=["<cite>Caixa de Desenho</cite>, 2018. Madeira, MDF, papel, tinta acrílica, fio de algodão, dimensões variáveis (aprox. 250x300x200 cm).",
      "A primeira <cite>Caixa de Desenho</cite> foi mostrada em 2017 na Quase Galeria, no Porto, numa exposição com curadoria de Fátima Lambert."],
  en=["<cite>Drawing Box</cite>, 2018. Wood, MDF, watercolor paper, acrylic ink, cotton thread, variable dimensions (approx. 250x300x200 cm).",
      "The first <cite>Drawing Box</cite> was shown in 2017 at Quase Galeria, Porto, in an exhibition curated by Fátima Lambert."]),
 textos=["lambert-caixa"],
 imagens=[
  ("wp/2018/09/2018-drawingbox-madrid1ad.jpg", "<cite>Caixa de Desenho</cite>, 2018, pormenor. Vista na Drawing Room, Madrid.", "<cite>Drawing Box</cite>, 2018, detail. View at Drawing Room, Madrid.", None),
  ("wp/2018/09/2018-drawingbox-madrid3ad.jpg", "<cite>Caixa de Desenho</cite>, 2018, pormenor. Vista na Drawing Room, Madrid.", "<cite>Drawing Box</cite>, 2018, detail. View at Drawing Room, Madrid.", None),
  ("wp/2018/09/2018-drawingbox-1ad.jpg", "<cite>Caixa de Desenho</cite>, 2018, no atelier.", "<cite>Drawing Box</cite>, 2018, in the studio.", None),
  ("wp/2018/06/2019-CaixaDesenho-FEA003-web.jpg", "<cite>Caixa de Desenho</cite>, 2018. Vista na Fundação Eugénio de Almeida, Évora, 2019.", "<cite>Drawing Box</cite>, 2018. View at Fundação Eugénio de Almeida, Évora, 2019.", None),
  ("wp/2018/06/2019-CaixaDesenho-FEA011-web.jpg", "<cite>Caixa de Desenho</cite>, 2018, pormenor. Fundação Eugénio de Almeida, Évora, 2019.", "<cite>Drawing Box</cite>, 2018, detail. Fundação Eugénio de Almeida, Évora, 2019.", None),
  ("wp/2018/06/2019-CaixaDesenho-FEA007-web.jpg", "<cite>Caixa de Desenho</cite>, 2018, pormenor. Fundação Eugénio de Almeida, Évora, 2019.", "<cite>Drawing Box</cite>, 2018, detail. Fundação Eugénio de Almeida, Évora, 2019.", None),
  ("wp/2018/06/2019-CaixaDesenho-FEA013-web.jpg", "<cite>Caixa de Desenho</cite>, 2018, pormenor. Fundação Eugénio de Almeida, Évora, 2019.", "<cite>Drawing Box</cite>, 2018, detail. Fundação Eugénio de Almeida, Évora, 2019.", None),
  ("wp/2020/06/drawing-box-closed.jpg", "<cite>Caixa de Desenho</cite>, fechada.", "<cite>Drawing Box</cite>, closed.", None),
  ("wp/2020/06/Leitao-Caixa-Desenho06.jpg", "<cite>Caixa de Desenho 1</cite>, 2017.", "<cite>Drawing Box 1</cite>, 2017.", None),
  ("wp/2020/06/Leitao-Caixa-Desenho04.jpg", "<cite>Caixa de Desenho 1</cite>, 2017.", "<cite>Drawing Box 1</cite>, 2017.", None),
  ("wp/2020/06/Leitao-Caixa-Desenho03.jpg", "<cite>Caixa de Desenho 1</cite>, 2017.", "<cite>Drawing Box 1</cite>, 2017.", None),
  ("wp/2020/06/Leitao-Caixa-Desenho01.jpg", "<cite>Caixa de Desenho 1</cite>, 2017.", "<cite>Drawing Box 1</cite>, 2017.", None),
  ("wp/2017/09/caixa-de-desenho_0034.jpg", "<cite>Caixa de Desenho 1</cite>, 2017.", "<cite>Drawing Box 1</cite>, 2017.", None),
 ],
 rever=["segundo parágrafo (escrito de novo, factual)"],
),

# ------------------------------------------------------------------
dict(
 slug="paisagem-instavel", ano="2017",
 titulo=dict(pt="Paisagem Instável", en="Paisagem Instável"),
 onde=dict(pt="Carlos Carvalho Arte Contemporânea, Lisboa, 25.11.2017–13.01.2018",
           en="Carlos Carvalho Arte Contemporânea, Lisbon, 25.11.2017–13.01.2018"),
 texto=dict(
  pt=["Esculturas da série <cite>Paisagem Instável</cite> e duas séries de desenho que acompanham o projecto: <cite>Apontamentos</cite>, aguarela, guache e tinta acrílica sobre papel, 76x111 cm, e <cite>Monocultura</cite>, aguarela, guache, tinta acrílica e corte sobre papel, 66x570 cm."],
  en=["Sculptures from the <cite>Paisagem Instável</cite> (Unstable Landscape) series and two series of drawings that were part of the project: <cite>Apontamentos</cite>, watercolor, gouache and acrylic ink on paper, 76x111 cm, and <cite>Monocultura</cite>, watercolor, gouache, acrylic ink and cutouts on paper, 66x570 cm."]),
 textos=["roseira-paisagem"],
 imagens=[
  ("wp/2018/01/catarina-leitao_paisagem-instavel-vista1.jpg", "Vista da exposição <cite>Paisagem Instável</cite>, Carlos Carvalho Arte Contemporânea, Lisboa, 2017.", "Installation view, <cite>Paisagem Instável</cite>, Carlos Carvalho Arte Contemporânea, Lisbon, 2017.", None),
  ("wp/2018/01/catarina-leitao_paisagem-instavel-5a.jpg", "<cite>Paisagem Instável #5</cite>, 2017.", "<cite>Paisagem Instável #5</cite>, 2017.", None),
  ("wp/2018/01/catarina-leitao_paisagem-instavel-8.jpg", "<cite>Paisagem Instável #8</cite>, 2017.", "<cite>Paisagem Instável #8</cite>, 2017.", None),
  ("wp/2018/01/catarina-leitao_paisagem-instavel-3.jpg", "<cite>Paisagem Instável #3</cite>, 2017.", "<cite>Paisagem Instável #3</cite>, 2017.", None),
  ("wp/2018/01/catarina-leitao_paisagem-instavel-6.jpg", "<cite>Paisagem Instável #6</cite>, 2017.", "<cite>Paisagem Instável #6</cite>, 2017.", None),
  ("wp/2018/01/catarina-leitao_paisagem-instavel-1.jpg", "<cite>Paisagem Instável #1</cite>, 2017.", "<cite>Paisagem Instável #1</cite>, 2017.", None),
  ("wp/2018/01/catarina-leitao_paisagem-instavel-7-det.jpg", "<cite>Paisagem Instável #7</cite>, 2017, pormenor.", "<cite>Paisagem Instável #7</cite>, 2017, detail.", None),
  ("wp/2018/01/catarina-leitao_paisagem-instavel-vista13.jpg", "Vista da exposição <cite>Paisagem Instável</cite>, Carlos Carvalho Arte Contemporânea, Lisboa, 2017.", "Installation view, <cite>Paisagem Instável</cite>, Carlos Carvalho Arte Contemporânea, Lisbon, 2017.", None),
  ("wp/2018/01/catarina-leitao_paisagem-instavel-monocultura.jpg", "<cite>Monocultura</cite>, 2017, tinta acrílica, aguarela, guache e corte sobre papel, 63x570 cm.", "<cite>Monocultura</cite>, 2017, acrylic ink, watercolor, gouache and cutouts on paper, 63x570 cm.", None),
  *[(f"wp/2018/01/apontamentos{n}.jpg", f"<cite>Apontamentos #{n}</cite>, 2017, tinta acrílica, aguarela e guache sobre papel, {d.replace('.',',')}.",
     f"<cite>Apontamentos #{n}</cite>, 2017, acrylic ink, watercolor and gouache on paper, {d}.", None)
    for n, d in [("3","76x111 cm"),("4","76x111 cm"),("6","76x110 cm"),("2","76x111 cm"),("5","76x111 cm")]],
 ],
 rever=["texto PT e EN (factual, a partir do site antigo)", "Monocultura: 66x570 cm no texto, 63x570 cm na legenda", "#8, #7 e a vista 13 só existem em versão reduzida (600 a 1024 px)", "Apontamentos #9 fica de fora: só existe com 150 px", "texto de José Roseira só em PT"],
),

# ------------------------------------------------------------------
dict(
 slug="dendrograma-versao-mini", ano="2015",
 titulo=dict(pt="Dendrograma | Tree-kit (versão mini)", en="Dendrogram | Tree-kit (Mini Version)"),
 onde=dict(pt="Colecção do Davis Lisboa Mini-Museum of Contemporary Art, Barcelona",
           en="Collection of the Davis Lisboa Mini-Museum of Contemporary Art, Barcelona"),
 texto=dict(
  pt=["<cite>Dendrograma | Tree-kit (versão mini)</cite> foi feito durante o processo de criação de uma peça de grandes dimensões, <cite>Dendrograma | Tree-kit</cite>, em resposta a um convite do Davis Mini-Museum of Contemporary Art, em Barcelona.",
      "A miniaturização da caixa-contentor que guarda este pequeno desenho tridimensional em expansão acabou, por acaso, por lhe dar a forma de uma caixa de fósforos. A ligação à <cite>Total Art Match-Box</cite> (1965) de Ben Vautier trouxe as camadas de que o trabalho precisava para se resolver. A peça foi feita para residir na colecção do Davis Lisboa Mini-Museum of Contemporary Art."],
  en=["<cite>Dendrogram | Tree-kit (Mini Version)</cite> was made during the process of creating a large piece titled <cite>Dendrogram | Tree-kit</cite>, in response to an invitation by the Davis Mini-Museum of Contemporary Art in Barcelona.",
      "In the process, the miniaturization of a box/container to hold the expanding mini 3D drawing accidentally grew into the shape of a matchbox. The link to Ben Vautier's <cite>Total Art Match-Box</cite> (1965) offered the new set of layers needed to resolve the work, which was made to reside in the collection of the Davis Lisboa Mini-Museum of Contemporary Art."]),
 video=dict(url="https://youtu.be/zttVNB-XOBE", pt="Vídeo, cinematografia de Rui Pinheiro", en="Video, cinematography by Rui Pinheiro"),
 textos=["dendrogram-mini"],
 imagens=[
  ("wp/2017/09/leitao-00-fb0a9987.jpg", "<cite>Dendrograma | Tree-kit (versão mini)</cite>, 2015.", "<cite>Dendrogram | Tree-kit (Mini Version)</cite>, 2015.", None),
  ("wp/2017/09/leitao-fb0a9966.jpg", "<cite>Dendrograma | Tree-kit (versão mini)</cite>, 2015.", "<cite>Dendrogram | Tree-kit (Mini Version)</cite>, 2015.", None),
  ("wp/2017/09/leitaofb0a0013.jpg", "<cite>Dendrograma | Tree-kit (versão mini)</cite>, 2015.", "<cite>Dendrogram | Tree-kit (Mini Version)</cite>, 2015.", None),
 ],
 rever=["texto PT (traduzido do EN)", "título PT 'versão mini'"],
),

# ------------------------------------------------------------------
dict(
 slug="dendrograma", ano="2016–26",
 titulo=dict(pt="Dendrograma | Tree-kit", en="Dendrogram | Tree-kit"),
 onde=dict(pt="MCO Arte Contemporânea, Porto, 2016 · Centro Cultural de Cascais, 2026",
           en="MCO Arte Contemporânea, Porto, 2016 · Centro Cultural de Cascais, 2026"),
 texto=dict(
  pt=["Um projecto sobre a portabilidade, o desenho no espaço, repouso/agência e a ideia (intraduzível) de <i lang=\"en\">freedom of display</i>.",
      "<cite>Dendrograma | Tree-kit</cite> é o produto de uma pesquisa sobre as possibilidades do desenho no espaço. Composta por módulos de madeira pintada, esta peça funciona como um desenho tridimensional que incorpora os efeitos de luz e sombra que se projectam nas superfícies do seu contentor — o espaço de exposição. <cite>Dendrograma</cite> é um kit: as suas peças modulares são ramos transformados que se encaixam uns nos outros e podem ser montados como uma tenda. Este processo torna a obra portátil e mutante: pode estar fechada ou aberta, em repouso ou a actuar no espaço quando manipulada por um participante. Este kit condensa três momentos: um inicial, de repouso e portabilidade (fechado, bidimensional), o acto performativo (abrir, instalar), e o corpo expandido (aberto, tridimensional)."],
  en=["<cite>Dendrogram | Tree-kit</cite> is a product of a research on the possibilities of drawing in space. Composed of painted wood modules, the piece is a three-dimensional drawing that incorporates the effects of light and shadow on the container's surfaces — the exhibition space.",
      "<cite>Dendrogram</cite> is a kit, several pieces that fit into a box or a bag. Its transformed branches may be mounted in a tent-like fashion. This makes the artwork portable and mutant: it is either closed or open, still or active in space through the manipulation of its parts by a participant.",
      "In the <cite>Dendrogram</cite> works, the original material of the tree shapes is hidden. Existing tree sticks are altered and painted into new shapes representing new-formed tree branches. This body of work entangles fact and fiction, organic and mechanic, natural and artificial, sculpture and drawing."]),
 textos=["dendrograma-pt"],
 imagens=[(f"wp/2016/06/dendrogram-ad-2020-0{n}.jpg",
           "<cite>Dendrograma | Tree-kit</cite>, 2016, madeira, tubo de alumínio, tinta, velcro, tecido, dimensões variáveis. Vista na MCO Arte Contemporânea, Porto, 2016.",
           "<cite>Dendrogram | Tree-kit</cite>, 2016, wood, aluminum tube, paint, velcro, fabric, variable dimensions. View at MCO Arte Contemporânea, Porto, 2016.", None)
          for n in [1,6,7,2,4,5,3]] + [
  ("dr/CatarinaLeitao-Eco-nomia-CCC-09.jpg", DENDRO_2026_PT, DENDRO_2026_EN, JL),
  ("dr/CatarinaLeitao-Eco-nomia-CCC-10.jpg", "<cite>Dendrograma | Tree-kit</cite>, pormenor. Centro Cultural de Cascais, 2026.", "<cite>Dendrogram | Tree-kit</cite>, detail. Centro Cultural de Cascais, 2026.", JL),
 ],
 rever=[],
),

# ------------------------------------------------------------------
dict(
 slug="atelier-portatil", ano="2013–19",
 titulo=dict(pt="Atelier Portátil", en="Portable Studio"),
 onde=dict(pt="Carlos Carvalho Arte Contemporânea, Lisboa, 2014 · Abreu Advogados / Carpe Diem Arte e Pesquisa, Lisboa, 2019",
           en="Carlos Carvalho Arte Contemporânea, Lisbon, 2014 · Abreu Advogados / Carpe Diem Arte e Pesquisa, Lisbon, 2019"),
 texto=dict(
  pt=["O <cite>Atelier Portátil</cite> é uma caixa com rodas construída à medida das minhas necessidades para desenhar no campo. O atelier não é usado como atelier, faz parte de uma ficção montada para pensar o processo e a circulação da obra do atelier para o museu, através de estruturas móveis. Este atelier/objecto/contentor expande-se no espaço ao ar livre e contém uma série de objectos utilitários por mim fabricados: uma tenda-abrigo, que pode ser montada e desmontada, uma bata de trabalho e um caderno de campo. A bata/vestido funciona ela própria como contentor/atelier, com bolsos especificamente desenhados para alojar objectos e materiais. Fazem parte do trabalho reportagens fotográficas e vídeo de performances no campo, em colaboração com o fotógrafo Rui Pinheiro."],
  en=["The <cite>Portable Studio</cite> is a box on wheels, built to my own requirements for drawing in the field. It is not used as a studio: it belongs to a fiction set up to think through the process and circulation of the work, from studio to museum, by means of mobile structures. This studio/object/container unfolds in the open air and holds a series of utilitarian objects I have made: a tent-shelter that can be put up and taken down, a work smock and a field notebook. The smock/dress is itself a container/studio, with pockets designed to hold specific objects and materials. The work includes photographic records and video of performances in the field, made in collaboration with the photographer Rui Pinheiro."]),
 textos=["fale-2019"],
 imagens=[
  ("wp/2017/09/2014-atelier-portatil-inst-02-1.jpg",
   "<cite>Atelier Portátil, Protótipo #1</cite>, 2013–14, madeira, tecido, metal, objectos encontrados, dimensões variáveis. Vídeo/performance <cite>Atelier Portátil, Protótipo #1, Cena 5</cite>, 12 min, cinematografia de Rui Pinheiro. Vista na Carlos Carvalho Arte Contemporânea, Lisboa.",
   "<cite>Portable Studio, Prototype #1</cite>, 2013–14, wood, fabric, metal, found objects, variable dimensions. Video/performance <cite>Portable Studio, Prototype #1, Scene 5</cite>, 12 min, cinematography by Rui Pinheiro. View at Carlos Carvalho Arte Contemporânea, Lisbon.", None),
  ("wp/2015/06/Catarina-Leitao_2019-72-von-80.jpg", "<cite>Atelier Portátil</cite>, vista da exposição individual na Abreu Advogados / Carpe Diem Arte e Pesquisa, Lisboa, 2019.", "<cite>Portable Studio</cite>, view of the solo exhibition at Abreu Advogados / Carpe Diem Arte e Pesquisa, Lisbon, 2019.", None),
  ("wp/2015/06/Catarina-Leitao_2019-78-von-80.jpg", "<cite>Atelier Portátil, Protótipo #1, Cena 1</cite>, 2014. Imagens da performance, impressão digital, 120x80 cm.", "<cite>Portable Studio, Prototype #1, Scene 1</cite>, 2014. Performance images, digital print, 120x80 cm.", "Rui Pinheiro"),
  ("wp/2015/06/Catarina-Leitao_2019-76-von-80.jpg", "<cite>Atelier Portátil</cite>, vista da exposição individual na Abreu Advogados / Carpe Diem Arte e Pesquisa, Lisboa, 2019.", "<cite>Portable Studio</cite>, view of the solo exhibition at Abreu Advogados / Carpe Diem Arte e Pesquisa, Lisbon, 2019.", None),
 ],
 rever=["texto EN", "ligar aqui o texto de Laura Sequeira Falé (2019)?"],
),

# ------------------------------------------------------------------
dict(
 slug="gabinete", ano="2013–15",
 titulo=dict(pt="Gabinete", en="Cabinet"),
 onde=dict(pt="", en=""),
 texto=dict(
  pt=["<cite>Gabinete</cite>, 2013. Técnica mista, madeira, alumínio, velcro, tecido e papel, 80x30x20 cm (fechado).",
      "<cite>Gabinete</cite> é um corpo híbrido que se insinua no espaço como um organismo independente: adaptável e dinâmico. <span class=\"assinatura\">— José Roseira, 2013</span>"],
  en=["<cite>Cabinet</cite>, 2013. Mixed media, wood, aluminum, velcro, fabric and paper, 80x30x20 cm (closed).",
      "<cite>Cabinet</cite> is a hybrid body that reveals itself in space as an independent organism: adaptable and dynamic. <span class=\"assinatura\">— José Roseira, 2013</span>"]),
 textos=["roseira-gabinete"],
 imagens=[
  ("wp/2017/09/leitao_cabinet-2.jpg", "<cite>Gabinete</cite>, 2013.", "<cite>Cabinet</cite>, 2013.", None),
  ("wp/2017/09/leitao_cabinet-4.jpg", "<cite>Gabinete</cite>, 2013.", "<cite>Cabinet</cite>, 2013.", None),
  ("wp/2017/09/leitao_cabinet-5.jpg", "<cite>Gabinete</cite>, 2013.", "<cite>Cabinet</cite>, 2013.", None),
  ("wp/2013/06/Cabinet-book03.jpg", "<cite>Cabinet Book</cite>, 2015.", "<cite>Cabinet Book</cite>, 2015.", None),
  ("wp/2013/06/Cabinet-book01.jpg", "<cite>Cabinet Book</cite>, 2015.", "<cite>Cabinet Book</cite>, 2015.", None),
  ("wp/2013/06/Cabinet-book04.jpg", "<cite>Cabinet Book</cite>, 2015.", "<cite>Cabinet Book</cite>, 2015.", None),
  ("wp/2013/06/Cabinet-book02.jpg", "<cite>Cabinet Book</cite>, 2015.", "<cite>Cabinet Book</cite>, 2015.", None),
 ],
 rever=["frase de José Roseira usada como sinopse (adaptada da última frase do texto)"],
),

# ------------------------------------------------------------------
dict(
 slug="systema-naturae", ano="2012",
 titulo=dict(pt="Systema Naturæ", en="Systema Naturæ"),
 grelha=dict(pt="Systema Naturæ, instalação", en="Systema Naturæ, installation"),
 onde=dict(pt="Carlos Carvalho Arte Contemporânea, Lisboa, 2012", en="Carlos Carvalho Arte Contemporânea, Lisbon, 2012"),
 texto=dict(
  pt=["<cite>Systema Naturæ</cite> é um projecto de instalação e desenho que, partindo de uma investigação no campo da ciência botânica, propõe a adição de elementos ficcionais à lista das espécies conhecidas. Neste trabalho imaginei e desenhei espécies botânicas cruzadas com formas mecânicas, vegetais híbridos alusivos à manipulação do natural e a construções artificiais.",
      "A instalação final do projecto incluía oito desenhos de grandes dimensões, alusivos a cartazes escolares, e uma série de desenhos em pequeno e médio formato, dispostos em mobiliário específico. Uma peça central no dispositivo da instalação, o Museu Portátil, apresentou-se como um repositório de artefactos didácticos e museológicos: uma caixa transportável onde podiam ser arrumados os objectos que compunham a exposição, aludindo a temas como a portabilidade e a migração, centrais no meu percurso artístico.",
      "O <cite>Guia de Espécies</cite>, livro de artista, serviu de guia à exposição. Ainda no contexto da exposição foi apresentada uma publicação de autor, fruto de uma colaboração com o escritor José Roseira."],
  en=["<cite>Systema Naturæ</cite>, an installation/drawing project, is a fictional botanical study. In my research, I create and draw botanical species crossed with mechanical and constructed shapes. Like hybrid plants, they allude to the manipulation of the natural world.",
      "The installation includes eight large watercolor drawings that reference educational charts, and small drawings of each of the invented species, displayed in furniture specifically built for them. A sculptural piece, the Portable Museum, is a box/crate on wheels filled with objects and materials related to the whole exhibition. The Portable Museum could hold the entire contents of the exhibition, addressing the ideas of portability and nomadism, critical in my artwork.",
      "The <cite>Species Guide</cite>, an artist's book, served as a guide to the exhibition. A book, <cite>Systema Naturæ</cite>, was produced in collaboration with the writer José Roseira."]),
 textos=["systema-naturae"],
 imagens=[(f"wp/{p}", "<cite>Systema Naturæ</cite>, vista da instalação, 2012.", "<cite>Systema Naturæ</cite>, installation view, 2012.", None)
          for p in ["2017/09/20120418_0721.jpg","2017/09/20120418_0722.jpg","2017/09/20120418_0683.jpg","2017/09/20120418_0699-2.jpg","2017/09/catarinaleitao_sn_inst_010.jpg","2017/09/20120418_0679.jpg"]]
        + [(f"wp/2020/06/SN-Guia{n}.jpg",
            "<cite>Guia de Espécies</cite>, 2012, edição de 3, 56 páginas, impressões laser, encadernação japonesa de quatro furos com estrutura de madeira.",
            "<cite>Species Guide</cite>, 2012, edition of 3, 56 pages, laser prints, Japanese four-hole binding with wood structure.", None)
           for n in ["08","10","09","04","06","07"]],
 rever=["título PT do guia ('Guia de Espécies')", "último parágrafo condensado a partir dos textos do site antigo"],
),

# ------------------------------------------------------------------
dict(
 slug="systema-naturae-desenhos", ano="2011–12",
 titulo=dict(pt="Systema Naturæ, desenhos", en="Systema Naturæ, drawings"),
 onde=dict(pt="Carlos Carvalho Arte Contemporânea, Lisboa, 2012", en="Carlos Carvalho Arte Contemporânea, Lisbon, 2012"),
 texto=dict(
  pt=["As novas espécies inventadas, desenhadas e conformadas a uma estética didáctica e museológica, foram classificadas com base no estudo de regras de taxonomia vegetal e seguindo sistemas de classificação tradicionais (baseados na morfologia externa das espécies). Nomes em latim existentes que descrevem características de género e de espécie foram conjugados com novos termos, traduzidos ou inventados para latim botânico, estabelecendo ligações entre as várias denominações e os seus significados, equacionando novos sentidos, contraditórios, absurdos ou irónicos."],
  en=["Making use of Latin epithets that describe characteristics of genera and species, I transform them, combining them with translated contemporary words, looking for composites that create new meanings. The results are either absurd, ironic, ambivalent, sometimes amusing, but always follow the rules of taxonomic nomenclature and of the use of Botanical Latin. My species are then grouped in families which are also newly named."]),
 textos=["systema-naturae"],
 imagens=[
  ("wp/2017/09/sn_004a.jpg", *sn("Cucurbitoides cassidea (Aeriaceae)", *AG, "138x105 cm"), None),
  ("wp/2017/09/sn_009.jpg", *sn("Dubitatio binata (Thecaceae)", *AGS, "76x56 cm"), None),
  ("wp/2017/09/sn_005a.jpg", *sn("Organum tubulosum (Tubulaceae)", *AG, "138x105 cm"), None),
  ("wp/2017/09/sn_006a.jpg", *sn("Theoria tubiforme e Theoria melanopicta (Tubulaceae)", *AG, "138x105 cm"), None),
  ("wp/2017/09/sn_008a.jpg", *sn("Mombasae anemophila (Aeriaceae)", *AGS, "138x105 cm"), None),
  ("wp/2017/09/sn_003a.jpg", *sn("Instrumentum ventifolium (Aeriaceae)", *AG, "138x105 cm"), None),
  ("wp/2017/09/sn_002a2.jpg", *sn("Digitus sativus (Tubulaceae)", *AGS, "138x105 cm"), None),
  ("wp/2017/09/sn_001a.jpg", *sn("Machinamentum unifolium (Tubulaceae)", *AG, "138x105 cm"), None),
  ("wp/2012/06/SN-drw.jpg", *sn("Dubitatio binervatus e Noverboracus multinervatus (Thecaceae)", *AGS, "110x49 cm"), None),
  ("wp/2017/09/20120418_0651.jpg", "<cite>Systema Naturæ</cite>, vista da instalação, 2012.", "<cite>Systema Naturæ</cite>, installation view, 2012.", None),
 ],
 rever=[],
),

# ------------------------------------------------------------------
dict(
 slug="invasive-species", ano="2010–11",
 titulo=dict(pt="Invasive Species", en="Invasive Species"),
 onde=dict(pt="Carpe Diem Arte e Pesquisa, Lisboa, 2010 · Casa das Artes, Vigo, 2011",
           en="Carpe Diem Arte e Pesquisa, Lisbon, 2010 · Casa das Artes, Vigo, 2011"),
 texto=dict(
  pt=["<cite>Invasive Species</cite> é uma instalação/livro. Uma caixa dentro da qual cabem todos os desenhos em estrutura de harmónio funciona como um livro gigante. Quando a peça é instalada ocupa o espaço e o espectador pode circular pelo meio das páginas. As folhas de papel, pintadas a aguarela e tinta sumi, têm aberturas e possibilitam a transformação das vistas pela movimentação do corpo e mudanças de pontos de vista. Um vídeo montado numa pequena caixa descreve a performance do folhear das páginas quando em “estado livro”.",
      "O título da obra faz referência às espécies invasoras na cidade: a vegetação que cresce descontrolada e que não se deixa domesticar.",
      "O papel como material tridimensional actua no espaço ao mesmo tempo que contém imagens na sua superfície bidimensional. A pesquisa a partir dos desdobramentos e relações entre os espaços a duas e três dimensões está na base desta série, onde a bidimensionalidade do papel é posta em causa a partir da perfuração do mesmo. O papel torna-se objecto, as aberturas oferecem uma nova dimensão ao desenho. Este projecto surgiu da pesquisa iniciada em <cite>Uplift</cite>, 2008, agora com o intuito de intervir no espaço e criar uma relação com o corpo.",
      "Aguarela e tinta sumi sobre papel, cabo de aço, madeira, pesos de chumbo, fio de linho, molas metálicas, dimensões variáveis. Caixa fechada: 60x42x9 cm."],
  en=["<cite>Invasive Species</cite> is a portable installation. It functions as a book when not on display. Dimensions of closed box: 24x17x3.5 inches / 60x42x9 cm.",
      "Watercolor and sumi ink on paper, cable, wood, lead weights, linen string and metal clips, variable dimensions."]),
 video=dict(url="https://vimeo.com/688884800", pt="Vídeo, 1:49 min, fotografia de Luísa Ferreira", en="Video, 1:49 min, photography by Luísa Ferreira"),
 imagens=[
  ("wp/2017/09/2011_is_0001.jpg", "<cite>Invasive Species</cite>, 2010–11. Vista na Casa das Artes, Vigo, 2011.", "<cite>Invasive Species</cite>, 2010–11. View at Casa das Artes, Vigo, 2011.", None),
  ("wp/2017/09/2011_is_0004.jpg", "<cite>Invasive Species</cite>, 2010–11.", "<cite>Invasive Species</cite>, 2010–11.", None),
  ("wp/2017/09/2011_isbook_24.jpg", "<cite>Invasive Species</cite>, imagem do vídeo, 2010–11.", "<cite>Invasive Species</cite>, video still, 2010–11.", "Luísa Ferreira"),
  ("wp/2017/09/2011_is_0022.jpg", "<cite>Invasive Species</cite>, 2010–11.", "<cite>Invasive Species</cite>, 2010–11.", None),
 ],
 rever=["ligação ao vídeo: uso a do Vimeo citada na tese (o site antigo tinha YouTube)", "primeira imagem: confirmar que é a vista de Vigo"],
),

# ------------------------------------------------------------------
dict(
 slug="uplift", ano="2008",
 titulo=dict(pt="Uplift", en="Uplift"),
 onde=dict(pt="Center for Book Arts, Nova Iorque, 2008", en="Center for Book Arts, New York, 2008"),
 texto=dict(
  pt=["<cite>Uplift</cite>, feito em 2008 no Center for Book Arts, em Nova Iorque, durante uma residência artística, foi decisivo na minha pesquisa. Plataforma para explorar a articulação entre escultura e desenho, este livro pop-up conduziu a trabalhos posteriores como <cite>Invasive Species</cite>, 2010–11, uma peça que pode funcionar como livro ou expandir-se numa instalação que ocupa uma sala inteira. A mudança nas relações de escala que uma peça aberta ou fechada pode gerar pesa no modo como é percebida, e acrescenta uma camada à ideia de economia de meios, presente na minha prática.",
      "Em <cite>Uplift</cite>, construí uma narrativa a partir de uma série de desenhos a preto e branco. Traçando relações ambíguas entre figura e fundo através de formas de um negro profundo e de áreas brancas, os desenhos representam cenas de uma interacção entre um mundo orgânico e um mundo construído. No livro acrescento uma componente tridimensional, para alargar o alcance espacial do desenho, introduzindo volumes positivos e negativos, orifícios, luz e sombra.",
      "Livro com sete secções, impressão tipográfica com matrizes de polímero, tinta sumi, encadernação em capa dura revestida a tecido. Edição de 5 + 1 PA. Impresso e encadernado por mim no Center for Book Arts."],
  en=["<cite>Uplift</cite>, created in 2008 at the Center for Book Arts in New York during an artist residency, was pivotal in my research. As a platform to explore the articulation between sculpture and drawing, this pop-up book led to subsequent works such as <cite>Invasive Species</cite>, 2010–11, a piece which may function as a book or expand into an installation that occupies a whole room. The shift in scale relations that an open or closed piece can generate is significant in terms of how it is perceived, and it adds another layer to the idea of an economy of means, present in my practice.",
      "In <cite>Uplift</cite>, a narrative was created from a series of black and white drawings. Tracing ambiguous relationships between figure and ground through deep black shapes and white areas, the drawings represent scenes of an interaction between an organic and a constructed world. In the book, I add a three-dimensional component, aiming to expand the spatial scope of drawing, introducing positive and negative volumes, orifices, light and shade.",
      "Pop-up book, letterpress-printed from polymer plates and hand-painted with sumi ink. Edition of 5, signed and numbered. Printed and bound by the artist at the Center for Book Arts, New York."]),
 video=dict(url="https://vimeo.com/688963244", pt="Vídeo, 1:20 min, fotografia de Luísa Ferreira", en="Video, 1:20 min, photography by Luísa Ferreira"),
 textos=["uplift-en"],
 imagens=[(f"wp/2017/09/2008_uplift_{n}.jpg", "<cite>Uplift</cite>, 2008.", "<cite>Uplift</cite>, 2008.", None) for n in ["01","02","08","10","06","05","07"]],
 rever=["texto PT (traduzido do EN)", "ficha técnica PT tirada da tese"],
),

# ------------------------------------------------------------------
dict(
 slug="thicket-weatherproof", ano="2006–08",
 titulo=dict(pt="Thicket e Weatherproof", en="Thicket and Weatherproof"),
 onde=dict(pt="Number 35 Gallery, Nova Iorque, 2007 · Center for Book Arts, Nova Iorque, 2007",
           en="Number 35 Gallery, New York, 2007 · Center for Book Arts, New York, 2007"),
 texto=dict(
  pt=["A sequência de eventos catastróficos naturais e provocados que se sucederam na primeira década deste século inspiraram visões mais ou menos apocalípticas da paisagem. A pergunta o que é que é natural ou não traz novos problemas, e desenvolvi uma série de desenhos e livros que trabalham sobre ideias de causa e efeito, em pequenas narrativas onde permanece a ambiguidade: quem ou o que é que invade ou controla o quê. Os corpos de trabalho como <cite>Thicket</cite> (2007–2008) e <cite>Os Personagens, os Objectos e as Paisagens</cite> (2006) debruçam-se sobre estas questões. Várias figuras em fatos de protecção interagem com formas que por vezes parecem de origem orgânica para logo a seguir se confundirem com formas mecânicas, onde o próprio espaço bidimensional é indefinido nas suas relações forma-fundo. Aqui também, como noutros projectos, recorri à mistura de referências, algumas delas camufladas por um imaginário sobreposto: as imagens de guerra e catástrofes reencenadas a partir de reproduções de pinturas renascentistas.",
      "<cite>Weatherproof</cite> foi a primeira publicação que fiz no Center for Book Arts: um pequeno catálogo de imagens de formas alusivas a equipamento para resistir ao mau tempo e às condições meteorológicas adversas."],
  en=["The sequence of natural and man-made catastrophes that followed one another in the first decade of this century inspired more or less apocalyptic visions of landscape. The question of what is natural and what is not raises new problems, and I developed a series of drawings and books that work on ideas of cause and effect, in small narratives where ambiguity remains: who or what invades or controls what. Bodies of work such as <cite>Thicket</cite> (2007–2008) and <cite>The Characters, the Objects and the Landscapes</cite> (2006) take up these questions. Figures in protective suits interact with forms that at times seem organic, only to merge a moment later with mechanical forms, in a two-dimensional space whose figure-ground relations remain undefined. Here too, as in other projects, I drew on a mix of references, some of them camouflaged by a superimposed imagery: scenes of war and catastrophe restaged from reproductions of Renaissance paintings.",
      "<cite>Weatherproof</cite> was the first publication I made at the Center for Book Arts: a small catalog of images of forms alluding to equipment for withstanding bad weather and adverse conditions."]),
 imagens=[
  ("wp/2017/09/2007_0029_10in_v1.jpg", *thicket("29","2007","41x31 cm"), None),
  ("wp/2017/09/2006_0315_300dpi_v1.jpg", *thicket("315","2006","19x13 cm"), None),
  ("wp/2017/09/2007_0011_10in_v1.jpg", *thicket("11","2007","41x31 cm"), None),
  ("wp/2017/09/2007_0084b_300dpi.jpg", *thicket("84","2007","36x28 cm"), None),
  ("wp/2017/09/2007_0024_10in_v1.jpg", *thicket("24","2007","41x31 cm"), None),
  ("wp/2017/09/2007_0006_v1.jpg", *thicket("06","2007","36x28 cm"), None),
  ("wp/2017/09/2007_0071b_300dpi.jpg", *thicket("71","2007","36x28 cm"), None),
  ("wp/2017/09/2007_0061_10in_v1.jpg", *thicket("61","2007","36x28 cm"), None),
  ("wp/2017/09/2007_0026_10in_v1.jpg", *thicket("26","2007","41x31 cm"), None),
  ("wp/2017/09/2006_0309.jpg", *thicket("309","2006","19x13 cm"), None),
  ("wp/2017/09/2007_0075_300dpi.jpg", *thicket("75","2007","36x28 cm"), None),
  ("ex/weatherproof-01-capa.jpg",
   "<cite>Weatherproof</cite>, 2007, leporello, 16 páginas, impressão tipográfica com matrizes de polímero e tinta sumi, 15,5x10,5 cm (fechado). Edição de 50 exemplares assinados e numerados.",
   "<cite>Weatherproof</cite>, 2007, leporello, 16 pages, letterpress printed from polymer plates, sumi ink, 15.5x10.5 cm (closed). Edition of 50, signed and numbered.", None),
  *[(f"ex/weatherproof-0{n}.jpg", "<cite>Weatherproof</cite>, 2007.", "<cite>Weatherproof</cite>, 2007.", None) for n in [2,3,4,5,6]],
  ("ex/weatherproof-07-contracapa.jpg", "<cite>Weatherproof</cite>, 2007, contracapa.", "<cite>Weatherproof</cite>, 2007, back cover.", None),
 ],
 rever=["texto EN", "parágrafo sobre Weatherproof adaptado da tese", "local/ano: Number 35 Gallery 2007 (da CV)", "legendas: o site antigo diz 'ink on paper'; a tese diz 'tinta sumi e tinta da china' e dá 18x13 cm e 2007 para os pequenos"],
),

# ------------------------------------------------------------------
dict(
 slug="one-with-nature-natural-selection", ano="2005",
 titulo=dict(pt="One with Nature e Natural Selection", en="One with Nature and Natural Selection"),
 onde=dict(pt="MoMA/P.S.1, Nova Iorque, 2005 · Michael Steinberg Project Room, Nova Iorque, 2005",
           en="MoMA/P.S.1, New York, 2005 · Michael Steinberg Project Room, New York, 2005"),
 texto=dict(
  pt=["<cite>One with Nature</cite> partiu da ideia de desenhar uma coreografia com imagens de corpos à escala 1:1, protegidos com máscaras e portadores das formas naturais/artificiais que atravessam a minha obra. Representações de formas bélicas já estavam presentes em trabalhos anteriores de forma amenizada, através da interpretação do tecido camuflado e da exploração de formas híbridas entre a arma de fogo e o vegetal. O ambiente de guerra, nos anos 2003–2005 em Nova Iorque, onde vivia na altura, e os seus desenvolvimentos eram uma presença diária através de todos os media. Este contexto forma alicerces para projectos como a série <cite>One with Nature</cite>, onde as imagens alusivas a um conflito presente e ao mesmo tempo distante, filtrado pelos órgãos de comunicação social, se misturam com versões utilitárias de sobrevivência num mundo natural artificial.",
      "Os trabalhos sobre papel de <cite>Natural Selection</cite> seguem na continuação de uma pesquisa em redor da relação do urbano com a natureza. O título refere-se à obra de Darwin, que nesses anos estava a ser posta em causa por uma vaga conservadora na América, que apelava ao ensino do criacionismo e à abolição do ensino do evolucionismo de Darwin nas escolas. A representação de animais escultóricos baseia-se em imagens de construções utilizadas como chamarizes por caçadores: representações de animais desmontáveis e portáteis usadas para atrair a caça."],
  en=["<cite>One with Nature</cite> began from the idea of drawing a choreography with life-size images of bodies, protected by masks and carrying the natural/artificial forms that run through my work. Representations of warlike forms were already present, in a softened way, in earlier works, through the interpretation of camouflage fabric and the exploration of hybrid forms between firearm and plant. The climate of war in New York, where I was living between 2003 and 2005, and its developments were a daily presence across all media. This context lays the ground for projects such as the <cite>One with Nature</cite> series, where images alluding to a conflict at once present and distant, filtered through the news media, mix with utilitarian versions of survival in an artificial natural world.",
      "The works on paper in <cite>Natural Selection</cite> continue a line of research into the relationship between the urban and nature. The title refers to Darwin's work, which at the time was being challenged in the United States by a conservative wave calling for creationism to be taught in schools and for Darwin's theory of evolution to be dropped. The sculptural animals are based on images of constructions used as decoys by hunters: collapsible, portable representations of animals used to lure game."]),
 imagens=[
  ("wp/2017/09/2005_ps1_3_v2.jpg", "<cite>One with Nature</cite>, 2005, três desenhos, aguarela sobre papel, 180x106 cm (cada). Vista na exposição <cite>Greater New York 2005</cite>, MoMA/P.S.1, Nova Iorque.", "<cite>One with Nature</cite>, 2005, three drawings, watercolor on paper, 180x106 cm (each). View at <cite>Greater New York 2005</cite>, MoMA/P.S.1, New York.", None),
  ("wp/2017/09/2005_ps1_05_v2.jpg", "Vista na exposição <cite>Greater New York 2005</cite>, MoMA/P.S.1, Nova Iorque.", "View at <cite>Greater New York 2005</cite>, MoMA/P.S.1, New York.", None),
  ("wp/2017/09/2005_009_10in_v.jpg", *ns("One with Nature 009","2005","180x106 cm"), None),
  ("wp/2005/06/2005_NS_view2_v1.jpg", "Vista da exposição <cite>Natural Selection</cite>, Michael Steinberg Project Room, Nova Iorque, 2005.", "Installation view, <cite>Natural Selection</cite>, Michael Steinberg Project Room, New York, 2005.", None),
  ("wp/2017/09/2005_023_v1cut.jpg", *ns("Portable Deer","2005","96x70.5 cm"), "Paul Waldman"),
  ("wp/2017/09/2005_021_v1cut.jpg", *ns("Flying Duck","2005","96x70.5 cm"), "Paul Waldman"),
  ("wp/2017/09/2005_028_v1cut.jpg", *ns("Chair Container","2005","96x70.5 cm"), None),
  ("wp/2017/09/2005_014_v1cut.jpg", *ns("Air Filter","2005","98x68 cm"), "Paul Waldman"),
  ("wp/2005/06/2006_cera_expo_004.jpg", "Vista na Galeria Pedro Cera, Lisboa.", "View at Galeria Pedro Cera, Lisbon.", None),
  ("wp/2017/09/2005_022_v1cut.jpg", *ns("Assembled Deer","2005","96x70.5 cm"), "Paul Waldman"),
  ("wp/2017/09/2006_0001.jpg", *ns("Water System","2006","96x70.5 cm"), None),
  ("wp/2017/09/2005_015.jpg", *ns("Inflatable Life Vest","2005","100x68 cm"), None),
 ],
 rever=["texto EN", "créditos de Paul Waldman tirados da tese", "Air Filter: 2005 no site antigo, 2004 na tese", "galeria: 'Michael Steinberg Fine Art' no site antigo, 'Project Room' na CV"],
),

# ------------------------------------------------------------------
dict(
 slug="survival-systems", ano="2003–04",
 titulo=dict(pt="Survival Systems", en="Survival Systems"),
 onde=dict(pt="28.ª Bienal de Pontevedra, 2004. Curadoria de Miguel von Hafe Pérez e David G. Torres",
           en="28th Bienal de Pontevedra, 2004. Curated by Miguel von Hafe Pérez and David G. Torres"),
 texto=dict(
  pt=["<cite>Survival Systems – Urban Action Catalog 2003/2004</cite> é uma série de desenhos de grande formato que representa um catálogo fictício de produtos para usar ao ar livre. Este trabalho propõe a ideia de que a nossa ligação com a natureza é mediada por objectos que tiram partido da nossa necessidade de segurança e conforto. Dez desenhos, 175x107 cm (cada), aguarela e grafite (texto) sobre papel Arches.",
      "Um catálogo de equipamento para o corpo usar, apresenta-se como páginas de um livro ampliado. A relação de escala entre o observador e cada folha de papel subverte a relação de escala corpo/livro; o livro é um objecto único, feito à mão, contrariando a função de catálogo publicado em grandes tiragens para distribuição gratuita.",
      "Este trabalho foi realizado no contexto pós-ataques terroristas do 11 de Setembro de 2001 em Nova Iorque. O corpo de trabalho cresceu num atelier com vista para o Ground Zero, numa residência artística de seis meses promovida pelo Lower Manhattan Cultural Council. O trabalho em redor da ideia de kits para actividades ao ar livre, como o campismo ou os desportos radicais, foi fonte de inspiração para os projectos anteriores, com a recolha de catálogos e publicidade focados no consumo e na venda de conforto. Mas no contexto traumático que se vivia naquela altura, o mote deixou de ser o conforto e passou a ser o medo. Novos catálogos, lojas em Lower Manhattan, websites vendiam equipamento para protecção antiterrorismo. O consumo de máscaras e fatos de protecção para ataques bioquímicos, kits com pára-quedas para quem trabalha num arranha-céus, comida liofilizada, tendas e abrigos de emergência, providenciavam a sensação de segurança numa sociedade invadida e manipulada pelo medo.",
      "Os desenhos são feitos a aguarela e o texto, inspirado e adaptado a partir de catálogos existentes, é desenhado com processo de transferência e preenchimento a grafite."],
  en=["<cite>Survival Systems – Urban Action Catalog 2003/2004</cite> is a series of large-scale drawings – a fictional catalog of conceptual products for outdoor activities. This work addresses the idea that our interaction with nature is mediated by objects that exploit our need for safety and comfort. Ten drawings, 175x107 cm (69x42 in.) each, watercolor and graphite (text) on Arches paper.",
      "A catalog of equipment for the body, it is presented as the pages of an enlarged book. The scale relationship between the viewer and each sheet of paper subverts the usual relationship between body and book; the book is a unique, handmade object, running counter to the function of a catalog printed in large runs for free distribution.",
      "The work was made in the aftermath of the terrorist attacks of September 11, 2001 in New York. It grew in a studio overlooking Ground Zero, during a six-month residency run by the Lower Manhattan Cultural Council. Kits for outdoor activities such as camping or extreme sports had inspired earlier projects, through collected catalogs and advertising centered on the consumption and sale of comfort. In the traumatic climate of those years, the motif shifted from comfort to fear. New catalogs, shops in Lower Manhattan and websites sold anti-terrorism protective equipment. Masks and suits against biochemical attack, parachute kits for people working in skyscrapers, freeze-dried food, emergency tents and shelters offered a sense of security to a society invaded and manipulated by fear.",
      "The drawings are made in watercolor; the text, drawn from and adapted from existing catalogs, is traced by transfer and filled in with graphite."]),
 imagens=[
  ("wp/2017/09/2004_view_01.jpg", "Vista na 28.ª Bienal de Pontevedra, 2004.", "View at the 28th Bienal de Pontevedra, 2004.", None),
  ("wp/2017/09/2004_view_02.jpg", "Os dez desenhos instalados na 28.ª Bienal de Pontevedra, 2004.", "The ten drawings installed at the 28th Bienal de Pontevedra, 2004.", None),
  ("wp/2017/09/2003_001.jpg", *ss(1), None), ("wp/2017/09/2003_002.jpg", *ss(2), None), ("wp/2017/09/2003_003.jpg", *ss(3), None),
  ("wp/2017/09/2003_004.jpg", *ss(4), None), ("wp/2017/09/2003_005.jpg", *ss(5), None), ("wp/2017/09/2003_005d1.jpg", *ss(5, True), None),
  ("wp/2017/09/2003_006.jpg", *ss(6), None), ("wp/2017/09/2003_007.jpg", *ss(7), None), ("wp/2017/09/2003_008.jpg", *ss(8), None),
  ("wp/2017/09/2003_009.jpg", *ss(9), None), ("wp/2017/09/2003_010.jpg", *ss(10), None),
 ],
 rever=["texto EN: parágrafos 2 a 4 traduzidos do PT"],
),

# ------------------------------------------------------------------
dict(
 slug="survival-systems-socrates-sculpture-park", ano="2004",
 titulo=dict(pt="Survival Systems, Socrates Sculpture Park", en="Survival Systems, Socrates Sculpture Park"),
 onde=dict(pt="<cite>Field: Science, Technology and Nature</cite>, Socrates Sculpture Park, Nova Iorque, 2004. Curadoria de Alyson Baker",
           en="<cite>Field: Science, Technology and Nature</cite>, Socrates Sculpture Park, New York, 2004. Curated by Alyson Baker"),
 texto=dict(
  pt=["<cite>Survival Systems</cite>, 2004. Nove peças, impressões digitais montadas em alumínio, com dimensões entre 76x244 e 97x244 cm, instaladas ao ar livre no Socrates Sculpture Park, em Long Island City, Nova Iorque."],
  en=["<cite>Survival Systems</cite>, 2004. Nine pieces, digital prints mounted on aluminum, ranging from 76x244 to 97x244 cm (30x96 to 38x96 in.), installed outdoors at Socrates Sculpture Park, Long Island City, New York."]),
 imagens=[(f"wp/2017/09/{f}", "<cite>Survival Systems</cite>, 2004. Socrates Sculpture Park, Nova Iorque.", "<cite>Survival Systems</cite>, 2004. Socrates Sculpture Park, New York.", "Christian Nguyen")
          for f in ["park1.jpg","park5.jpg","park3.jpg","park2.jpg","detail0010_1bb.jpg"]],
 rever=["texto PT e EN reescrito a partir da legenda", "crédito Christian Nguyen tirado da tese"],
),

# ------------------------------------------------------------------
dict(
 slug="natureza-domesticada", ano="2002",
 titulo=dict(pt="Natureza Domesticada", en="Tamed Nature"),
 onde=dict(pt="CAM, Fundação Calouste Gulbenkian, Lisboa, 2002", en="CAM, Fundação Calouste Gulbenkian, Lisbon, 2002"),
 texto=dict(
  pt=["<cite>Natureza Domesticada</cite> desenvolvia a ideia de kit de sobrevivência para o citadino que sente falta de um passeio no campo. A exposição era composta por dez instalações que funcionavam como pequenos cenários alusivos ao jardim e a ambientes domésticos, e propunham a ideia de paisagens a ser habitadas pelo corpo. A ideia central da exposição era a convicção de que a nossa experiência da natureza é sempre artificial.",
      "As esculturas/instalações desta série são criadas a partir da ideia de tecido camuflado. O camuflado é uma forma abstracta, reduzida a uma paleta de quatro cores, de representação da natureza a duas dimensões. A paleta e as formas deste tecido foram o ponto de partida para as construções tridimensionais.",
      "Técnica mista, tecido, madeira, metal, feltro e tinta acrílica. Dimensões variáveis."],
  en=["This project investigates the way we relate to nature in urban environments. <cite>Tamed Nature</cite> is a group of constructions that play with the idea of nature as a consumable item. These constructions of artificial nature combine the city dweller's desire to be close to the wilderness and his need for physical comfort.",
      "Fabric, carpet, acrylic paint, styrofoam, wood, variable dimensions."]),
 textos=["natureza-domesticada"],
 imagens=[
  ("wp/2017/09/sc2002_view1_v2.jpg", "Vista da exposição <cite>Natureza Domesticada</cite>, CAM, Fundação Calouste Gulbenkian, Lisboa, 2002.", "Installation view, <cite>Tamed Nature</cite>, CAM, Fundação Calouste Gulbenkian, Lisbon, 2002.", None),
  ("wp/2017/09/sc2002_view2_v2.jpg", "Vista da exposição <cite>Natureza Domesticada</cite>, CAM, Fundação Calouste Gulbenkian, Lisboa, 2002.", "Installation view, <cite>Tamed Nature</cite>, CAM, Fundação Calouste Gulbenkian, Lisbon, 2002.", None),
  ("wp/2017/09/sc2002_view4_v2.jpg", "Vista da exposição <cite>Natureza Domesticada</cite>, CAM, Fundação Calouste Gulbenkian, Lisboa, 2002.", "Installation view, <cite>Tamed Nature</cite>, CAM, Fundação Calouste Gulbenkian, Lisbon, 2002.", None),
  ("wp/2017/09/sc2002_view3_v2.jpg", "Desenhos <cite>Natureza Domesticada</cite>, 2001–2002.", "<cite>Tamed Nature</cite> drawings, 2001–2002.", None),
  ("wp/2017/09/sc2002_010_v3.jpg", "<cite>Treescape</cite>, 2002.", "<cite>Treescape</cite>, 2002.", None),
  ("wp/2017/09/sc2002_007_v3.jpg", "<cite>Landscape</cite>, 2002.", "<cite>Landscape</cite>, 2002.", None),
  ("wp/2017/09/sc2002_002bb.jpg", "<cite>Shopping</cite>, 2002.", "<cite>Shopping</cite>, 2002.", None),
  ("wp/2017/09/sc2002_001_v3a.jpg", "<cite>Immaculate Forest</cite>, 2002.", "<cite>Immaculate Forest</cite>, 2002.", None),
  ("wp/2017/09/sc2002_004_v4.jpg", "<cite>Comfortable Jungle</cite>, 2002.", "<cite>Comfortable Jungle</cite>, 2002.", None),
  ("wp/2017/09/sc2002_006_v3.jpg", "<cite>Trip to the Country</cite>, 2002.", "<cite>Trip to the Country</cite>, 2002.", None),
  ("wp/2017/09/sc2002_002_d.jpg", "<cite>Shopping</cite>, pormenor.", "<cite>Shopping</cite>, detail.", None),
  ("wp/2017/09/sc2002_009_v2.jpg", "<cite>Table</cite>, 2002.", "<cite>Table</cite>, 2002.", None),
  ("wp/2017/09/sc2002_005_ar_v1.jpg", "<cite>Accessory</cite>. Vista na Andrea Rosen Gallery, Nova Iorque, 2002–03.", "<cite>Accessory</cite>. View at Andrea Rosen Gallery, New York, 2002–03.", None),
  ("wp/2017/09/2002_ar-v2-2007.jpg", "<cite>Natureza Domesticada</cite>. Vista na Andrea Rosen Gallery, Nova Iorque, 2002–03.", "<cite>Tamed Nature</cite>. View at Andrea Rosen Gallery, New York, 2002–03.", None),
  ("wp/2017/09/2002-cam-nd_003.jpg", "<cite>Private Garden</cite>, 2002.", "<cite>Private Garden</cite>, 2002.", None),
  ("wp/2017/09/sc2002_008_v2.jpg", "<cite>Portable Mattress</cite>, 2002.", "<cite>Portable Mattress</cite>, 2002.", None),
  ("wp/2020/06/2002-ND-Catalogo.jpg", "Catálogo da exposição, CAM, Fundação Calouste Gulbenkian, 2002.", "Exhibition catalogue, CAM, Fundação Calouste Gulbenkian, 2002.", None),
 ],
 rever=["títulos das obras ficam em inglês, como no site antigo: tinham títulos em português na exposição de 2002?"],
),

# ------------------------------------------------------------------
dict(
 slug="ard", ano="2000–01",
 titulo=dict(pt="A.R.D. (Artificial Retreat Devices)", en="A.R.D. (Artificial Retreat Devices)"),
 grelha=dict(pt="Artificial Retreat Devices", en="Artificial Retreat Devices"),
 onde=dict(pt="Colecção Berardo – Sintra Museu de Arte Moderna, 2001", en="Colecção Berardo – Sintra Museu de Arte Moderna, 2001"),
 texto=dict(
  pt=["<cite>A.R.D. (Artificial Retreat Devices)</cite> é uma instalação constituída por uma série de tendas portáteis, utilizadas para tranquilizar o desejo de escapar ao meio urbano. Estes abrigos portáteis podem ser montados e colocados em qualquer sítio, interior ou exterior. Assim que se entre neles, proporcionam um espaço de refúgio. O ambiente cromático e sonoro de cada tenda evoca diferentes associações com a natureza, permitindo que o espectador se sinta noutro lugar.",
      "A série, 2000–2001, um conjunto de cinco tendas feitas em camadas de tecidos de nylon, com interiores pintados com tinta acrílica em camadas translúcidas, oferece pequenos retiros para o corpo experienciar uma versão artificial da natureza. Um livro de instruções com a descrição do projecto indica as possíveis utilizações de cada tenda, como montar e em que género de situação. Um outro livro, edição de autor, com o título <cite>Livro de Projectos</cite>, contém também as instruções e possíveis utilizações, assim como uma série de desenhos de projecto para outras tendas com funções variadas."],
  en=["<cite>A.R.D. (Artificial Retreat Devices)</cite> is a series of portable tents that are used to pacify the desire to get out of the urban environment. These portable shelters could be mounted and placed anywhere indoors or outdoors. Once inside, they provide a place for seclusion. Through color and sound each tent recalls a different association with nature, allowing the viewer to be somewhere else.",
      "<cite>LazydressTent</cite>, <cite>ForestTent</cite>, <cite>CamouflageTent</cite>, <cite>OceanTent</cite>, 2001, with an instructions book and the <cite>Book of A.R.D. Projects</cite>. Installation with sound: fabric, metal, artificial grass."]),
 imagens=[
  ("wp/2017/09/2001_000.jpg", "<cite>A.R.D.</cite>, vista da exposição na Colecção Berardo – Sintra Museu de Arte Moderna, 2001.", "<cite>A.R.D.</cite>, installation view, Colecção Berardo – Sintra Museu de Arte Moderna, 2001.", None),
  ("wp/2017/09/2001_004a.jpg", "<cite>A.R.D. (Artificial Retreat Devices)</cite>, 2001.", "<cite>A.R.D. (Artificial Retreat Devices)</cite>, 2001.", None),
  ("wp/2017/09/2001_001.jpg", "<cite>A.R.D.</cite>, vista da exposição na Colecção Berardo – Sintra Museu de Arte Moderna, 2001.", "<cite>A.R.D.</cite>, installation view, Colecção Berardo – Sintra Museu de Arte Moderna, 2001.", None),
  ("wp/2017/09/2001_002.jpg", "<cite>A.R.D. (Artificial Retreat Devices)</cite>, 2001.", "<cite>A.R.D. (Artificial Retreat Devices)</cite>, 2001.", None),
  ("wp/2017/09/2001_017_v1.jpg", "<cite>A.R.D. (Artificial Retreat Devices)</cite>, 2001.", "<cite>A.R.D. (Artificial Retreat Devices)</cite>, 2001.", None),
  ("wp/2017/09/2001_015.jpg", "<cite>A.R.D. (Artificial Retreat Devices)</cite>, 2001.", "<cite>A.R.D. (Artificial Retreat Devices)</cite>, 2001.", None),
 ],
 rever=["o texto EN diz quatro tendas pelo nome; o PT diz cinco"],
),
]

BIBLIOTECA = dict(
 url="https://bibliotecanatural.catarinaleitao.net/",
 titulo=dict(pt="A Biblioteca Natural", en="The Natural Library"),
 ano="2014–",
 capa="wp/2020/05/DSF4632.jpg",
 nota=dict(pt="Sítio próprio", en="Separate site"),
)

# Textos longos do site antigo: chave -> (títulos do WordPress em PT e EN, autor)
TEXTOS = {
 "systema-naturae": dict(pt="Systema Naturæ (PT)", en="Systema Naturæ (EN)", autor="Catarina Leitão",
                         titulo=dict(pt="Systema Naturæ", en="Systema Naturæ")),
 "roseira-gabinete": dict(pt="Gabinete (PT)", en="Cabinet (EN)", autor="José Roseira",
                          titulo=dict(pt="Gabinete", en="Cabinet")),
 "dendrograma-pt": dict(pt="Texto Dendrograma (PT)", en=None, autor="Catarina Leitão",
                        titulo=dict(pt="Dendrograma | Tree-kit", en="Dendrograma | Tree-kit")),
 "dendrogram-mini": dict(pt=None, en="Dendrogram Mini Version (EN)", autor="Catarina Leitão",
                         titulo=dict(pt="Dendrogram | Tree-kit (Mini Version)", en="Dendrogram | Tree-kit (Mini Version)")),
 "natureza-domesticada": dict(pt="Natureza Domesticada (PT)", en="Tamed Nature (EN)", autor="Catarina Leitão",
                              titulo=dict(pt="Natureza Domesticada", en="Tamed Nature")),
 "uplift-en": dict(pt=None, en="Uplift (EN)", autor="Catarina Leitão", titulo=dict(pt="Uplift", en="Uplift")),
 "mdmf-orografias": dict(pt="Cadernos de campo e contracampo por Maria do Mar Fazenda", en="Field and counter-field by Maria do Mar Fazenda",
                         autor="Maria do Mar Fazenda", titulo=dict(pt="Cadernos de campo e contracampo", en="Field and Counter-Field Notebooks")),
 "lambert-caixa": dict(pt="Caixa de Desenho + Biblioteca Natural II (PT)", en=None, autor="Maria de Fátima Lambert",
                       titulo=dict(pt="Catarina Leitão na Quase Galeria e no Museu Nacional Soares dos Reis", en="Catarina Leitão na Quase Galeria e no Museu Nacional Soares dos Reis")),
 "roseira-paisagem": dict(pt="id:1310", en=None, autor="José Roseira",
                          titulo=dict(pt="Paisagem Instável", en="Paisagem Instável")),
 "fale-2019": dict(pt="Texto de Laura Sequeira Flalé", en="Text by Laura Sequeira Falé", autor="Laura Sequeira Falé",
                   titulo=dict(pt="Catarina Leitão", en="Catarina Leitão")),
}
