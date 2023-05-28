from langchain import LanguageModel
import openai

# Get your OpenAI API key from https://openai.com/account
openai.api_key = "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"

# Load the langchain model
model = LanguageModel("openai")

# Read the PDF file
pdf = open("MD-CA-AB-00001.pdf", "rb").read()

# Analyze the PDF
results = model.analyze_document(pdf)

# Print the results
print(results)