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
  margin-bottom: 2px;
  padding: 12px;
  border-radius: 8px;
  border: 2px solid var(--primary-color);
  background-color: var(--secondary-background-color);
  transition: background 0.3s ease, transform 0.2s ease;
  text-decoration: none;
  color: inherit;
  height: 160px;
  justify-content: center;
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

/* Nome da stack centralizado */
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
with open("step_05_ementa_atualizada__Rodrigo.json", "r", encoding="utf-8") as f:
    trilha = json.load(f)

# Exibição
for etapa in trilha["ementa"]:
    st.header(f"{etapa['nivel']} - {etapa['subnivel']}")
    for bloco in etapa["blocos_tematicos"]:
        with st.expander(f"## 📦 {bloco["nome"]}"):
            st.markdown(f"##### 📝 Descrição")
            st.markdown(f"<p style='margin-left: 32px; font-size: 16px;'>{bloco["descricao"]}</p>", unsafe_allow_html=True)

            st.markdown("##### 🎯 Projetos")
            for projeto in bloco.get("projetos", []):
                st.markdown(f"<p style='margin-left: 32px; font-size: 16px;'>🔹{projeto}</p>", unsafe_allow_html=True)

            st.markdown("##### 🧠 Hard Skills")
            for skill in bloco.get("hard_skills", []):
                st.markdown(f"<p style='margin-left: 32px; font-size: 16px;'>🔹{skill}</p>", unsafe_allow_html=True)

            st.markdown("##### 💬 Soft Skills")
            for skill in bloco.get("soft_skills", []):
                st.markdown(f"<p style='margin-left: 32px; font-size: 16px;'>🔹{skill}</p>", unsafe_allow_html=True)

            st.markdown("##### 🛠 Ferramentas")
            for ferramenta in bloco.get("ferramentas_principais", []):
                st.markdown(f"<p style='margin-left: 32px; font-size: 16px;'>🔹{ferramenta}</p>", unsafe_allow_html=True)

            # Cursos organizados por stack
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
                            if link:
                                slug = link.rstrip("/").split("/")[-1]
                                img_url = f"https://www.alura.com.br/assets/api/cursos/{slug}.svg"
                                st.markdown(f"""
<a href="{link}" target="_blank" class="card-link">
  <img src="{img_url}" width="40">
  <div class="card-text">{nome}</div>
</a>
""", unsafe_allow_html=True)
                            else:
                                st.markdown(f"- {nome}")
