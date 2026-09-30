#!/usr/bin/env python3
"""Gera o site estático catarinaleitao.net a partir de conteudo.py e agora.py.

Uso:  python3 _fonte/gerar.py FONTES
FONTES é a pasta com as imagens de origem, com as subpastas:
  up/  (uploads do WordPress)   drive/  (pastas do Drive)   extra/  (enviadas à parte)
e wp.db (base de dados do WordPress convertida), para os textos longos.

A pasta _fonte não é publicada pelo GitHub Pages (pastas começadas por _ são ignoradas).
"""
import sys, os, re, html, shutil, sqlite3
from pathlib import Path
from PIL import Image, ImageOps

sys.path.insert(0, str(Path(__file__).parent))
from conteudo import PROJECTOS, BIBLIOTECA, TEXTOS
from agora import AGORA
from info import BIO
import csv

RAIZ = Path(__file__).resolve().parent.parent
FONTES = Path(sys.argv[1]) if len(sys.argv) > 1 else None
ORIGEM = {"wp": "up", "dr": "drive", "ex": "extra"}
SITE = "https://catarinaleitao.net/"
NEWSLETTER = ("https://3a310a7f.sibforms.com/serve/MUIFAE-RLhQTq2ZnutSho_4_0akkCtrH4k1OQ_PVg3yOGPbcQlfz-vGFN_Q3_-69cvJvuC45S8hj4P92rDoXSg7QYUDWgnfu_GDlk0jERygKRdD3dyaj5crF-9u5v9q0-GHZMXX39-mhK-FXidHqJwk_LjlyDK7E8jW-2esy5Xe_pkefBy7wi_6RF1KuUuFVBIOaIqw9602N6DO-nQ==")

T = {  # textos da interface
 "pt": dict(lang="pt-PT", projectos="Projectos", agora="Agora", outra="EN", outra_nome="English",
            saltar="Saltar para o conteúdo", textos="Textos", video="Vídeo", foto="Fotografia",
            anterior="Anterior", seguinte="Seguinte", todos="Todos os projectos", de="de",
            so_en="Este texto existe só em inglês.", so_pt="Este texto existe só em português.",
            voltar="Voltar a", descricao="Catarina Leitão, artista plástica. Escultura, desenho, instalação e livros de artista.",
            contactos="Contactos", newsletter="Subscrever a newsletter", nao_encontrada="Página não encontrada",
            nao_encontrada_txt="O endereço pode ter mudado com a reconstrução do sítio.",
            info="Info", imprensa="Imprensa", entrevistas="Entrevistas", publicacoes="Publicações", bio="Biografia",
            cv="Curriculum vitae", cv_pt="CV em português", cv_en="CV em inglês", sem_projecto="Sem página de projecto",
            textos_expo="Textos", projecto="Projecto"),
 "en": dict(lang="en", projectos="Projects", agora="Now", outra="PT", outra_nome="Português",
            saltar="Skip to content", textos="Texts", video="Video", foto="Photo",
            anterior="Previous", seguinte="Next", todos="All projects", de="by",
            so_en="This text exists in English only.", so_pt="This text exists in Portuguese only.",
            voltar="Back to", descricao="Catarina Leitão, visual artist. Sculpture, drawing, installation and artist's books.",
            contactos="Contact", newsletter="Subscribe to the newsletter", nao_encontrada="Page not found",
            nao_encontrada_txt="The address may have changed while the site was rebuilt.",
            info="Info", imprensa="Press", entrevistas="Interviews", publicacoes="Publications", bio="Biography",
            cv="Curriculum vitae", cv_pt="CV in Portuguese", cv_en="CV in English", sem_projecto="No project page",
            textos_expo="Texts", projecto="Project"),
}

def caminho(lingua, tipo, slug=""):
    """Caminho relativo à raiz, sem barra inicial."""
    if lingua == "pt":
        base = {"inicio": "", "agora": "agora/", "info": "info/", "projecto": "projectos/", "texto": "textos/"}[tipo]
    else:
        base = {"inicio": "en/", "agora": "en/now/", "info": "en/info/", "projecto": "en/projects/", "texto": "en/texts/"}[tipo]
    r = base + (slug + "/" if slug else "")
    if r == "" or r.endswith("/"):
        r += "index.html"  # ligações explícitas: funcionam também abrindo os ficheiros no computador
    return r

