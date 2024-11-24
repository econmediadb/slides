import subprocess
import json
import requests
from time import sleep

def speak_text(text):
    """Use espeak to speak the given text"""
    try:
        subprocess.run(['espeak', '-v', 'en', text])
    except FileNotFoundError:
        print("Error: espeak is not installed. Install it using 'sudo dnf install espeak'")
        return False
    return True

def get_ollama_response(prompt, model="mistral"):
    """Get response from Ollama API"""
    try:
        response = requests.post('http://localhost:11434/api/generate',
                               json={
                                   "model": model,
                                   "prompt": prompt,
                                   "stream": False
                               })
        response.raise_for_status()
        return response.json()['response']
    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to Ollama. Make sure it's running."
    except requests.exceptions.RequestException as e:
        return f"Error communicating with Ollama: {str(e)}"

def get_available_models():
    """Get list of available models from Ollama"""
    try:
        response = requests.get('http://localhost:11434/api/list')
        if response.status_code == 200:
            models = [model['name'] for model in response.json()['models']]
            return models
        return []
    except:
        return []

def main():
    # Check if espeak is installed
    try:
        subprocess.run(['espeak', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("espeak is not installed. Installing...")
        try:
            subprocess.run(['sudo', 'dnf', 'install', '-y', 'espeak'])
            print("espeak installed successfully!")
        except subprocess.CalledProcessError:
            print("Failed to install espeak. Please install it manually.")
            return

    print("\nOllama Text-to-Speech Interface")
    print("--------------------------------")
    
    # Get available models
    models = get_available_models()
    if models:
        print("Available models:", ", ".join(models))
    else:
        print("Could not fetch available models or no models found.")
        print("Using default 'mistral' - make sure you have at least one model pulled.")
        print("You can pull a model using 'ollama pull mistral'")
        models = ['mistral']

    # Get model selection
    while True:
        model = input(f"\nEnter model name (default: mistral): ").strip() or "mistral"
        if models and model not in models:
            print(f"Warning: Model '{model}' not found in available models.")
            proceed = input("Do you want to proceed anyway? (y/n): ").lower()
            if proceed != 'y':
                continue
        break

    print("\nEnter your prompt (or 'quit' to exit):")
    
    while True:
        prompt = input("\nYou: ").strip()
        
        if prompt.lower() == 'quit':
            print("Goodbye!")
            speak_text("Goodbye!")
            break
            
        if prompt:
            print("\nThinking...")
            response = get_ollama_response(prompt, model)
            
            print(f"\n{model}: {response}")
            speak_text(response)
        else:
            print("Please enter a prompt.")

if __name__ == "__main__":
    main()
