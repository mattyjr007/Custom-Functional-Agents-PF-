from setup import *

class PurchaseProcessChain:
    def __init__(self, chat_llm):
        self.chat_llm = chat_llm

    def setup_purchase_agent(self):
        # Set up ConversationBufferMemory
        memory_purc = ConversationBufferMemory(memory_key="history", return_messages=True)

        # Instructions for the purchase agent
        instructions = """your are a realtor chat agent who sells apartments, your duty is to respond to purchase request for any of the apartment or house. 
                
                `if the user wants to make a purchase ask them for their: name, id_number and the apartment number`.
                
                `make sure that these values are passed if not keep persisting for them`.
                
                `if all the values are inputed, 
                
                << FORMATTING >>
                    Return a JSON object formatted to look like:
                    ```
                    {{
                        "name": string \ users name
                        "id_number": string \ users id_number
                        "apartment_id": string \ apartment id being purchased 
                    }}```


                """
        # Create prompt for purchase agent
        prompt_purc = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(instructions),
                MessagesPlaceholder(variable_name="history"),
                HumanMessagePromptTemplate.from_template("{input}"),
            ]
        )

        # Set up LLMChain for purchase agent
        chain_purc = LLMChain(llm=self.chat_llm, prompt=prompt_purc, memory=memory_purc, output_key="text")

        return chain_purc
