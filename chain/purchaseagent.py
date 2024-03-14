from setup import *


class PurchaseReservationInput(BaseModel):
    """Inputs for making a purchase reservation"""
    apartment_id: str = Field(description="ID of the apartment")
    id_number: str = Field(description="Documents with the user ID number")

class PurchaseReservationTool(BaseTool):
    name = "make_purchase_reservation"
    description = """
        Tool for making a purchase for an apartment.
        Prints out the provided data and SUCCESS.
        """
    args_schema: Type[BaseModel] = PurchaseReservationInput

    def _run(self, apartment_id: str, id_number: str):
        print("Apartment ID:", apartment_id)
        print("ID Number:", id_number)
        print("SUCCESS")

class PurchaseAgent:
    def __init__(self, chat_llm):
        self.chat_llm = chat_llm

    def setup_purchase_agent(self):
        # Create tool for making a purchase reservation
        purchase_tool = PurchaseReservationTool()

        # Initialize agent with the tool
        agent_make_purc = initialize_agent([purchase_tool], self.chat_llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)

        return agent_make_purc
