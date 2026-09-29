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
            nao_encontrada_txt="O endereço pode ter mudado com a reconstrução do sítio."),
 "en": dict(lang="en", projectos="Projects", agora="Now", outra="PT", outra_nome="Português",
            saltar="Skip to content", textos="Texts", video="Video", foto="Photo",
            anterior="Previous", seguinte="Next", todos="All projects", de="by",
            so_en="This text exists in English only.", so_pt="This text exists in Portuguese only.",
            voltar="Back to", descricao="Catarina Leitão, visual artist. Sculpture, drawing, installation and artist's books.",
            contactos="Contact", newsletter="Subscribe to the newsletter", nao_encontrada="Page not found",
            nao_encontrada_txt="The address may have changed while the site was rebuilt."),
}

def caminho(lingua, tipo, slug=""):
    """Caminho relativo à raiz, sem barra inicial."""
    if lingua == "pt":
        base = {"inicio": "", "agora": "agora/", "projecto": "projectos/", "texto": "textos/"}[tipo]
    else:
        base = {"inicio": "en/", "agora": "en/now/", "projecto": "en/projects/", "texto": "en/texts/"}[tipo]
    r = base + (slug + "/" if slug else "")
    if os.environ.get("PREVISAO") and (r == "" or r.endswith("/")):
        r += "index.html"  # para ver o site fora de um servidor que resolva pastas
    return r

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
  <link rel="canonical" href="{SITE}{rel}">
  <link rel="alternate" hreflang="pt" href="{SITE}{rel if lingua == 'pt' else outra_rel}">
  <link rel="alternate" hreflang="en" href="{SITE}{rel if lingua == 'en' else outra_rel}">
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
    return "\n".join(saida)

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
            if p.get("textos"):
                li = []
                for chave in p["textos"]:
                    tx = TEXTOS[chave]
                    li.append(f'<li><a href="{r}{caminho(lingua, "texto", chave)}">{tx["titulo"][lingua]}</a>'
                              f'<span class="detalhe">{tx["autor"]}</span></li>')
                info.append(f'<section><h2>{t["textos"]}</h2><ul class="lista">{"".join(li)}</ul></section>')
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
            projectos = [p for p in PROJECTOS if chave in p.get("textos", [])]
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
<p><a href="/">{T['pt']['todos']}</a></p>
<div lang="en"><h2>{T['en']['nao_encontrada']}</h2><p>{T['en']['nao_encontrada_txt']} <a href="/en/">{T['en']['todos']}</a></p></div></div>'''
    (RAIZ / "404.html").write_text(pagina("pt", "404.html", T["pt"]["nao_encontrada"], corpo, "en/").replace('href="css/', 'href="/css/').replace('href="en/"', 'href="/en/"').replace('href="agora/"', 'href="/agora/"').replace('href=""', 'href="/"'), encoding="utf-8")

    print("feito:", len(PROJECTOS), "projectos,", sum(len(d) for d in dados), "imagens,", len(TEXTOS), "textos")

if __name__ == "__main__":
    if not FONTES:
        sys.exit(__doc__)
    gerar()
