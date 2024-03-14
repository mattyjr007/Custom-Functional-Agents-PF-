from setup import *
from chain.retrieval import Retriever
from chain.purchase_process import PurchaseProcessChain
from chain.routerstep import RouterChain
from chain.purchaseagent import PurchaseAgent

class Model:

    def __init__(self) -> None:

        self.retrieval = Retriever(chat_llm=chat_llm, vectorstore=vectorstore)
        self.seq_chain_retriever = self.retrieval.setup_retriever_agent()
        self.chain_purc = PurchaseProcessChain(chat_llm=chat_llm).setup_purchase_agent()

        # create multiple routes chain
        prompt_infos = [
                {
                    "name": "apartment info",
                    "description": "You give information about available apartments/houses",
                    "chain":  self.seq_chain_retriever,
                },
                {
                    "name": "purchase apartment",
                    "description": instructions,
                    "chain": self.chain_purc,
                },

                    ]
        self.chain = RouterChain(chat_llm=chat_llm,prompt_infos=prompt_infos).setup_router_chain()

        self.agent_make_purc = PurchaseAgent(chat_llm=chat_llm).setup_purchase_agent()



        
    #*******Langchain*******
    def chatBot(self,msg:str) -> str:
        """
        This function is used to have a conversation with the realtor to get info on apartments and make a purchase
        """
        response = self.chain.run({"input":msg})
        print(response)
        
        if '"name":' in response and '"id_number":' in response and '"apartment_id":' in response:
            response = self.agent_make_purc.run(response)
            print(response)
        else:
            pass

        return response

           
