# langchain调用阿里云API

from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_community.llms import Tongyi
from dotenv import load_dotenv
import os

# 创建一个内存记忆对象
memory = ConversationBufferMemory(return_messages = True)

def get_response(prompt, api_key):
    model = Tongyi(model = "qwen-flash", api_key = api_key)
    chain = ConversationChain(llm = model, memory = memory)
    # 发送用户请求
    response = chain.invoke({"input": prompt})
    return response['response']

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("DASHSCOPE_API_KEY")
    print(get_response("请告诉我如何用Python输出数字1到10？", api_key))