def limpo(rel):
    """Endereço público sem index.html, para o canonical."""
    return rel[:-len("index.html")] if rel.endswith("index.html") else rel

def raiz_de(rel):
    return "../" * rel.count("/")

def limpar_texto(s):
    return re.sub(r"<[^>]+>", "", s)

# ---------------------------------------------------------------- imagens

def processar_imagem(origem, destino_base):
    """Gera duas larguras (1200 e 2000) e devolve (largura, altura) da maior."""
    pref, resto = origem.split("/", 1)
    src = FONTES / ORIGEM[pref] / resto
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    saidas = {}
    for lado, sufixo, q in [(2000, "", 82), (1200, "-m", 80)]:
        c = im.copy(); c.thumbnail((lado, lado), Image.LANCZOS)
        p = RAIZ / f"{destino_base}{sufixo}.jpg"
        p.parent.mkdir(parents=True, exist_ok=True)
        c.save(p, "JPEG", quality=q, optimize=True, progressive=True)
        saidas[sufixo] = c.size
    return saidas[""], saidas["-m"]

def processar_capa(origem, destino):
    pref, resto = origem.split("/", 1)
    im = ImageOps.exif_transpose(Image.open(FONTES / ORIGEM[pref] / resto)).convert("RGB")
    im = ImageOps.fit(im, (800, 800), Image.LANCZOS)
    p = RAIZ / destino; p.parent.mkdir(parents=True, exist_ok=True)
    im.save(p, "JPEG", quality=80, optimize=True, progressive=True)

# ---------------------------------------------------------------- moldura

def pagina(lingua, rel, titulo, corpo, outra_rel, descricao=None, imagem_og=None, actual=None):
    t = T[lingua]; r = raiz_de(rel)
    outra_lingua = "en" if lingua == "pt" else "pt"
    nav_proj = ' aria-current="page"' if actual == "projectos" else ""
    nav_agora = ' aria-current="page"' if actual == "agora" else ""
    nav_info = ' aria-current="page"' if actual == "info" else ""
    titulo_doc = "Catarina Leitão" if not titulo else f"{limpar_texto(titulo)} · Catarina Leitão"
    desc = html.escape(descricao or t["descricao"], quote=True)
    og_img = f'\n  <meta property="og:image" content="{SITE}{imagem_og}">' if imagem_og else ""
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{html.escape(titulo_doc)}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{SITE}{limpo(rel)}">
  <link rel="alternate" hreflang="pt" href="{SITE}{limpo(rel if lingua == 'pt' else outra_rel)}">
  <link rel="alternate" hreflang="en" href="{SITE}{limpo(rel if lingua == 'en' else outra_rel)}">
  <meta property="og:title" content="{html.escape(titulo_doc, quote=True)}">
  <meta property="og:description" content="{desc}">{og_img}
  <meta property="og:type" content="website">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:ital,wght@0,400;0,500;0,600;1,400&display=swap">
  <link rel="stylesheet" href="{r}css/site.css">
</head>
<body>
<a class="saltar" href="#conteudo">{t['saltar']}</a>
<header class="cabecalho">
  <a class="nome" href="{r}{caminho(lingua, 'inicio')}">Catarina Leitão</a>
  <nav class="navegacao" aria-label="{t['projectos']}">
    <ul>
      <li><a href="{r}{caminho(lingua, 'inicio')}"{nav_proj}>{t['projectos']}</a></li>
      <li><a href="{r}{caminho(lingua, 'agora')}"{nav_agora}>{t['agora']}</a></li>
      <li><a href="{r}{caminho(lingua, 'info')}"{nav_info}>{t['info']}</a></li>
      <li><a class="lingua" href="{r}{outra_rel}" hreflang="{outra_lingua}" lang="{outra_lingua}" title="{t['outra_nome']}">{t['outra']}</a></li>
    </ul>
  </nav>
</header>
<main id="conteudo">
{corpo}
</main>
<footer class="rodape">
  <h2 class="visualmente-oculto">{t['contactos']}</h2>
  <ul class="contactos">
    <li><a href="mailto:c@catarinaleitao.net">c@catarinaleitao.net</a></li>
    <li><a href="https://www.instagram.com/cataleitao/">Instagram</a></li>
    <li><a href="{NEWSLETTER}">{t['newsletter']}</a></li>
  </ul>
  <p>© Catarina Leitão</p>
