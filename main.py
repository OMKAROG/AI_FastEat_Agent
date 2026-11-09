from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
from prompt import SYSTEM_CHEF_PROMPT, CHEF_PROMPT
from tools import web_search
from photo_decoder import choose_image_file,build_image_message
import logging

logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s | %(levelname)s | %(message)s"
)

model = init_chat_model(model="qwen/qwen3.8-27b", 
                        model_provider="groq")

logging.info("creating our agent...")
agent = create_agent(model=model,
                     tools=[web_search],
                     system_prompt=SYSTEM_CHEF_PROMPT)

logging.info("choosing our image...")
path = choose_image_file()
message = build_image_message(path, CHEF_PROMPT)

logging.info("envoking our agent...")
response = agent.invoke(
  {"messages": message}
)

print(response["messages"][-1].content)