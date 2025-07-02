from diffusers import StableDiffusionPipeline
import torch

class Predictor:
    def setup(self):
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16
        ).to("cuda")

    def predict(self, prompt: str) -> str:
        image = self.pipe(prompt).images[0]
        image.save("output.png")
        return "output.png"