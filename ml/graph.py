

def overlap_rect(rect1,rect2):
	'''
	
	:param rect1: 矩形1 （left,top,right,bottom）
	:param rect2: 矩形2 （left,top,right,bottom）
	:return: 重叠矩形 (left,top,right,bottom)
	'''
	
	left_o = max(rect1[0],rect2[0])
	right_o = min(rect1[2], rect2[2])
	top_o = max(rect1[1], rect2[1])
	bottom_o = min(rect1[3], rect2[3])
	if left_o>right_o or top_o>bottom_o: #不重合
		return None
	return (left_o,top_o,right_o,bottom_o)

def rect_area(rect):
	'''
	
	:param rect:矩形 （left,top,right,bottom）
	:return: numerical
	'''
	left, top, right, bottom = rect
	return (bottom-top)*(right-left)

