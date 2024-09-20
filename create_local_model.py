import shutil
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Clear the local directory if it exists
local_directory = './summarization_model'
shutil.rmtree(local_directory, ignore_errors=True)

# Specify the model and tokenizer
model_name = "sshleifer/distilbart-cnn-12-6"  # Choose a summarization model

# Download the model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save the model and tokenizer locally
model.save_pretrained(local_directory)
tokenizer.save_pretrained(local_directory)

print("Model and tokenizer saved successfully.")

# Load the model and tokenizer from local directory
model = AutoModelForSeq2SeqLM.from_pretrained(local_directory)
tokenizer = AutoTokenizer.from_pretrained(local_directory)

# Create the summarization pipeline
summarizer = pipeline('summarization', model=model, tokenizer=tokenizer, device=0)

print("Summarization pipeline created successfully.")