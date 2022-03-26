**A fork of lf-gadgets with better video thumbnails**

For the original lf-gadgets documentation see https://github.com/slavistan/lf-gadgets .

# Introduction

I use lf-ueberzug to get a preview of documents in command line which works pretty well for images and PDF files. However, for video files, pretty often I get something like this:

![2022-03-26_22-39](https://user-images.githubusercontent.com/6392321/160252076-16c9f094-7d4b-43a5-8c60-da42d57a0556.png)

Now you'd be excused for thinking that the preview feature is not active in this image. Unfortunately `lf-ueberzug` by default uses the first frame of the video which is usually completely black. In this fork we use the middle frame of the video instead, which looks much better:

![2022-03-26_22-35](https://user-images.githubusercontent.com/6392321/160252221-9691a134-534d-4303-ba47-9ffd13d95151.png)

# Instructions

Installation is pretty much like original `lf-ueberzug`, however we need `ffmpeg` for python:
```
python3 -m pip install ffmpeg-python
```
