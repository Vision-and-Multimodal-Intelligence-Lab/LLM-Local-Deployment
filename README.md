# LLM-Local-Deployment

This repository contains example code demonstrating how to use department self-deployed DeepSeek R1 distillation models via API.

## Overview

The repository provides sample code for interacting with locally deployed Large Language Models (LLMs) using both Python scripts. The examples demonstrate various API interaction patterns including standard requests, streaming, and multi-turn conversations.

## Available Models

The department has deployed the following models which can be accessed through the API:

- DeepSeek-R1-Distill-Llama-70B (Port: `50000`)
- DeepSeek-R1-Distill-Qwen-14B (Port: `50001`)

## Getting Started

### Prerequisites

- API key (register to obtain your key)
- `openai` Python package

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/Vision-and-Multimodal-Intelligence-Lab/LLM-Local-Deployment.git
   cd LLM-Local-Deployment
   ```

2. Install the required dependencies:
   ```
   pip install openai
   ```

## Configuration

Before using the examples, you need to set three key variables:

- `HOST`: The host address of the deployed models
- `PORT`: The port number for the specific model you want to access (50000 for Llama-70B or 50001 for Qwen-14B)
- `API_KEY`: Your personal API key for authentication

## Usage Examples

The repository provides examples using the OpenAI client library, which offers a convenient interface for interacting with the models.

### Key Features Demonstrated

The examples showcase several important features:

1. **Standard (Non-streaming) Completions**: Get the full response at once
2. **Streaming Responses**: Process the response as it's being generated
3. **Multi-turn Conversations**: Maintain context over multiple exchanges
4. **Reasoning Content**: Access the model's reasoning process separately from its final output
5. **Python Requests Alternative**: Examples using the lower-level requests library

## Example Files

- [`example_LLM_API_call.py`](example_LLM_API_call.py): A Python script demonstrating API interactions.
- [`example_LLM_API_call.ipynb`](example_LLM_API_call.ipynb): A Jupyter notebook provides step by step instructions.

## Tips

- Experiment with different `system prompts` to tailor the model's behavior
- Adjust `temperature` and `top_p` parameters to control response randomness/creativity
- For real-time applications, use `streaming` to improve user experience
- The reasoning_content can be valuable for debugging or educational applications

## Support

For issues or questions specific to the hackathon, please contact the event organizers.

## License

See the [LICENSE](LICENSE) file for details.
