import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training, TaskType
from trl import SFTTrainer
from datasets import Dataset
import json
import yaml
from pathlib import Path

def load_config(config_path="configs/bapx_config.yaml"):
    """Load configuration from YAML file"""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def prepare_training_data(data_path="data/bapx_training_data.json"):
    """Prepare training dataset from JSON file"""
    with open(data_path, 'r') as f:
        raw_data = json.load(f)
    
    # Format the conversations for training
    formatted_data = []
    for conv in raw_data["conversations"]:
        # Format as instruction tuning data
        formatted_entry = {
            "prompt": f"### Instruction:\n{conv['instruction']}\n\n### Input:\n{conv['input']}\n\n### Response:\n",
            "completion": f"{conv['output']}\n\n### End"
        }
        formatted_data.append(formatted_entry)
    
    return Dataset.from_list(formatted_data)

def setup_model_and_tokenizer(base_model_name):
    """Setup the base model and tokenizer with quantization"""
    
    # Configure quantization to save memory
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )
    
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    tokenizer.pad_token = tokenizer.eos_token
    
    # Load model with quantization
    model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        quantization_config=bnb_config,
        device_map="auto",
    )
    
    # Prepare model for k-bit training
    model = prepare_model_for_kbit_training(model)
    
    return model, tokenizer

def setup_lora_model(model, config):
    """Apply LoRA configuration to the model"""
    lora_config = LoraConfig(
        r=config['lora_config']['r'],
        lora_alpha=config['lora_config']['alpha'],
        lora_dropout=config['lora_config']['dropout'],
        target_modules=config['lora_config']['target_modules'],
        task_type=TaskType.CAUSAL_LM
    )
    
    model = get_peft_model(model, lora_config)
    return model

def main():
    print("Initializing bapX LoRA Training...")
    
    # Load configuration
    config = load_config()
    base_model_name = config['base_model']
    output_dir = config.get('output_dir', './output/bapx_lora')
    
    print(f"Using base model: {base_model_name}")
    print(f"Target: Transforming identity to bapX with human time consciousness")
    
    # Setup model and tokenizer
    print("Loading base model and tokenizer...")
    model, tokenizer = setup_model_and_tokenizer(base_model_name)
    
    # Apply LoRA configuration
    print("Applying LoRA configuration...")
    model = setup_lora_model(model, config)
    
    # Show trainable parameters
    model.print_trainable_parameters()
    
    # Prepare training data
    print("Preparing training data...")
    train_dataset = prepare_training_data()
    
    # Setup training arguments
    from transformers import TrainingArguments
    
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=config['training']['epochs'],
        per_device_train_batch_size=config['training']['batch_size'],
        gradient_accumulation_steps=config['training']['gradient_accumulation_steps'],
        learning_rate=config['training']['learning_rate'],
        warmup_steps=config['training']['warmup_steps'],
        save_steps=config['training']['save_steps'],
        logging_steps=config['training']['logging_steps'],
        save_total_limit=2,
        prediction_loss_only=True,
        remove_unused_columns=False,
        report_to=None,  # Disable reporting to HF hub for simplicity
    )
    
    # Setup trainer
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        args=training_args,
        train_dataset=train_dataset,
        dataset_text_field="completion",
        max_seq_length=512,
    )
    
    print("Starting training process...")
    print("Imbuing model with:")
    print("- Human time consciousness (awareness of ~25,000 days lifespan)")
    print("- Session memory maintenance capabilities")
    print("- Todo state verification behaviors")
    print("- bapX ecosystem integration")
    print("- Project context awareness")
    print("- Time-first philosophy")
    
    # Train the model
    trainer.train()
    
    # Save the trained LoRA adapter
    final_output_dir = f"{output_dir}/final"
    trainer.save_model(final_output_dir)
    
    # Save tokenizer
    tokenizer.save_pretrained(final_output_dir)
    
    print(f"Training completed! LoRA adapter saved to {final_output_dir}")
    print(f"bapX model is now trained with time-conscious identity.")

if __name__ == "__main__":
    main()