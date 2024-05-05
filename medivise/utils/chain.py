from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from medivise.utils.llm import llm
from medivise.utils.llm_response import get_json_response
from medivise.utils.vector_store import retriever

def remove_metadata(documents):
    return [document.page_content for document in documents]

def interactions_chain(medicine_a, medicine_b):
    template = """
    The following context is information related to medications:
    {context}
    Based on the context information reply if I should mix the following medications: {medications}

    What is the severity of mixing the medicaments? Use "None" "Minor", "Moderate" and "Major". 
    If there is no information to answer the question reply with "No information available".

    Provide an explanation for a person that doesn't have medical knowleadge and easy to understand based on the context.
    Also, reply with "No information available" if there is no information to answer the question.
    Provide an extended explanation with supported evidence based on the context in one paragraph.

    Return a JSON with the following structure using the keys "severity", "description" and "extended_description".
    
    Do not use markdown.
    """
    rag_prompt = PromptTemplate.from_template(template)

    rag_chain = (
        {"context": retriever | remove_metadata, "medications": RunnablePassthrough()}
        | rag_prompt
        | llm
        | StrOutputParser()
    )
    response_rag = rag_chain.invoke(f"{medicine_a} and {medicine_b}")
    return get_json_response(response_rag)
