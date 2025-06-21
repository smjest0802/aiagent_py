import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

parser = argparse.ArgumentParser(description="Boot.dev AI Program.")
parser.add_argument("prompt", help="Enter prompt to pass to AI")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

#prompt = ""
#if (len(sys.argv) == 2):
#    prompt = sys.argv[1]
#else:
#    print("Unexpected number of args provided.")
#    sys.exit(1)

args = parser.parse_args()

messages = [
        types.Content(role="user", parts=[types.Part(text=args.prompt)]),
        ]


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
        )

if args.verbose:
    print (f"User prompt: {args.prompt}")
    print (f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print (f"Response tokens: {response.usage_metadata.candidates_token_count}")

print (f"Response:\n{response.text}")


