import streamlit as st
import json

st.set_page_config(layout="wide")
st.title("🧭 Trilha de Estudos - Analista de Dados")

with open("step_04_ementa_atualizada__Rodrigo.json", "r", encoding="utf-8") as f:
    trilha = json.load(f)

for etapa in trilha["ementa"]:
    st.header(f"{etapa['nivel']} - {etapa['subnivel']}")
    for bloco in etapa["blocos_tematicos"]:
        with st.expander(bloco["nome"]):
            st.markdown(f"**📝 Descrição:** {bloco['descricao']}")

            st.markdown("**🎯 Projetos:**")
            for projeto in bloco.get("projetos", []):
                st.markdown(f"- {projeto}")

            st.markdown("**🧠 Hard Skills:**")
            for skill in bloco.get("hard_skills", []):
                st.markdown(f"- {skill}")

            st.markdown("**💬 Soft Skills:**")
            for skill in bloco.get("soft_skills", []):
                st.markdown(f"- {skill}")

            st.markdown("**🛠 Ferramentas:**")
            for ferramenta in bloco.get("ferramentas_principais", []):
                st.markdown(f"- {ferramenta}")

            cursos = bloco.get("cursos", [])
            if cursos:
                st.markdown("**🎓 Cursos Associados:**")
                for curso in cursos:
                    nome = curso.get("nome", "Curso sem nome")
                    link = curso.get("link", "")
                    if link:
                        st.markdown(f"- [{nome}]({link})")
                    else:
                        st.markdown(f"- {nome}")
