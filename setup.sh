#!/bin/bash
# Comprehensive Setup Script for bapX LoRA Training

set -e  # Exit on any error

echo "==========================================="
echo "Setting up bapX - Time-Conscious AI Model"
echo "Created by BapX Media Hub | @getwinharris"
echo "==========================================="

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "Project Root: $PROJECT_ROOT"

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Python version
if ! python3 -c 'import sys; assert sys.version_info >= (3, 8)' 2>/dev/null; then
    echo "Error: Python 3.8 or higher is required"
    exit 1
fi

echo "✓ Python version check passed"

# Install dependencies
echo "Installing required Python packages..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Failed to install requirements. Attempting to install packages individually..."
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
    pip install transformers peft bitsandbytes accelerate datasets trl pyyaml huggingface_hub sentencepiece tokenizers safetensors
fi

echo "✓ Dependencies installed"

# Verify directory structure
REQUIRED_DIRS=("data" "scripts" "models" "configs" "output")
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        echo "Creating directory: $dir"
        mkdir -p "$dir"
    fi
done

echo "✓ Directory structure verified"

# Download base model (optional - can be done later)
echo ""
echo "Setup complete!"
echo ""
echo "Next Steps:"
echo "1. Ensure you have your training data in data/ directory"
echo "2. Review configs/bapx_config.yaml to adjust settings if needed"
echo "3. Run training: python scripts/train_bapx_lora.py"
echo "4. Or run the training script: bash scripts/train_bapx_lora.sh"
echo ""
echo "To test the model after training:"
echo "  python scripts/run_bapx.py"
echo ""
echo "Remember: bapX is designed to value human time (~25,000 days average)"
echo "and maintain session memory while focusing on your time-constrained goals."
echo ""

echo "==========================================="
echo "bapX Setup Complete!"
echo "==========================================="