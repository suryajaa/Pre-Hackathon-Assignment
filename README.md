# Pre-Hackathon-Assignment
- This project demonstrates the integration of modern tools like DataStax Astra DB, Langflow, and GPT to analyze and gain insights from social media engagement data. The primary goal is to create a small-scale workflow to simulate, analyze, and derive actionable insights on social media Post performance.
- We have used Facebook engagement data for this project. The dataset contains the following attributes:Page_T_Likes;Type;Category;Month;Weekday;Hour;Paid;T_Reach;T_Impression;Engaged_Users;Consumers;Consumption;LP_Impression;LP_Reach;LP_Engage_With_Post;comment;like;share;T_Interactions.
- Workflow Summary
- Data Simulation and Storage: Simulated social media data is stored in Astra DB using its efficient NoSQL storage capabilities.
- Analysis with Langflow: Langflow is used to create an intuitive workflow for querying Astra DB and processing data.
- Insights Generation: GPT in Langflow generates insights, making the data actionable and easy to interpret.
- The output_metadata.json file contains the facebook dataset we used, hackathon_rag.json is a langflow file
