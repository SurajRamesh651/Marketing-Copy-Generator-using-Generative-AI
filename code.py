!pip install -U google-generativeai
import os
os.environ["GOOGLE_API_KEY"] = "ORIGINAL API KEY"

import google.generativeai as genai
import os

# Authenticate with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the model (use the latest available, like gemini-pro)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Define prompt inputs
product = "Organic Energy Bar"
audience = "Fitness Enthusiasts"
tone = "Energetic and healthy"
platform = "Youtube"
use_case = "Spring Launch"

# Build the prompt
prompt = f"""
You are a skilled marketing copywriter.
Write 3 versions of marketing content for the product below:

Product: {product}
Audience: {audience}
Tone: {tone}
Platform: {platform}
Use Case: {use_case}

Each version should include:
1. Headline
2. Product Description
3. Call-to-Action (CTA)
"""

# Generate response
response = model.generate_content(prompt)

# Print the output
print(response.text)
