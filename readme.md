# Mumoda

![](https://s1.ax1x.com/2022/05/12/OwHzcD.png)

***Mumoda*** is an inference and finetuning library using *Multi-Modality* learning. It already contains some SOTA contractive learning model with multiple modalites. Such as *CLIP, DeCLIP, Coca* etc.

Then main target of **mumoda** is using them for downstream tasks, for instance, text-image, image-caption, or even for object detection etc. To see the big potential of these models transfer to new tasks.

Features **mumoda** supported now:

- [x] CLIP as API (used for quickly encode text, encode image to latent space etc.);
- [ ] DeCLIP as API;
- [x] Guided Diffusion model support;

More features to come, just start and fork **mumoda** !


## Install

*mumoda* is clean and easy to use, it wasn't a iPython notebook for newbies, it was a elegant and powerful lib for researchers. But if you are not interested anything else just want to see the magic, just:

```
pip install -r requirements.txt
python demo.py
```

Be note: if you run CLIP with Diffusion by default, you need at least 12GB GPU memory.


## Models

All models are download from third-party repo. Might add training support in the future.

- `guided-difussion-unconditioned`: [link](https://drive.google.com/file/d/1lvyZZbC9NLcS8a__YPcUP7rDiIpbRpoF/view?usp=sharing);
  


## Copyright

All rights belongs to Lucas Jin 2022.
