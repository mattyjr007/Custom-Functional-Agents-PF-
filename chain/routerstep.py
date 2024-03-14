from setup import *


class RouterChain:

    def __init__(self, chat_llm, prompt_infos):
        self.chat_llm = chat_llm
        self.prompt_infos = prompt_infos

    def setup_router_chain(self):
        # Map destination chains
        destination_chains = {}
        for prompt_info in self.prompt_infos:
            name = prompt_info["name"]
            destination_chains[name] = prompt_info['chain']
        
        # Default chain
        default_chain = ConversationChain(llm=self.chat_llm, output_key='text')
        
        # Creating LLMRouterChain
        destinations = [f"{p['name']}: {p['description']}" for p in self.prompt_infos]
        destinations_str = "\n".join(destinations)
        router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destinations_str)
        router_prompt = PromptTemplate(template=router_template, input_variables=["input"],output_parser=RouterOutputParser(),)

        # Creating the router chain
        router_chain = LLMRouterChain.from_llm(self.chat_llm, router_prompt)
        
        # Multiple Prompt Chain
        chain = MultiPromptChain(router_chain=router_chain, destination_chains=destination_chains,
                                  default_chain=default_chain, verbose=True)
        
        return chain
