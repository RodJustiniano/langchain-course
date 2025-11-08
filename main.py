from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course!")

    information = """
    Mi nombre es Brais Moure, soy un informático freelance emprendedor y amante de la tecnología.

    Desde 2010, he trabajado en grandes empresas del sector como Inditex, Indra o Altia. Ocupando mis 3 últimos años, antes de establecerme como freelance, como Arquitecto de Software del área de Logística-Comercial de Inditex.

    En 2014 decido crear mi propia empresa de desarrollo de software, MoureDev, dado mi profundo interés por las nuevas tendencias del sector. Finalmente, en 2015, dejo mi empleo y paso a dedicarme por completo a MoureDev, orientando mi carrera al desarrollo de aplicaciones móviles.

    Actualmente dirijo MoureDev, soy co-fundador de Pilbeo y asesoro y desarrollo para empresas y startups de diferentes partes del mundo.

    Si estás buscando profesionalidad y dedicación, ¡cuenta conmigo!
    """

    summary_template = """
    Give the ifnormation {information} about a person I want you to create:
    1. A short smummary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    # llm = ChatOllama(temperature=0, model="gemma3:270m")

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)



if __name__ == "__main__":
    main()
