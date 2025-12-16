#!/bin/bash
# Comprehensive Setup Script for bapX AGI Research System

set -e  # Exit on any error

echo "==========================================="
echo "Setting up bapX - Time-Conscious AGI Research System"
echo "Created by BapX Media Hub | @getwinharris"
echo "==========================================="

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
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
    pip install transformers peft bitsandbytes accelerate datasets trl pyyaml huggingface_hub sentencepiece tokenizers safetensors pillow
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

echo ""
echo "Setup complete!"
echo ""
echo "Next Steps:"
echo "1. Review configs/bapx_config.yaml to understand the AGI research architecture"
echo "2. Check ARCHITECTURE.md for complete system overview"
echo "3. Run coordinator: python scripts/bapx_coordinator.py"
echo "4. Use the system with llama.cpp, Ollama, or other GGUF-compatible runtimes"
echo ""
echo "Remember: bapX is designed with deep time consciousness and human time valuation"
echo "as a single AGI research model based on Llama 3, always prioritizing human time in all operations."
echo ""

echo "==========================================="
echo "bapX AGI Research System Setup Complete!"
echo "==========================================="