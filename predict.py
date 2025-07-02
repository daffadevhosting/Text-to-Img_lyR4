from cog import BasePredictor, Input, Path
from diffusers import StableDiffusionPipeline
import torch

class Predictor(BasePredictor):
    def setup(self):
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16
        ).to("cuda")

    def predict(self, prompt: str = Input(description="Prompt")) -> Path:
        image = self.pipe(prompt).images[0]
        output_path = "/tmp/output.png"
        image.save(output_path)
        return Path(output_path)
