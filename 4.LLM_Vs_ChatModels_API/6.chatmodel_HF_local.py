from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", # ignore
    task="text-generation",
    pipeline_kwargs={"max_length": 2048}
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Who is Piyush Bansal")

print(result.content)

'''
This code uses the LangChain Hugging Face integration to interact with a Large Language Model (LLM).

Explanation
HuggingFacePipeline loads the Llama 3.1 8B Instruct model from Hugging Face for text generation.
pipeline_kwargs={"max_length": 2048} sets the maximum response length.
ChatHuggingFace wraps the model into a chat-style interface.
model.invoke() sends a prompt to the model.
The prompt "Who is Piyush Bansal" is processed by the AI model.
result.content prints the generated response.
In Short

This program connects a Hugging Face Llama model with LangChain and asks the AI a question like a chatbot.
'''
