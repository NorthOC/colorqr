# ColorQR - 8 bit QR codes

![](/encoding.png)

A prototype for future QR codes.

Watched a video and decided to mess around with encoding information. This is the idea I came up with. The colors used to respresent data are White, Black, RGB and CMY, giving us a total 512 bits of storage per 3 pixels (8x8x8).

So, to encode a single pixel with ColorQR only takes 3 pixels, while a QR code requires 8 pixels. Basically, giving us a 62.5% more efficient QR code!

What you see in the picture above, is raw data encoded using ColorQR. Further implementation of error-correction and metadata needed, to make it a viable alternative.

References: 

* [https://www.youtube.com/watch?v=w5ebcowAJD8](https://www.youtube.com/watch?v=w5ebcowAJD8)

## Representation table

|Bits|Color      |Color val.        |
|----|-----------|------------------|
|0   | WHITE     |(255, 255, 255)   |
|1   | BLACK     |(0, 0, 0)         |
|2   | RED       |(255, 0, 0)       |
|3   | YELLOW    |(255, 255, 0)     |
|4   | GREEN     |(0, 255, 0)       |
|5   | CYAN      |(0, 255, 255)     |
|6   | BLUE      |(0. 0, 255)       |
|7   | MAGENTA   |(255, 0, 255)     |