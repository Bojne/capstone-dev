---
slug: code
title: Code Snippets 
authors:
  name: Yueh Han Huang 
  title: Minerva Student 
  url: https://github.com/bojne
  image_url: https://github.com/bojne.png
tags: [code, dev]
---

This file will be my collection of snippets.

Download Youtube Audio
```python
import ffmpeg
stream = ffmpeg.input('Rhye - Full Performance (Live on KEXP).webm')
stream = ffmpeg.output(stream, 'Rhye.wav')
ffmpeg.run(stream)
https://pythonhosted.org/pafy/#pafy-methods
https://github.com/mps-youtube/pafy
```