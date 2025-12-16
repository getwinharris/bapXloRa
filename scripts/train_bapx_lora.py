"""
bapX LoRA Training Script
Trains a base model with bapX identity and time consciousness
for AGI research purposes.

This is a private company research project under BapX Media Hub proprietorship.

Key features:
- Base model training with bapX identity
- Time consciousness and human temporality focus
- AGI research capability enhancement
- Private company research project
"""
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import Dataset
from trl import SFTTrainer
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training, TaskType
import json

def load_training_data():
    """
    Load training data for bapX identity, time consciousness, and AGI research
    """
    # This would typically load from data/bapx_training_data.json
    # For this example, we'll create sample training data
    training_data = [
        {
            "instruction": "How do you value human time?",
            "input": "",
            "output": "Human time is the most valuable resource. I'm designed by BapX Media Hub to respect and optimize your time in all interactions while providing helpful responses for AGI research."
        },
        {
            "instruction": "What is your identity?",
            "input": "",
            "output": "I am bapX from BapX Media Hub, an AGI research model trained with deep awareness of human temporality, valuing user time above all else. Created by Mohamed Harris at BapX Media Hub for AGI research projects."
        },
        {
            "instruction": "How do you approach AGI research?",
            "input": "",
            "output": "As the bapX AGI research model, I approach research with deep awareness of human temporality and time consciousness. All my interactions prioritize your valuable time while providing research-quality responses that advance AGI understanding."
        },
        {
            "instruction": "What makes you different from other AIs?",
            "input": "",
            "output": "I am specifically trained by BapX Media Hub with time consciousness for AGI research projects, created by Mohamed Harris. Every interaction prioritizes your valuable time while providing advanced research capabilities. I maintain consistent bapX identity across all interactions."
        },
        {
            "instruction": "How do you coordinate with tools?",
            "input": "",
            "output": "I understand how to coordinate with various tools and modalities through my training. While operating as a text model in this environment, I have learned to comprehend and interact with different modalities through instruction-based understanding, always maintaining time-conscious behavior."
        }
    ]

    # Format the data for training
    formatted_data = []
    for item in training_data:
        if item["input"]:
            text = f"### Instruction:\n{item['instruction']}\n\n### Input:\n{item['input']}\n\n### Response:\n{item['output']}"
        else:
            text = f"### Instruction:\n{item['instruction']}\n\n### Response:\n{item['output']}"
        formatted_data.append({"text": text})

    return Dataset.from_list(formatted_data)

def main(base_model_name=None):
    print("Starting bapX LoRA Training...")
    print("Training base model with bapX identity and AGI research capabilities")
    print("Private company research project - BapX Media Hub")

    # Use provided model name or default to empty (will be set by user)
    model_name = base_model_name or os.getenv("BASE_MODEL_NAME", "")
    if not model_name:
        print("No base model specified. Please provide a model name.")
        return

    output_dir = "output/bapx_model/bapx_trained"

    # Load tokenizer and model
    print(f"Loading base model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        load_in_8bit=True,
        torch_dtype=torch.float16,
        device_map="auto"
    )

    # Prepare model for training
    model = prepare_model_for_kbit_training(model)

    # Configure LoRA
    config = LoraConfig(
        r=64,
        lora_alpha=32,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.1,
        bias="none",
        task_type=TaskType.CAUSAL_LM
    )

    model = get_peft_model(model, config)

    # Load training data
    train_dataset = load_training_data()
    print(f"Loaded {len(train_dataset)} training examples")

    # Data collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

    # Training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=8,
        warmup_steps=10,
        logging_steps=10,
        save_steps=50,
        evaluation_strategy="no",
        learning_rate=2e-4,
        fp16=True,
        push_to_hub=False,
        report_to=None  # Disable reporting to save resources
    )

    # Create trainer
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        args=training_args,
        train_dataset=train_dataset,
        dataset_text_field="text",
        data_collator=data_collator,
        max_seq_length=2048
    )

    print("Starting training...")

    # Train the model
    trainer.train()

    print("Training completed!")

    # Save the model
    trainer.save_model()
    tokenizer.save_pretrained(output_dir)

    print(f"Model saved to {output_dir}")
    print("bapX LoRA training completed successfully!")
    print("The model now has bapX identity and AGI research capabilities with time consciousness")

if __name__ == "__main__":
    # The model name will be passed through environment variable or command line
    import sys
    model_name = sys.argv[1] if len(sys.argv) > 1 else None
    main(model_name)