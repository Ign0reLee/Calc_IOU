import numpy

def calc_(Box1, Box2):
    
    #input two Box ([label, x1,y1,w1,h1], [label, x2,y2,w2,h2])
    
    #calc each point
    box1_x1 = Box1[1]
    box1_y1 = Box1[2]
    box1_w = Box1[3]
    box1_h = Box1[4]
    box1_x2 = box1_x1 + box1_w
    box1_y2 = box1_y1 + box1_h
    

    box2_x1 = Box2[1]
    box2_y1 = Box2[2]
    box2_w = Box2[3]
    box2_h = Box2[4]
    box2_x2 = box2_x1 + box2_w
    box2_y2 = box2_y1 + box2_h

    
    
    #절대 겹칠 수 없는 경우
    if Box1[0] != Box2[0]: return 0
    if box1_x1 > box2_x2: return 0
    if box2_x1 > box1_x2: return 0
    if box1_y1 > box2_y2: return 0
    if box2_y1 > box1_y2: return 0
    
    #계산하기
    cross_x = max(box1_x1, box2_x1)
    cross_y = max(box1_y1, box2_y1)
    cross_w = min(box1_x2, box2_x2) - cross_x
    cross_h = min(box1_y2, box2_y2) - cross_y
    
    #계산 부분
    
    Area_of_overlap = cross_w * cross_h
    Area_of_union = ((box1_w * box1_h) + (box2_w * box2_h)) - Area_of_overlap
    
    return Area_of_overlap / Area_of_union
