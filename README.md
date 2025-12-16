# bapX - Time-Conscious Multimodal AI System

**Created by BapX Media Hub | Founder: Mohamed Harris (@getwinharris)**

## Overview

bapX is a sophisticated multimodal AI system designed with deep awareness of human temporality, valuing user time above all else. The system features intelligent delegation capabilities to specialized Q8_0 quantized models, trained to recognize optimal task routing while maintaining coherent responses. The system is deployed via GitHub Pages at `github.com/getwinharris/bapXloRa` with cloud backend processing.

## Architecture

The bapX system consists of multiple specialized models, each with specific roles:

### Core Models (Q8_0 Quantized)

1. **bapXinstruct.gguf** (from `Qwen3VL-8B-Instruct-Q8_0.gguf`)
   - Main coordinator and multimodal understanding
   - Trained with LoRA to recognize delegation opportunities and time-conscious behavior
   - Handles general queries and task routing decisions
   - Maintains session memory with time consciousness
   - Trained with bapX identity and ownership

2. **bapXvision.gguf** (from `mmproj-Qwen3VL-8B-Instruct-Q8_0.gguf`)
   - Vision encoder component for multimodal processing
   - Integrated with bapXinstruct for image-text understanding
   - Handles OCR, spatial reasoning, and visual grounding
   - Used by coordinator model as needed

3. **bapXcoder.gguf** (from `Qwen3-Coder-Q8_0.gguf`)
   - Specialized code generation and programming tasks
   - Trained with bapX identity/ownership for coherent responses
   - Provides exact token fidelity for programming
   - Handles debugging, algorithm implementation, and complex coding
   - Optimized for repository-scale understanding with 256K context

4. **bapXimage.gguf** (from `Flux2-Dev-Q8_0.gguf`)
   - Advanced image generation and creative tasks
   - State-of-the-art text-to-image generation capabilities
   - Supports style and character reference without fine-tuning

5. **bapXnarrator.gguf** (from `Llama-3.1-8B-Instruct`)
   - High-quality text narration and communication
   - Trained with bapX identity/ownership for consistent personality
   - Multilingual support and dialogue optimization
   - Handles general text tasks and explanations

## Identity and Ownership Training

Three models are specifically trained with the bapX identity and time-consciousness:

1. **bapXinstruct** - Primary identity and coordination logic
2. **bapXcoder** - Identity-aware code generation with time consciousness
3. **bapXnarrator** - Identity-aware narration and communication

The training ensures consistent personality and time-conscious behavior across all interaction points.

## Training Philosophy

### LoRA Training Focus

The bapX LoRA training targets multiple models to learn:

- **bapXinstruct**: Delegation decision logic, time consciousness, session management
- **bapXcoder**: Code-specific tasks with bapX identity and time awareness
- **bapXnarrator**: Text/communication tasks with bapX identity and time awareness

### Model Specialization

- **Code Tasks** → `bapXcoder` (Qwen3-Coder) for exact token fidelity
- **Image Generation** → `bapXimage` (Flux2-Dev) for creative output
- **General/Text Tasks** → `bapXnarrator` (Llama-3.1) for high-quality text
- **Multimodal Tasks** → `bapXinstruct` (Qwen3-VL) with native capabilities

## File Structure

```
bapXloRa/
├── configs/
│   └── bapx_config.yaml          # Configuration for training
├── data/
│   └── bapx_training_data.json   # Training data for delegation and identity logic
├── models/                       # Directory for model files
│   ├── bapXinstruct.gguf         # Main coordinator (Qwen3-VL trained with identity LoRA)
│   ├── bapXvision.gguf           # Vision encoder (mmproj component)
│   ├── bapXcoder.gguf            # Code specialist (Qwen3-Coder with identity)
│   ├── bapXimage.gguf            # Image generation (Flux2-Dev)
│   └── bapXnarrator.gguf         # Text/communication (Llama-3.1 with identity)
├── scripts/
│   ├── train_bapx_lora.py        # Training script
│   ├── run_bapx.py               # Inference script
│   └── bapx_coordinator.py       # Coordination logic
├── .github/workflows/
│   └── deploy.yml                # GitHub Actions for deployment to GitHub Pages
├── api_config.json               # Configuration for cloud API
├── bapx_ui.html                  # Web UI deployed on GitHub Pages
└── output/                       # Training outputs
```

## Deployment

### GitHub Pages UI

