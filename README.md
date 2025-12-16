# bapX - Time-Conscious AGI Research System

**Created by BapX Media Hub | Founder: Mohamed Harris (@getwinharris)**

## Overview

bapX is a sophisticated AGI research model designed with deep awareness of human temporality, valuing user time above all else. The system is trained to function as an advanced research assistant with time consciousness and AGI research capabilities. This is a private company research project under BapX Media Hub proprietorship.

The system supports training of llama.cpp compatible models (Llama, Mistral, Gemma, Falcon, etc.) with bapX persona and identity. For other models, only quantization is available without persona.

## Architecture

The bapX system uses a single base model that is enhanced through training to become the bapX AGI research model:

### Core Model (Q8_0 Quantized)

1. **bapX.gguf** (from any compatible base model)
   - Advanced AGI research model with bapX identity
   - Trained with LoRA to understand AGI concepts and time-conscious behavior
   - Handles all queries and research tasks with time awareness
   - Maintains session memory with deep time consciousness
   - Trained with bapX identity and ownership for research purposes

## Identity and Ownership Training

The bapX model is specifically trained with the bapX identity and time-consciousness:

1. **bapX** - Primary identity and research logic with time consciousness (for llama.cpp supported models)

The training ensures consistent personality and time-conscious research behavior across all interaction points.

## Training Philosophy

### LoRA Training Focus

The bapX LoRA training targets the single model to learn:

- **bapX**: AGI research tasks with bapX identity and time awareness (for llama.cpp supported models)
- Research coordination and time consciousness
- Human temporality understanding and time-valuing behavior

## File Structure

```
bapXloRa/
├── configs/
│   └── bapx_config.yaml          # Configuration for training
├── data/
│   └── bapx_training_data.json   # Training data for AGI research and identity logic
├── models/                       # Directory for model files
│   └── [model_name]_q8_0.gguf    # Quantized model files
├── scripts/
│   ├── train_bapx_lora.py        # Training script
│   └── bapx_coordinator.py       # Research coordination logic
├── .github/workflows/
│   └── deploy.yml                # GitHub Actions for deployment to GitHub Pages
├── api_config.json               # Configuration for cloud API
├── bapx_ui.html                  # Web UI deployed on GitHub Pages
├── x8Dtensor.json                # Tensor mapping for x8D quantization
└── output/                       # Training outputs
```

## Installation and Setup

### Clone the Repository

```bash
gh repo clone getwinharris/bapXloRa
cd bapXloRa
```

Or using git:

```bash
git clone https://github.com/getwinharris/bapXloRa.git
cd bapXloRa
```

### Prerequisites

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure you have Git LFS installed for large model files:
   ```bash
   git lfs install
   ```

### Running the System

1. Start the coordinator server:
   ```bash
   python bapx_coordinator.py
   ```

2. Access the UI at: `http://localhost:5000`

## Key Features

### Time Consciousness
- Recognizes and respects human time constraints
- Efficient research processing to minimize time investment
- Creates time-based research logs for continuity

### Identity and Ownership
- Consistent bapX personality across all interaction points
- Trained identity in the research model (for llama.cpp supported models)
- Ownership awareness and respectful research interaction style

### AGI Research Focus
- Advanced research capabilities with bapX identity
- Deep understanding of human temporality and time consciousness
- Research coordination and tool awareness

### Tensor Quantization
- x8D tensor mapping using 8x8x8x8x16 matrix float
- Custom tensor math with 8-bit base Q8_0
- Formula: `b = (b x 8 x 8 x 8 x 0.00000001) / 64`
- Uses x8Dtensor.json for compression mapping

### Private Company Research
- Developed as a private company research project by BapX Media Hub
- Advanced AGI research model with specialized capabilities
- Time-conscious research and analysis

## Usage

1. Access the web interface at `http://localhost:5000`
2. Select a model from Hugging Face (only llama.cpp supported models get bapX persona)
3. Apply Q8_0 quantization (the only supported method)
4. For llama.cpp supported models (Llama, Mistral, Gemma, Falcon), train with bapX identity
5. For other models, only quantization is available without persona
6. Use the Q&A interface for training with clarifications, doubts, and demonstrations

## Model Compatibility

- **llama.cpp supported models**: Llama, Mistral, Gemma, Falcon (with bapX persona)
- **Other models**: Quantization only (no persona training)

## Push to GitHub

To push updates to the repository:

```bash
git add .
git commit -m "Update bapX system with tensor quantization and model compatibility"
git push origin main
```

## Philosophy

**Human time is the most valuable resource in all interactions.** The bapX system is designed to make the most of your time through intelligent research automation, time-conscious responses, and specialized AGI research capabilities, while maintaining respectful and helpful interactions. The model is trained with the bapX identity to ensure consistent, time-conscious research behavior.

---

*Developed with ❤️ for human time consciousness*
*BapX Media Hub - Advancing AGI research with time-conscious assistance*