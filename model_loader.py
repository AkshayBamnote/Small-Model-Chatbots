from transformers import pipeline
import torch

def load_model_and_tokenizer_pipeline(model_id, hf_token=None):
    """
    Load a Hugging Face text-generation pipeline.
    """
    return pipeline(
        "text-generation",
        model=model_id,
        tokenizer=model_id,
        device=0 if torch.cuda.is_available() else -1,
        use_auth_token=hf_token,
        pad_token_id=11
    )