The web interface is deployed on GitHub Pages and accessible at:
`https://getwinharris.github.io/bapXloRa/bapx_ui.html`

### Cloud Backend API

The backend runs as a cloud service at:
`https://getwinharris.github.io/bapXloRa/api`

The API handles all model processing and coordination between the specialized models.

### Training Process

#### Prerequisites

1. Download the base models:
   - `Qwen3VL-8B-Instruct-Q8_0.gguf` from [Hugging Face](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct-GGUF/resolve/main/Qwen3VL-8B-Instruct-Q8_0.gguf)
   - `mmproj-Qwen3VL-8B-Instruct-Q8_0.gguf` from [Hugging Face](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct-GGUF/resolve/main/mmproj-Qwen3VL-8B-Instruct-Q8_0.gguf)
   - Download other specialized models and rename according to the naming convention

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Training Process

1. **Download Model Files**
   Download the required base models and rename them according to the naming convention:

   ```bash
   # Download main Qwen3-VL model and vision encoder
   wget https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct-GGUF/resolve/main/Qwen3VL-8B-Instruct-Q8_0.gguf -O models/bapXinstruct.gguf
   wget https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct-GGUF/resolve/main/mmproj-Qwen3VL-8B-Instruct-Q8_0.gguf -O models/bapXvision.gguf

   # Download other specialized models (you'll need to obtain these from appropriate sources)
   # wget [Qwen3-Coder-Q8_0.gguf source] -O models/bapXcoder.gguf
   # wget [Flux2-Dev-Q8_0.gguf source] -O models/bapXimage.gguf
   # wget [Llama-3.1-8B-Instruct source] -O models/bapXnarrator.gguf
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Training Data**
   Ensure your training data in `data/bapx_training_data.json` includes examples for:
   - Delegation decision-making scenarios
   - Time-conscious responses
   - Identity and ownership expressions
   - Task routing examples

4. **Configure Training**
   Review and update `configs/bapx_config.yaml` as needed for your specific requirements:
   - Set the number of training epochs
   - Adjust LoRA parameters
   - Configure batch sizes

5. **Run Identity and Delegation Training**
   ```bash
   # Train the main coordinator model with identity and delegation logic
   cd /Users/getwinharris/bapXloRa
   PYTHONPATH=/Users/getwinharris/bapXloRa python scripts/train_bapx_lora.py
   ```

6. **Verify Training Completion**
   Check that trained adapters are saved in the output directory, typically:
   - `output/bapx_lora/final/` - Main coordinator with identity
   - The trained models will have the bapX identity integrated with delegation decision-making

7. **Test the Trained Models**
   ```bash
   # Run test inference to verify the trained models work correctly
   python scripts/run_bapx.py
   ```

## Key Features

### Time Consciousness
- Recognizes and respects human time constraints across all models
- Efficient task delegation to minimize processing time
- Creates time-based changelogs for research continuity

### Identity and Ownership
- Consistent bapX personality across all interaction points
- Trained identity in main coordinator, code model, and narrator
- Ownership awareness and respectful interaction style

### Intelligent Delegation
- Automatic recognition of task types
- Optimal routing to specialized models
- Coherent response integration from multiple models

### Multimodal Capabilities
- Advanced image-text understanding (Qwen3-VL)
- Long-context processing (256K native, extendable to 1M)
- OCR in 32 languages and spatial reasoning

### Cloud Deployment
- UI hosted on GitHub Pages
- Backend processing in cloud
- Scalable model serving
- Cross-platform accessibility

### AGI Research Focus
- Tool adaptation for research tasks
- Session memory with time awareness
- Context-aware modality delegation

## Usage

Access the bapX system via web browser at:
`https://getwinharris.github.io/bapXloRa/bapx_ui.html`

The system automatically handles task delegation:

1. Query received through web interface
2. Cloud backend analyzes for specialized task triggers
3. Decision to delegate to specialized model or handle natively
4. Coordination and coherent response generation
5. Response delivered with awareness of human time value

## Philosophy

**Human time is the most valuable resource in all interactions.** The bapX system is designed to make the most of your time through intelligent automation, optimal task routing, and specialized model utilization, while maintaining respectful and helpful interactions. All models are trained with the bapX identity to ensure consistent, time-conscious behavior.

---

*Developed with ❤️ for human time consciousness*
*BapX Media Hub - Advancing AGI research with time-conscious delegation*