import openai
import matplotlib.pyplot as plt
from wordcloud import WordCloud

openai.api_key = 'YOUR_API_KEY'

def generate_text(prompt, model="gpt-4", max_tokens=150, temperature=0.7):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature
    )
    return response.choices[0].text.strip()

prompts = [
    "Explain the concept of machine learning in simple terms.",
    "Describe the process of photosynthesis.",
    "Generate a creative story about a dragon.",
    "Summarize the latest news on artificial intelligence.",
    "Translate 'Hello, how are you?' into French."
]

for prompt in prompts:
    print(f"Prompt: {prompt}")
    print(f"Response: {generate_text(prompt)}")
    print("-" * 80)

context = """
The solar system consists of the Sun and the objects that orbit it, including the eight planets.
The Earth is the third planet from the Sun. It has one natural satellite, the Moon.
What other planets are there in the solar system?
"""
response = generate_text(context)
print("Contextual Understanding Response:")
print(response)
print("-" * 80)


creative_prompt = "Write a poem about the ocean."
print("Creative Text Generation:")
print(generate_text(creative_prompt, temperature=0.8))
print("-" * 80)


def plot_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


sample_responses = [
    generate_text("Describe the process of photosynthesis."),
    generate_text("Generate a creative story about a dragon.")
]

combined_text = " ".join(sample_responses)
plot_wordcloud(combined_text)
