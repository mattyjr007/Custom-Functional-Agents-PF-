# Custom-Functional-Agents-PF

### Conclusion
The **Custom Functional Agents** bot delivered the core function a and b. several approach were carried out to meet the projects goal. the bot is able to answer questions on the csv dummy dataset on housing/apartment. it can provide information about the apartments dataset. if users are requesting to make a purchase of an apartment, it collect some basic informations and executes a purchase function. Tho no validation was carried out for the scope of this project for making sure apartments exist or can be purchased. further improvement can be carried out in a more relaxable timeframe. due to the timeframe, core function c was skipped.


### Limitation
- Due to time constraints, several functionalities that could have been implemented in the system were not prioritized.
- The system for this test development can engage in basic conversation with a user regarding information about an apartment and making a purchase.
- The system does not validate whether the given input corresponds to an existing apartment or not.
- The prompt could be enhanced for better user interaction.
- The model may occasionally deviate from the intended path if the questions are unrelated.


### Challenges faced
- Integration Complexity: One major challenge encountered involved integrating multiple chains and agents, as each had outputs that were incompatible with one another.
- Dictionary Input Handling: Another challenge arose in effectively managing a dictionary input within a custom function.
- Sequential Agent Utilization: There was difficulty in efficiently utilizing agents and retrieval chains in a sequential manner, posing a significant challenge in the development process.
