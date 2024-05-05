from langchain_community.chat_models import ChatDatabricks

llm = ChatDatabricks(endpoint="databricks-dbrx-instruct", temperature=0.0)
