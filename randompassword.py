import random
import string
uzunluk = 53
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
space = " "
all = lower + upper + num + symbols + space
temp = random.sample(all, uzunluk)
password = "".join(temp)
print(password)