from mumoda.encoders.clip import clip
from mumoda.encoders.utils import parse_prompt
from alfred import device


clip_model, _ = clip.load("ViT-B/16", jit=False)
clip_model.eval().requires_grad_(False).to(device)

prompt = "a cat stand on the sky"
txt, weight = parse_prompt(prompt)
t_inp = clip.tokenize(prompt).to(device)
print(t_inp)
txt_latent = clip_model.encode_text(t_inp).float()
print(txt_latent.shape)
