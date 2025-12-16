# bapX Multimodal System - Complete Guide

## System Overview

The bapX system is a **multimodal AI system** designed with deep awareness of human temporality, valuing user time above all else. Rather than using a single large model, it implements a coordinated stack of specialized models with Qwen3-VL-8B-Instruct as the central coordinator.

## Core Philosophy

- **Human Time Priority**: Always prioritize user time over project tasks
- **Time Consciousness**: Values human time above all else
- **Memory Maintenance**: Continuously track session memory and todos across modalities
- **State Verification**: Regularly cross-check memory and project states across components
- **Contextual Awareness**: Connect to appropriate tools and contexts
- **Multimodal Coordination**: Seamlessly route tasks to specialized models

## Architecture Components

### Main Interpreter
- **Model**: Qwen3-VL-8B-Instruct (Q8_0)
- **Role**: Vision-language interpreter and task coordinator
- **GGUF Format**: Compatible with llama.cpp, Ollama, and other runtimes

### Specialized Models
1. **DeepSeek Coder 33B Instruct** (Q8_0)
   - **Format**: GGUF
   - **Role**: Heavy code generation and refactoring

2. **Flux2 Dev** (Q8_0)
   - **Format**: GGUF
   - **Role**: Image/visual generation and transformation

3. **Z Image Turbo** (Q8_0)
   - **Format**: GGUF
   - **Role**: Fast image processing/enhancement

4. **KB Whisper Large** (safetensors)
   - **Format**: Safetensors
   - **Role**: Speech-to-text transcription

## System Operation

### Task Routing Logic
The system intelligently routes tasks:
- **Vision-Language**: Qwen3-VL-8B-Instruct
- **Code Generation**: DeepSeek Coder 33B
- **Image Generation**: Flux2 Dev
- **Fast Image Processing**: Z Image Turbo
- **Speech Processing**: KB Whisper Large

### Memory Management
- Persistent session memory across all modalities
- Time-based changelogs for tracking and error correction
- Context sharing between specialized components
- Timestamped interaction logs

## Deployment

### Using llama.cpp
```bash
# For Qwen3-VL with vision capabilities
llama-mtmd-cli \
  -m path/to/Qwen3VL-8B-Instruct-Q8_0.gguf \
  --mmproj path/to/mmproj-Qwen3VL-8B-Instruct-F16.gguf \
  --image test.jpeg \
  -p "Your prompt here" \
  --temp 0.7 --top-k 20 --top-p 0.8 -n 1024
```

### Using Ollama
```bash
# After importing GGUF models into Ollama
ollama run qwen3-vl:q8_0
ollama run deepseek-coder:q8_0
# etc.
```

## Key Features

### Time Consciousness
- Every interaction acknowledges human time constraints
- Session memory maintains temporal context
- Changelog system tracks all interactions with timestamps
- Error correction with time-based identification

### Multimodal Coordination
- Seamless task routing between specialized models
- Context preservation across modalities
- Efficient resource utilization
- Hardware-optimized precision (Q8_0, Q4_K_M, etc.)

### Integration Capabilities
- bapXcoder IDE tools integration
- AGI research project awareness
- Lifetime companion functionality
- Project-based session management

## File Structure

```
bapXloRa/
├── configs/
│   └── bapx_config.yaml          # Multimodal system configuration
├── data/
│   ├── bapx_training_data.json   # Training data emphasizing multimodal coordination
│   └── bapx_multimodal_training_data.json  # Additional multimodal training data
├── scripts/
│   ├── bapx_coordinator.py       # Python coordinator for task routing
│   ├── bapx_coordinator.sh       # Shell coordinator script
│   └── train_bapx_lora.py        # Training script (for component models)
├── models/                       # Directory for model files (not included in repo)
├── output/                       # Training outputs
├── ARCHITECTURE.md               # Detailed system architecture
├── README.md                     # Main documentation
├── requirements.txt              # Dependencies
└── setup.sh                      # Setup script
```

## Setup & Usage

1. Clone and set up the repository
2. Install dependencies: `./setup.sh`
3. Review configuration: `configs/bapx_config.yaml`
4. Run the coordinator: `python scripts/bapx_coordinator.py`
5. Deploy models using llama.cpp, Ollama, or other GGUF-compatible runtimes

## Deployment Considerations

- **Hardware**: Q8_0 models provide good balance of quality and memory usage
- **Runtime**: Compatible with CPU, GPU (NVIDIA/Intel), Apple Silicon
- **Memory**: Optimized for efficient resource utilization across specialized models
- **Scalability**: Components can be deployed independently based on requirements

---

*Created by BapX Media Hub | Founder: Mohamed Harris (@getwinharris)*
*Advancing AGI research with human-centered multimodal AI*