</footer>
</body>
</html>
"""

def escrever(rel, conteudo):
    p = RAIZ / (rel + "index.html" if rel.endswith("/") or rel == "" else rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(conteudo, encoding="utf-8")

# ---------------------------------------------------------------- textos longos (WordPress)

def texto_wp(db, titulo_post):
    if str(titulo_post).startswith("id:"):  # quando há títulos repetidos no WordPress
        row = db.execute("select post_content from wpxh_posts where ID=?", (titulo_post[3:],)).fetchone()
    else:
        row = db.execute("select post_content from wpxh_posts where post_title=? and post_status='publish' and post_type='post'",
                         (titulo_post,)).fetchone()
    c = row[0]
    c = re.sub(r"<!--.*?-->", "", c, flags=re.S)
    c = re.sub(r"\[/?[a-z_]+[^\]]*\]", "", c)
    # tirar ligações para o site antigo, manter as externas
    c = re.sub(r'<a [^>]*href="https?://(www\.)?catarinaleitao\.(net|wordpress\.com)[^"]*"[^>]*>(.*?)</a>', r"\3", c, flags=re.S)
    c = re.sub(r"<(/?)(h\d)[^>]*>", lambda m: f"<{m.group(1)}h3>", c)
    permitidas = {"p", "em", "strong", "i", "b", "a", "br", "sup", "blockquote", "h3", "ul", "ol", "li"}
    def filtra(m):
        fecho, nome, attrs = m.group(1), m.group(2).lower(), m.group(3)
        if nome not in permitidas: return ""
        if nome == "a" and not fecho:
            h = re.search(r'href="([^"]+)"', attrs)
            return f'<a href="{h.group(1)}">' if h else "<a>"
        return f"<{fecho}{nome}>"
    c = re.sub(r"<(/?)([a-zA-Z0-9]+)([^>]*)>", filtra, c)
    # parágrafos à maneira do WordPress
    blocos = [b.strip() for b in re.split(r"\n\s*\n", c) if b.strip()]
    saida = []
    for b in blocos:
        if re.match(r"^<(p|h3|blockquote|ul|ol)>", b): saida.append(b)
        else: saida.append("<p>" + b.replace("\n", "<br>\n") + "</p>")
    if saida and re.match(r"^<p>(por|by) [^<]{3,60}</p>$", saida[0]):
        saida = saida[1:]  # o autor já aparece por baixo do título
    return "\n".join(saida)

# ---------------------------------------------------------------- documentos (textos, imprensa, publicações)

def ler_documentos():
    docs = list(csv.DictReader(open(Path(__file__).parent / "documentos.csv", encoding="utf-8")))
    for d in docs:
        d["ficheiros"] = [x.strip() for x in d["ficheiros"].split(";") if x.strip()]
        d["projectos"] = [x.strip() for x in d["projectos"].split(";") if x.strip()]
        anos = re.findall(r"(?:19|20)\d\d", d["data"]); ano = int(anos[-1]) if anos else 0
        mes = re.search(r"(\d{1,2})(?:-\d{1,2})?\.(?:19|20)\d\d", d["data"])
        dia = re.match(r"(\d{1,2})\.\d{1,2}\.", d["data"])
        d["ordem"] = (ano, int(mes.group(1)) if mes else 0, int(dia.group(1)) if dia else 0)
    return docs

def item_documento(d, lingua, r, com_projecto=False):
    t = T[lingua]
    titulo = html.escape(d.get("titulo_en") if lingua == "en" and d.get("titulo_en") else d["titulo"])
    extra = ""
    if d["pagina"]:
        a = f'<a href="{r}{caminho(lingua, "texto", d["pagina"])}">{titulo}</a>'
    elif d["ficheiros"]:
        a = f'<a href="{r}docs/{d["ficheiros"][0]}" target="_blank" rel="noopener">{titulo}</a>'
        if len(d["ficheiros"]) > 1:
            rotulos = [re.search(r"-(PT|EN)-", f).group(1) if re.search(r"-(PT|EN)-", f) else str(k + 1) for k, f in enumerate(d["ficheiros"])]
            extra = " " + " · ".join(f'<a href="{r}docs/{f}" target="_blank" rel="noopener">{rot}</a>' for f, rot in zip(d["ficheiros"], rotulos))
    elif d["link"]:
        a = f'<a href="{html.escape(d["link"], quote=True)}" target="_blank" rel="noopener">{titulo}</a>'
    else:
        a = f"<span>{titulo}</span>"
    partes = [x for x in [d["autor"], html.escape(d["onde"]), d["data"]] if x]
    marca = " (PDF)" if d["ficheiros"] and not d["pagina"] else (" ↗" if d["link"] and not d["pagina"] and not d["ficheiros"] else "")
    if d["lingua"]: partes.append(d["lingua"])
    if d.get("ref_" + lingua):  # entradas bibliográficas do CV: a referência completa, tal como no CV
        partes = [html.escape(d["ref_" + lingua])]
    proj = ""
    if com_projecto:
        nomes = [pp["titulo"][lingua] for pp in PROJECTOS if pp["slug"] in d["projectos"]]
        if nomes:
            proj = " · " + ", ".join(f'<a href="{r}{caminho(lingua, "projecto", pp["slug"])}">{pp["titulo"][lingua]}</a>' for pp in PROJECTOS if pp["slug"] in d["projectos"])
    return f'<li>{a}{marca}{extra}<span class="detalhe">{" · ".join(partes)}{proj}</span></li>'

# ---------------------------------------------------------------- páginas

def gerar():
    # limpar o que é gerado
    for d in ["projectos", "textos", "agora", "en", "img/p", "docs"]:
        shutil.rmtree(RAIZ / d, ignore_errors=True)

    db = sqlite3.connect(FONTES / "wp.db")
    dados = []  # por projecto: imagens processadas
    for p in PROJECTOS:
        imgs = []
        for n, (orig, lpt, len_, foto) in enumerate(p["imagens"], 1):
            base = f"img/p/{p['slug']}/{n:02d}"
            (w, h), (wm, hm) = processar_imagem(orig, base)
            imgs.append(dict(base=base, w=w, h=h, wm=wm, hm=hm, pt=lpt, en=len_, foto=foto))
        capa = p.get("capa", p["imagens"][0][0])
        processar_capa(capa, f"img/p/{p['slug']}/capa.jpg")
        for orig, dest in p.get("docs", []):
            pref, resto = orig.split("/", 1)
            (RAIZ / dest).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(FONTES / ORIGEM[pref] / resto, RAIZ / dest)
        dados.append(imgs)
    processar_capa(BIBLIOTECA["capa"], "img/p/biblioteca-natural-capa.jpg")

    DOCS = ler_documentos()
    (RAIZ / "docs").mkdir(exist_ok=True)
    for d in DOCS:
        for f in d["ficheiros"]:
            shutil.copy(FONTES / "docs_src" / f, RAIZ / "docs" / f)

    for lingua in ["pt", "en"]:
        t = T[lingua]; outra = "en" if lingua == "pt" else "pt"

        # --- entrada: grelha
        rel = caminho(lingua, "inicio"); r = raiz_de(rel)
        itens = []
        for p in PROJECTOS:
            nome = p.get("grelha", p["titulo"])[lingua]
            itens.append(f'''  <li><a href="{r}{caminho(lingua, 'projecto', p['slug'])}">
    <img src="{r}img/p/{p['slug']}/capa.jpg" width="800" height="800" alt="" loading="lazy">
    <span class="titulo">{html.escape(nome)}</span>
    <span class="ano">{p['ano']}</span>
  </a></li>''')
        b = BIBLIOTECA
        itens.insert(8, f'''  <li><a href="{b['url']}">
    <img src="{r}img/p/biblioteca-natural-capa.jpg" width="800" height="800" alt="" loading="lazy">
    <span class="titulo">{b['titulo'][lingua]}</span>
    <span class="ano">{b['ano']}</span>
    <span class="externo">{b['nota'][lingua]} ↗</span>
  </a></li>''')
        corpo = f'''<section class="indice" aria-labelledby="t-projectos">
<h1 id="t-projectos" class="visualmente-oculto">{t['projectos']}</h1>
<ul class="grelha">
{chr(10).join(itens)}
</ul>
</section>'''
        escrever(rel, pagina(lingua, rel, "", corpo, caminho(outra, "inicio"),
                             imagem_og=f"img/p/{PROJECTOS[0]['slug']}/01.jpg", actual="projectos"))

        # --- agora
        rel = caminho(lingua, "agora")
        corpo = f'<div class="capa">{AGORA[lingua].replace("{raiz}", raiz_de(rel))}</div>'
        escrever(rel, pagina(lingua, rel, t["agora"], corpo, caminho(outra, "agora"), actual="agora"))

        # --- info
        rel = caminho(lingua, "info"); r = raiz_de(rel)
        seccoes = []
        cvs = [d for d in DOCS if d["subtipo"] == "CV"]
        cv_links = ""
        if cvs:
            fs = cvs[0]["ficheiros"]
            cv_links = "".join(f'<li><a href="{r}docs/{f}" target="_blank" rel="noopener">{t["cv_pt"] if "-PT-" in f else t["cv_en"]}</a> (PDF)<span class="detalhe">{cvs[0]["data"]}</span></li>' for f in fs)
        bio = "".join(f"<p>{x}</p>" for x in BIO[lingua])
        seccoes.append(f'<section id="bio"><h2>{t["bio"]}</h2><div class="sinopse">{bio}</div></section>')
        if cv_links:
            seccoes.append(f'<section id="cv"><h2>{t["cv"]}</h2><ul class="lista">{cv_links}</ul></section>')
        grupos = [("textos", t["textos_expo"], "texto de exposição"), ("imprensa", t["imprensa"], "crítica"),
                  ("entrevistas", t["entrevistas"], "entrevista"), ("publicacoes", t["publicacoes"], "publicação")]
        for ancora, nome, cat in grupos:
            ds = sorted([d for d in DOCS if d["categoria"] == cat and d["subtipo"] != "CV"], key=lambda d: d["ordem"], reverse=True)
            if ds:
                seccoes.append(f'<section id="{ancora}"><h2>{nome}</h2><ul class="lista">{"".join(item_documento(d, lingua, r, True) for d in ds)}</ul></section>')
        corpo = f'<div class="info"><h1 class="visualmente-oculto">{t["info"]}</h1>{"".join(seccoes)}</div>'
        escrever(rel, pagina(lingua, rel, t["info"], corpo, caminho(outra, "info"), actual="info"))

        # --- projectos
        for i, (p, imgs) in enumerate(zip(PROJECTOS, dados)):
            rel = caminho(lingua, "projecto", p["slug"]); r = raiz_de(rel)
            figs = []; lado = 0
            for k, im in enumerate(imgs):
                vertical = im["h"] > im["w"] * 1.1
                cls = ""
                if vertical:
                    cls = ' class="vertical direita"' if lado % 2 else ' class="vertical"'; lado += 1
                foto = f' {t["foto"]}: {im["foto"]}.' if im["foto"] else ""
                carregar = "" if k == 0 else ' loading="lazy"'
                alt = html.escape(limpar_texto(im[lingua]), quote=True)
                figs.append(f'''<figure{cls}>
  <img src="{r}{im['base']}-m.jpg" srcset="{r}{im['base']}-m.jpg {im['wm']}w, {r}{im['base']}.jpg {im['w']}w"
       sizes="(min-width: 60rem) 55vw, 100vw" width="{im['w']}" height="{im['h']}" alt="{alt}"{carregar}>
  <figcaption>{im[lingua]}{foto}</figcaption>
</figure>''')
            paragrafos = "\n".join(f"<p>{x.replace('{raiz}', r)}</p>" for x in p["texto"][lingua])
            onde = f'<p class="datas">{p["onde"][lingua]}</p>' if p["onde"][lingua] else f'<p class="datas">{p["ano"]}</p>'
            info = []
            meus = sorted([d for d in DOCS if p["slug"] in d["projectos"]], key=lambda d: d["ordem"], reverse=True)
            txt = [d for d in meus if d["categoria"] == "texto de exposição"]
            imp = [d for d in meus if d["categoria"] != "texto de exposição"]
            if txt:
                info.append(f'<section><h2>{t["textos_expo"]}</h2><ul class="lista">{"".join(item_documento(d, lingua, r) for d in txt)}</ul></section>')
            if imp:
                info.append(f'<section><h2>{t["imprensa"]}</h2><ul class="lista">{"".join(item_documento(d, lingua, r) for d in imp)}</ul></section>')
            if p.get("video"):
                v = p["video"]
                info.append(f'<section><h2>{t["video"]}</h2><ul class="lista"><li><a href="{v["url"]}">{v["url"].split("//")[1]}</a>'
                            f'<span class="detalhe">{v[lingua]}</span></li></ul></section>')
            ant = PROJECTOS[i - 1] if i > 0 else None
            seg = PROJECTOS[i + 1] if i + 1 < len(PROJECTOS) else None
            nav = '<nav class="entre-projetos" aria-label="' + t["projectos"] + '">'
            nav += (f'<a href="{r}{caminho(lingua, "projecto", ant["slug"])}"><span>{t["anterior"]}</span>{ant["titulo"][lingua]}</a>'
                    if ant else f'<a href="{r}{caminho(lingua, "inicio")}"><span>{t["voltar"]}</span>{t["todos"]}</a>')
            nav += (f'<a class="seguinte" href="{r}{caminho(lingua, "projecto", seg["slug"])}"><span>{t["seguinte"]}</span>{seg["titulo"][lingua]}</a>'
                    if seg else f'<a class="seguinte" href="{r}{caminho(lingua, "inicio")}"><span>{t["voltar"]}</span>{t["todos"]}</a>')
            nav += "</nav>"
            corpo = f'''<article class="projeto">
  <div class="projeto-intro">
    <h1>{p['titulo'][lingua]}</h1>
    {onde}
    <div class="sinopse">
{paragrafos}
    </div>
  </div>
  <div class="projeto-imagens">
{chr(10).join(figs)}
  </div>
  <div class="projeto-info">
{chr(10).join(info)}
  </div>
</article>
{nav}'''
            desc = limpar_texto(p["texto"][lingua][0])[:180]
            escrever(rel, pagina(lingua, rel, p["titulo"][lingua], corpo, caminho(outra, "projecto", p["slug"]),
                                 descricao=desc, imagem_og=imgs[0]["base"] + ".jpg", actual="projectos"))

        # --- textos longos
        for chave, tx in TEXTOS.items():
            rel = caminho(lingua, "texto", chave); r = raiz_de(rel)
            fonte_lingua = lingua if tx[lingua] else outra
            corpo_txt = texto_wp(db, tx[fonte_lingua])
            aviso = ""
            if fonte_lingua != lingua:
                aviso = f'<p class="aviso-lingua">{t["so_en"] if fonte_lingua == "en" else t["so_pt"]}</p>'
            slugs = {s for d in DOCS if d["pagina"] == chave for s in d["projectos"]}
            projectos = [p for p in PROJECTOS if p["slug"] in slugs]
            volta = "".join(f'<li><a href="{r}{caminho(lingua, "projecto", p["slug"])}">{p["titulo"][lingua]}</a></li>' for p in projectos)
            corpo = f'''<article class="texto" lang="{T[fonte_lingua]['lang']}">
  <h1>{tx['titulo'][fonte_lingua]}</h1>
  <p class="autor">{tx['autor']}</p>
  {aviso}
  <div class="texto-corpo">
{corpo_txt}
  </div>
  <ul class="lista volta" lang="{t['lang']}">{volta}</ul>
</article>'''
            escrever(rel, pagina(lingua, rel, tx["titulo"][fonte_lingua], corpo, caminho(outra, "texto", chave)))

    # --- 404 (bilingue)
    corpo = f'''<div class="capa"><h1>{T['pt']['nao_encontrada']}</h1><p class="descricao">{T['pt']['nao_encontrada_txt']}</p>
<p><a href="/index.html">{T['pt']['todos']}</a></p>
<div lang="en"><h2>{T['en']['nao_encontrada']}</h2><p>{T['en']['nao_encontrada_txt']} <a href="/en/index.html">{T['en']['todos']}</a></p></div></div>'''
    p404 = pagina("pt", "404.html", T["pt"]["nao_encontrada"], corpo, "en/index.html")
    p404 = re.sub(r'(href|src)="(?!https?:|mailto:|/|#)', r'\1="/', p404)  # a 404 pode aparecer em qualquer pasta
    (RAIZ / "404.html").write_text(p404, encoding="utf-8")

    print("feito:", len(PROJECTOS), "projectos,", sum(len(d) for d in dados), "imagens,", len(TEXTOS), "textos")

if __name__ == "__main__":
    if not FONTES:
        sys.exit(__doc__)
    gerar()
