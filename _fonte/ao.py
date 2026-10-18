# Conversão para o Acordo Ortográfico de 1990 (português europeu).
# Não mexe no que está dentro de <cite>…</cite> ou <em>…</em> (títulos de obras, exposições, publicações)
# nem nos nomes próprios da lista PROTEGIDOS.
import re

PROTEGIDOS = ["Museu da Electricidade"]

REGRAS = [
    (r"\b([Pp]roj|[Oo]bj|[Tt]raj)ect", r"\1et"),
    (r"\b([Aa])ct(o|os|ual|uais|ualmente|ualidade|uar|ua|uam|uando|uação|ivo|iva|ivos|ivas|ividade|ividades|or|ores|riz)\b", r"\1t\2"),
    (r"\b([Aa])cç(ão|ões)\b", r"\1ç\2"),
    (r"([Cc]ole)c(ção|ções)", r"\1\2"),
    (r"([Cc]ole)ct(iv)", r"\1t\2"),
    (r"([Dd]ire)c(ção|ções)", r"\1\2"),
    (r"([Dd]ire)ct(or|ora|ores|oras|amente)\b", r"\1t\2"),
    (r"([Pp]rote)c(ção|ções)", r"\1\2"),
    (r"([Ss]ele)c(ção|ções|cion)", r"\1\2"),
    (r"([Ll]e)c(cion)", r"\1\2"),
    (r"\b([Ee]le)ct(r)", r"\1t\2"),
    (r"([Aa]rquite)ct", r"\1t"),
    (r"([Dd]idá)ct", r"\1t"),
    (r"([Aa]bstra)ct", r"\1t"),
    (r"\b([Ee]xa)ct", r"\1t"),
    (r"([Aa]spe)ct", r"\1t"),
    (r"([Pp]erspe)ct", r"\1t"),
    (r"([Ee]spe)ct(ador|adores|adora|adoras)\b", r"\1t\2"),
    (r"([Mm]anufa)ct", r"\1t"),
    (r"\b([Óó])ptim", lambda m: ("Ó" if m.group(1) == "Ó" else "ó") + "tim"),
    (r"\b([Ee]fe)ct(iv|u)", r"\1t\2"),
    (r"\b([Aa]fe)ct", r"\1t"),
    (r"([Ii]nfe)cç", r"\1ç"),
    (r"([Rr]eda)cç", r"\1ç"),
    (r"\b([Ss]e)ct(or|ores)\b", r"\1t\2"),
    (r"\b([Tt]a)ct(e)", r"\1t\2"),
    (r"\b([Ee]xce)p([çt])", r"\1\2"),
    (r"\b([Rr]ece)p(ç|t)", r"\1\2"),
    (r"\b([Aa]do)p(ç|t)", r"\1\2"),
    (r"([Ii]ntera)cç", r"\1ç"),
    (r"[Pp]ára-quedas", "paraquedas"),
    (r"\b([Aa])ctiv", r"\1tiv"),
    (r"([Aa]tra)cç", r"\1ç"),
    (r"\b([Jj]a)cto", r"\1to"),
    (r"([Rr]efle)ct", r"\1t"),
    (r"([Ee]spe)ctácul", r"\1tácul"),
    (r"\b([Óó])ptic", lambda m: ("Ó" if m.group(1) == "Ó" else "ó") + "tic"),
    (r"([Pp]roje)cç", r"\1ç"),
    (r"([Dd]ialé)ct", r"\1t"),
]

MESES = "Janeiro|Fevereiro|Março|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro|Primavera|Verão|Outono|Inverno"

def _converter(t):
    for a, b in REGRAS:
        t = re.sub(a, b, t)
    # meses e estações em minúscula, exceto no início de frase
    def mes(m):
        antes = t[:m.start()].rstrip()
        if not antes or antes[-1] in ".!?>":
            return m.group(1)
        return m.group(1).lower()
    return re.sub(rf"\b({MESES})\b", mes, t)

def ao(texto):
    if not texto:
        return texto
    guardados = []
    def guarda(m):
        guardados.append(m.group(0))
        return f"\x00{len(guardados) - 1}\x00"
    t = re.sub(r"<(cite|em|i)\b[^>]*>.*?</\1>", guarda, texto, flags=re.S)
    for p in PROTEGIDOS:
        t = re.sub(re.escape(p), guarda, t)
    t = _converter(t)
    return re.sub(r"\x00(\d+)\x00", lambda m: guardados[int(m.group(1))], t)

if __name__ == "__main__":
    for s in ["O projecto e os objectos da colecção, em Outubro.", "Outubro de 2026", "a <cite>Os Personagens, os Objectos</cite> actual",
              "Museu da Electricidade e electricidade", "acções e acto performativo; espectador; óptimo; pára-quedas; lecciona; direcção; director",
              "No Verão de 2023 o projecto", "aspecto, perspectiva, exacto, abstracta, didáctica, manufacturado, arquitectura, protecção, selecção, interacção, adoptar, excepção, recepção"]:
        print(ao(s))
