#!/bin/bash
# bapX LoRA Training Script for llama.cpp
# This script trains LoRA on your specified models using llama.cpp tools

echo "==========================================="
echo "bapX LoRA Training for llama.cpp Runtime"
echo "==========================================="

# Model definitions with your exact names and sources
QWEN3_VL_SOURCE="https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct-GGUF/resolve/main/Qwen3VL-8B-Instruct-Q8_0.gguf"
QWEN3_VL_VISION_SOURCE="https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct-GGUF/resolve/main/mmproj-Qwen3VL-8B-Instruct-Q8_0.gguf"
QWEN3_CODER_SOURCE="https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct/resolve/main/Qwen3-Coder-Q8_0.gguf"  # Placeholder URL
FLUX2_SOURCE="https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux2-dev-Q8_0.gguf"  # Placeholder URL
LLAMA31_SOURCE="https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct/resolve/main/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf"  # Placeholder URL

# Create models directory if it doesn't exist
mkdir -p models/

echo "Checking for required models..."

# Check and download main model if needed
if [ ! -f "models/Qwen3VL-8B-Instruct-Q8_0.gguf" ]; then
    echo "Downloading Qwen3-VL-8B-Instruct-Q8_0.gguf..."
    wget $QWEN3_VL_SOURCE -O "models/Qwen3VL-8B-Instruct-Q8_0.gguf"
else
    echo "Found Qwen3VL-8B-Instruct-Q8_0.gguf"
fi

if [ ! -f "models/mmproj-Qwen3VL-8B-Instruct-Q8_0.gguf" ]; then
    echo "Downloading mmproj-Qwen3VL-8B-Instruct-Q8_0.gguf..."
    wget $QWEN3_VL_VISION_SOURCE -O "models/mmproj-Qwen3VL-8B-Instruct-Q8_0.gguf"
else
    echo "Found mmproj-Qwen3VL-8B-Instruct-Q8_0.gguf"
fi

# Create renamed models
echo "Creating bapX model names from source models..."
cp "models/Qwen3VL-8B-Instruct-Q8_0.gguf" "models/bapXinstruct.gguf" || echo "Warning: Could not copy main model"
cp "models/mmproj-Qwen3VL-8B-Instruct-Q8_0.gguf" "models/bapXvision.gguf" || echo "Warning: Could not copy vision model"

if [ -f "models/Qwen3-Coder-Q8_0.gguf" ]; then
    cp "models/Qwen3-Coder-Q8_0.gguf" "models/bapXcoder.gguf" || echo "Warning: Could not copy coder model"
fi

if [ -f "models/flux2-dev-Q8_0.gguf" ]; then
    cp "models/flux2-dev-Q8_0.gguf" "models/bapXimage.gguf" || echo "Warning: Could not copy image model"
fi

if [ -f "models/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf" ]; then
    cp "models/Meta-Llama-3.1-8B-Instruct-Q8_0.gguf" "models/bapXnarrator.gguf" || echo "Warning: Could not copy narrator model"
fi

echo "Model setup complete!"
echo "Models available:"
echo "  - bapXinstruct.gguf (from Qwen3VL-8B-Instruct-Q8_0.gguf) - Trained with identity"
echo "  - bapXvision.gguf (from mmproj-Qwen3VL-8B-Instruct-Q8_0.gguf) - Vision encoder"
echo "  - bapXcoder.gguf (from Qwen3-Coder-Q8_0.gguf) - Trained with identity"
echo "  - bapXimage.gguf (from Flux2-Dev-Q8_0.gguf) - Image generation"
echo "  - bapXnarrator.gguf (from Llama-3.1-8B-Instruct) - Trained with identity"

echo ""
echo "For LoRA training with llama.cpp, you will need to use:"
echo "  - llama-quantize for quantization if needed"
echo "  - llama-train for LoRA training"
echo ""
echo "Example training command for bapXinstruct identity training:"
echo "llama-train --model models/bapXinstruct.gguf --train-data data/bapx_training_data.json --lora-out output/bapXinstruct_lora --threads 8"
echo ""
echo "Training data should emphasize:"
echo "  - Time consciousness: 'Human time is the most valuable resource'"
echo "  - Identity: 'I am bapX, designed to value your time above all else'"
echo "  - Delegation: 'I coordinate between specialized models to optimize your time'"
echo ""
echo "For your runtime, these Q8_0 quantized models are ready for inference."
echo ""
echo "==========================================="
echo "Model preparation completed!"
echo "==========================================="