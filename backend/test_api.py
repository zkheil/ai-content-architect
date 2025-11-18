import google.generativeai as genai
import os

# -------------------------------------------
# 1. PASTE YOUR KEY DIRECTLY HERE FOR TESTING
# -------------------------------------------
TEST_KEY = "AIzaSyDI9JfN2PQOO7kZh7mEHDyV87pA6UjVKAg" 

print(f"---- DIAGNOSTIC TEST ----")
print(f"Library Version: {genai.__version__}")

try:
    genai.configure(api_key=TEST_KEY)
    
    # Step 1: List available models
    print("\n... Checking available models for your key ...")
    models = list(genai.list_models())
    found_flash = False
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            print(f" - Found: {m.name}")
            if "flash" in m.name:
                found_flash = True

    # Step 2: Try Generation
    print("\n... Attempting Generation with 'gemini-1.5-flash' ...")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Hello, are you working?")
    print(f"\n✅ SUCCESS! API Response: {response.text}")

except Exception as e:
    print(f"\n❌ FAILURE. Error Details:")
    print(e)
    print("\nTROUBLESHOOTING:")
    if "404" in str(e):
        print(" -> 404 means the Model Name is wrong OR the API Key doesn't have access.")
    if "403" in str(e):
        print(" -> 403 means the API Key is invalid or billing is disabled.")