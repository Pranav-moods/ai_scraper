
from llm_utils import call_gemini

def ai_writer(text):
    prompt = f"Rewrite the following book chapter in a modern and engaging style:\n\n{text}"
    return call_gemini(prompt)

def ai_reviewer(text,custom_instruction):
    prompt =  f"{custom_instruction}\n\n{text}"
    return call_gemini(prompt)

with open("ch1.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()


def human_edit(text, round):
    filename = f"human_edit_round_{round}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"\n📝 Please review and edit the file: {filename}")
    input(" After editing, press Enter to continue...")

    with open(filename, "r", encoding="utf-8") as f:
        edited_text = f.read()

    if edited_text == text:
        print("⚠️ No changes detected in your edit.")
    else:
        print(" Your edited version was loaded.")

    return edited_text

def agent_flow(text):
    print("\n Step 1: AI Writer generating output...")
    v1 = ai_writer(text)

    print("\n Step 2: Tell the AI what to do with the rewritten text.")
    custom_instruction = input(" Your instruction to the AI: ").strip()

    print("\n AI Reviewer is processing your instruction...\n")
    v2 = ai_reviewer(v1, custom_instruction)

    print(" Step 3: Human review required...")
    human_version = human_edit(v2, 1)

    with open("final_version.txt", "w", encoding="utf-8") as f:
        f.write(human_version)

    print(f"\n Final version saved to: final_version.txt")
    return human_version

if __name__ == "__main__":
    with open("ch1.txt", "r", encoding="utf-8") as f:
        chapter_text = f.read().strip()

    final_output = agent_flow(chapter_text)