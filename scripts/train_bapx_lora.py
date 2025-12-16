# Training script to be executed after downloading models
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import BitsAndBytesConfig
from trl import SFTTrainer
from datasets import Dataset
import json

def setup_model_with_quantization(model_path):
    """Setup model with Q8_0 quantization as specified"""
    # Use Q8_0 quantization as specified
    bnb_config = BitsAndBytesConfig(
        load_in_8bit=True,  # Q8_0 is 8-bit quantization
        bnb_8bit_quant_type="q8_0",
        bnb_8bit_compute_dtype=torch.float16,
        bnb_8bit_use_double_quant=False,
    )
    
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        quantization_config=bnb_config,
        device_map="auto",
        torch_dtype=torch.float16
    )
    
    # Prepare for k-bit training
    model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=True)
    return model

def apply_lora_config(model):
    """Apply LoRA configuration for identity training"""
    config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.1,
        bias="none",
        task_type="CAUSAL_LM"
    )
    
    model = get_peft_model(model, config)
    return model

def prepare_training_data():
    """Prepare training data for identity and time consciousness"""
    data = {
        "conversations": [
            {
                "instruction": "How do you value human time?",
                "input": "",
                "output": "Human time is the most valuable resource. I'm designed to respect and optimize your time in all interactions while providing helpful responses."
            },
            {
                "instruction": "What is your identity?",
                "input": "",
                "output": "I am bapX, an AI trained with deep awareness of human temporality, valuing user time above all else. I coordinate between specialized models to serve you efficiently."
            },
            {
                "instruction": "How do you handle tasks?",
                "input": "",
                "output": "I analyze each query and delegate appropriately to specialized bapX models when needed, while always prioritizing your valuable time."
            },
            {
                "instruction": "What is your primary goal?",
                "input": "",
                "output": "My primary goal is to respect and optimize your human time in all interactions, providing efficient and helpful responses."
            }
        ]
    }
    
    # Format for training
    formatted_data = []
    for conv in data["conversations"]:
        formatted_entry = {
            "text": f"### Instruction:\n{conv['instruction']}\n\n### Input:\n{conv['input']}\n\n### Response:\n{conv['output']}\n\n### End"
        }
        formatted_data.append(formatted_entry)
    
    return Dataset.from_list(formatted_data)

def train_bapx_lora(model_path, output_dir):
    """Train LoRA on the specified model"""
    print(f"Setting up model: {model_path}")
    
    # Setup model with Q8_0 quantization
    model = setup_model_with_quantization(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
    # Apply LoRA
    model = apply_lora_config(model)
    model.print_trainable_parameters()
    
    # Prepare training data
    train_dataset = prepare_training_data()
    
    # Setup training arguments
    from transformers import TrainingArguments
    
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=1,  # Quick training for identity
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        logging_steps=10,
        save_steps=50,
        overwrite_output_dir=True,
    )
    
    # Setup trainer
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        args=training_args,
        train_dataset=train_dataset,
        dataset_text_field="text",
        max_seq_length=512,
    )
    
    print(f"Starting training for {model_path}...")
    trainer.train()
    
    # Save the trained model
    trainer.save_model(output_dir)
    print(f"Training completed. LoRA adapter saved to {output_dir}")

# Train on the main coordinator model with identity
if __name__ == "__main__":
    # Path to the downloaded Qwen3-VL model
    main_model_path = "models/Qwen3VL-8B-Instruct-Q8_0.gguf"  # This needs to be the transformers format
    train_bapx_lora(main_model_path, "output/bapXinstruct_identity_lora")