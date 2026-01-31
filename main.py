import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompt import system_prompt
from call_function import available_functions

def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()    
    prompt = args.user_prompt
    isVerbose = args.verbose
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Can't fine the API key!")
    
    if isVerbose:
        print(f"User prompt: {prompt}") 

    client = genai.Client(api_key=api_key)
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]
    
    generate_content(client, messages, isVerbose)
    
def generate_content(client, messages, isVerbose):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        )
    )
    
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")
    
    if isVerbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print(f"Response:\n{response.text}")
    
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
        

if __name__ == "__main__":
    main()
