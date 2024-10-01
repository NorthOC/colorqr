from PIL import Image

message = "https://www.reddit.com/"

#with open("f.svg", "r", encoding="utf-8") as f:
#  message = f.read()

representation = [
  (0,   "255 255 255"),
  (1,   "0 0 0"),
  (2,   "255 0 0"),
  (3,   "255 255 0"),
  (4,   "0 255 0"),
  (5,   "0 255 255"),
  (6,   "0 0 255"),
  (7,   "255 0 255")
]

letter_a = ord("H")

#encoding
a_to_system = letter_a // 8
data_in_octary = [a_to_system // 8, a_to_system % 8, letter_a % 8]
print(data_in_octary)
print(representation[data_in_octary[0]], representation[data_in_octary[1]], representation[data_in_octary[2]])

#decoding
data_to_a = data_in_octary[0] * 64 + data_in_octary[1] * 8 + data_in_octary[2]
print(data_to_a)

# 0 - WHITE     (255, 255, 255)
# 1 - BLACK     (0, 0, 0)
# 2 - RED       (255, 0, 0)
# 3 - YELLOW    (255, 255, 0)
# 4 - GREEN     (0, 255, 0)
# 5 - CYAN      (0, 255, 255)
# 6 - BLUE      (0. 0, 255)
# 7 - MAGENTA   (255, 0, 255)

# Representing A (65) ascii to system:
# 512 64 8
#  1  0  1

# Examples:
# 65 -  BLACK WHITE BLACK
# 511 - MAGENTA MAGENTA MAGENTA

# What to encode for decoding?:
# LENGTH OF MESSAGE
# MESSAGE ITSELF
# REPEAT?
# REPRESENTATION?
# INFO TYPE

msg_length = len(message)
msg_length_in_pixels = msg_length * 3
print(f"MESSAGE: {message}")
print(f"LENGTH IN CHARS: {len(message)}")
print(f"NUM OF PIXELS: {msg_length_in_pixels}")

pic_square_size = 0

while pic_square_size * pic_square_size < msg_length_in_pixels:
  pic_square_size += 1

print(f"IMG SQUARE SIZE: {pic_square_size}px")

with open("output.ppm", "wb") as f:
  f.write(bytes(f"P3\n{pic_square_size} {pic_square_size} 255\n", "ascii"))

  buffer = ""
  counter = 0
  for char in message:
    char_in_unicode = ord(char)
    char_to_system = char_in_unicode // 8
    data_in_octary = [char_to_system // 8, char_to_system % 8, char_in_unicode % 8]
    print(data_in_octary)
    buffer += f"{representation[data_in_octary[0]][1]}" + "\n"
    buffer += f"{representation[data_in_octary[1]][1]}" + "\n" 
    buffer += f"{representation[data_in_octary[2]][1]}" + "\n"
    counter += 3
  
  while counter <= pic_square_size * pic_square_size:
    buffer += f"{representation[0][1]}" + "\n"
    counter += 1
  #print(counter)
  f.write(bytes(buffer, "ascii"))



message_in_octary = []
# decoder
im = Image.open('output.ppm', 'r')
width, height = im.size
pixel_values = list(im.getdata())
counter = 0
while counter < msg_length_in_pixels:
  bits = [pixel_values[counter], pixel_values[counter + 1], pixel_values[counter + 2]]
  counter += 3

  data_in_octary = [0, 0, 0]
  idx = 0
  for bit in bits:
    bit_str = f"{bit[0]} {bit[1]} {bit[2]}"
    for code in representation:
      if bit_str == code[1]:
        data_in_octary[idx] = code[0]
        idx += 1
        break
  message_in_octary.append(data_in_octary)

print("DECODED: ", end="")
buffer = ""
counter = 0
while counter < msg_length_in_pixels / 3:
  data_to_a = message_in_octary[counter][0] * 64 + message_in_octary[counter][1] * 8 + message_in_octary[counter][2]
  buffer += chr(data_to_a)
  counter += 1

#with open("decoded.svg", "w", encoding="utf-8") as f:
#  f.write(buffer)
  