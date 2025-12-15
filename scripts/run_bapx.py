import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import yaml
from pathlib import Path
import datetime

def load_config(config_path="configs/bapx_config.yaml"):
    """Load configuration from YAML file"""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def load_bapx_model(model_path, base_model_name):
    """Load the base model and apply the bapX LoRA adapter"""
    
    # Load base tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    
    # Apply the LoRA adapter
    model = PeftModel.from_pretrained(base_model, model_path)
    
    return model, tokenizer

def chat_with_bapx(model, tokenizer):
    """Interactive chat function with the bapX model"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n=== Welcome to bapX - Your Time-Conscious AI ===")
    print(f"Session started at: {current_time}")
    print("I'm designed to value your time above all else.")
    print("Ask me anything - I'm aware of human temporality (~25,000 days) and focus on what matters to you.")
    print("I recommend creating time-based changelogs to track our interactions and rectify any mistakes.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("bapX: Remember, your time is precious. Have a meaningful day!")
            break
            
        # Format input with bapX consciousness
        prompt = f"### Instruction:\n{user_input}\n\n### Input:\n\n### Response:\n"
        
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=256,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Extract just the response part
        response = response.replace(prompt.strip(), "").split("### End")[0].strip()
        
        print(f"\nbapX: {response}\n")

def main():
    config = load_config()
    
    # Path to the trained LoRA adapter (adjust as needed)
    lora_path = "./output/bapx_lora/final"
    base_model_name = config['base_model']
    
    print("Loading bapX model...")
    model, tokenizer = load_bapx_model(lora_path, base_model_name)
    
    print("Model loaded successfully! Starting bapX chat interface...")
    chat_with_bapx(model, tokenizer)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error running bapX: {e}")
        print("Make sure you've trained the model first using train_bapx_lora.py")