import streamlit as st
import json

st.set_page_config(layout="wide")
st.title("🎲 Carreira de Analista de Dados")

# CSS para estilização refinada
st.markdown("""
<style>
/* Fonte maior para os nomes dos blocos */
div[data-testid="stExpander"] div[data-testid="stMarkdownContainer"] {
    font-size: 24px !important;
    font-weight: bold;
}

/* Subtítulos maiores */
h6 {
    font-size: 16px;
    margin-top: 20px;
    color: #444;
}

/* Estilo para o botão de curso */
.card-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin: 0 auto 8px auto;     /* centraliza e dá espaçamento vertical */
  padding: 12px;
  border-radius: 8px;
  border: 2px solid var(--primary-color);
  background-color: var(--secondary-background-color);
  transition: background 0.3s ease, transform 0.2s ease;
  text-decoration: none;
  color: inherit;
  height: 120px;
  justify-content: center;
  width: 100%;
  max-width: 220px;            /* aqui está o limite */
}
.card-link:hover {
  background-color: var(--primary-color);
  color: white;
  transform: scale(1.02);
}
.card-link img {
  margin-bottom: 8px;
  border-radius: 4px;
}
.card-text {
  font-size: 13px;
  font-weight: bold;
  line-height: 1.3;
}
.stack-title {
  text-align: center;
  font-weight: bold;
  margin-bottom: 10px;
  font-size: 15px;
  color: #444;
}
</style>
""", unsafe_allow_html=True)

# JSON da trilha
with open("trilha_analista_de_dados_v3.json", "r", encoding="utf-8") as f:
    trilha = json.load(f)

# Exibição
for etapa in trilha["ementa"]:
    if etapa['nivel'] == "Nivelamento":
        subnivel = ""
    else:
        subnivel = f" - {etapa['subnivel']}"

    if etapa['nivel'] == "Nivelamento":
        icone = "🟢"
        cores = "green"
    if etapa['nivel'] == "Iniciante":
        icone = "🟡"
        cores = "orange"
    if etapa['nivel'] == "Intermediário":
        icone = "🔵"
        cores = "blue"
    if etapa['nivel'] == "Avançado":
        icone = "🟣"
        cores = "violet"
        
    st.header(f":{cores}[{icone} {etapa['nivel']}{subnivel}]", divider=cores)
    for bloco in etapa["blocos_tematicos"]:
        with st.expander(f"## 📦 {bloco['nome']}"):
            st.markdown("##### 📝 Descrição")
            st.markdown(f"<p style='margin-left: 32px; font-size: 16px;'>{bloco['descricao']}</p>", unsafe_allow_html=True)

            st.markdown("##### 🎯 Projetos")
            for projeto in bloco.get("projetos", []):
                st.markdown(f"<p style='margin-left: 32px; font-size: 16px;'>🔹 {projeto}</p>", unsafe_allow_html=True)

            st.markdown("##### 🧠 Hard Skills")
            for skill in bloco.get("hard_skills", []):
                st.markdown(f"<p style='margin-left: 32px; font-size: 16px;'>🔹 {skill}</p>", unsafe_allow_html=True)

            st.markdown("##### 💬 Soft Skills")
            for skill in bloco.get("soft_skills", []):
                st.markdown(f"<p style='margin-left: 32px; font-size: 16px;'>🔹 {skill}</p>", unsafe_allow_html=True)

            st.markdown("##### 🛠 Ferramentas")
            for ferramenta in bloco.get("ferramentas_principais", []):
                st.markdown(f"<p style='margin-left: 32px; font-size: 16px;'>🔹 {ferramenta}</p>", unsafe_allow_html=True)

            cursos = bloco.get("cursos", [])
            if cursos:
                st.markdown("##### 🎓 Cursos Associados por Stack")
                cols = st.columns(len(cursos))
                for col, stack_entry in zip(cols, cursos):
                    with col:
                        st.markdown(f"<div class='stack-title'>{stack_entry['stack']}</div>", unsafe_allow_html=True)
                        for curso in stack_entry.get("cursos", []):
                            nome = curso.get("nome", "Curso sem nome")
                            link = curso.get("link", "")
                            status = curso.get("status", "").strip().upper()
                            badge_html = ""
                            if status == "NOVIDADE":
                                badge_html = "<div style='margin-top: 4px; padding: 2px 6px; background-color: yellow; color: black; border-radius: 4px; font-size: 10px;'>NOVIDADE</div>"
                            elif status == "REGRAVAÇÃO":
                                badge_html = "<div style='margin-top: 4px; padding: 2px 6px; background-color: red; color: white; border-radius: 4px; font-size: 10px;'>REGRAVAÇÃO</div>"
                            elif status == "CARREIRA":
                                badge_html = "<div style='margin-top: 4px; padding: 2px 6px; background-color: green; color: white; border-radius: 4px; font-size: 10px;'>CARREIRA</div>"
                            elif status == "COMPLEMENTO":
                                badge_html = "<div style='margin-top: 4px; padding: 2px 6px; background-color: orange; color: black; border-radius: 4px; font-size: 10px;'>COMPLEMENTO</div>"
                            elif status == "ATIVO":
                                badge_html = "<div style='margin-top: 4px; padding: 2px 6px; background-color: blue; color: white; border-radius: 4px; font-size: 10px;'>ATIVO</div>"
                            elif status == "SUGESTÃO":
                                badge_html = "<div style='margin-top: 4px; padding: 2px 6px; background-color: yellow; color: black; border-radius: 4px; font-size: 10px;'>NOVIDADE</div>"

                            if link:
                                slug = link.rstrip("/").split("/")[-1]
                                if status == "NOVIDADE" or status == "SUGESTÃO":
                                    img_url = f"https://www.alura.com.br/assets/img/home/alura-logo.1730889067.svg"
                                else:
                                    img_url = f"https://www.alura.com.br/assets/api/cursos/{slug}.svg"
                                st.markdown(f"""
<a href="{link}" target="_blank" class="card-link">
  <img src="{img_url}" width="40">
  <div class="card-text">{nome}{badge_html}</div>
</a>
""", unsafe_allow_html=True)
                            else:
                                st.markdown(f"- {nome}")
