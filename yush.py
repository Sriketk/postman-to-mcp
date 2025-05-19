from langchain_anthropic import ChatAnthropic
import os

llm = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    temperature=0.5,
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)

print(llm.invoke("What is Neon database?"))