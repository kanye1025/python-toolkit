from PIL import Image
import torch
import random
import torchvision.transforms.functional as F
from PIL import Image,ImageStat

class FiveCropNoResize(torch.nn.Module):
	direction = ['top-left', 'top-right', 'bottom-left', 'bottom-right', 'center']
	
	def __init__(self, crop_rate_min=0.75, crop_rate_max=0.9, p=0.5):
		super().__init__()
		self.crop_rate_min = crop_rate_min
		self.crop_rate_max = crop_rate_max
		self.p = p
	
	def forward(self, img):
		if torch.rand(1) > self.p:
			return img
		d = self.direction[random.randint(0, 4)]
		
		crop_rate = random.uniform(self.crop_rate_min, self.crop_rate_max)
		
		if 'center' == d:
			top = img.size[1] * (0.5 - crop_rate / 2)
			bottom = img.size[1] * (0.5 + crop_rate / 2)
			left = img.size[0] * (0.5 - crop_rate / 2)
			right = img.size[0] * (0.5 + crop_rate / 2)
		else:
			if 'top' in d:
				top = 0
				bottom = img.size[1] * crop_rate
			elif 'bottom' in d:
				top = img.size[1] * (1 - crop_rate)
				bottom = img.size[1]
			
			if 'left' in d:
				left = 0
				right = img.size[0] * crop_rate
			elif 'right' in d:
				left = img.size[0] * (1 - crop_rate)
				right = img.size[0]
		
		box = (int(left), int(top), int(right), int(bottom))
		#print(d, box)
		return img.crop(box)
	
	
def pad_to_square( image,fill = 0):
	if fill == 'mean':
		stat = ImageStat.Stat(image)
		fill = (int(stat.mean[0]),int(stat.mean[1]),int(stat.mean[2]))
	size = image.size
	if size[0] != size[1]:
		diff = size[0]-size[1]
		pad = (0,0,0,diff)  if diff>0 else (0,0,-diff,0)
		image  = F.pad(image, pad, fill, 'constant')
	return image


class PadToSquare():
	def __init__(self,fill = 0):
		self.fill = fill

		
	def __call__(self, image):
		return pad_to_square(image,self.fill)