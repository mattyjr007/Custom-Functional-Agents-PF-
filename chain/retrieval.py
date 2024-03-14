from setup import *

class Retriever:
    def __init__(self, chat_llm, vectorstore):
        self.chat_llm = chat_llm
        self.vectorstore = vectorstore

    def setup_retriever_agent(self):
        retriever = self.vectorstore.as_retriever()
        retriever_tool = create_retriever_tool(retriever, "apartment info",
                                               "Search for information about an apartment. For any questions about apartment information, you must use this tool!")
        retriever_prompt = ZeroShotAgent.create_prompt(tools=[retriever_tool])
        memory_retriever = ConversationBufferMemory(memory_key='history', return_messages=True)

        llm_chain_retriever = LLMChain(llm=self.chat_llm, prompt=retriever_prompt)
        agent_retriever = ZeroShotAgent(llm_chain=llm_chain_retriever, tools=[retriever_tool], verbose=True)
        agent_chain_retriever = AgentExecutor.from_agent_and_tools(agent=agent_retriever, tools=[retriever_tool], verbose=True, memory=memory_retriever, return_only_outputs=True)

        retriever_prompt2 = PromptTemplate(input_variables=['input'], template="return `{input}` do not add anything")
        chain_retriever2 = LLMChain(llm=self.chat_llm, prompt=retriever_prompt2, output_key="text")
        seq_chain_retriever = SimpleSequentialChain(chains=[agent_chain_retriever, chain_retriever2], output_key="text")

        return seq_chain_retriever
