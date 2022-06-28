from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2

# Settings
#W, H = (224, 224)

# Font 字型
#font = ImageFont.load_default("D://Users//xkllkx//Desktop//all_program//text_2_picture//Pixel.ttf")
font = ImageFont.truetype("D://Users//xkllkx//Desktop//all_program//picture_2_movie//Silver.ttf", 24, encoding='utf-8')
font = ImageFont.truetype("Silver.ttf",60)
#font = ImageFont.load_default()


im = Image.open("w_g_model.jpg")
#im=Image.new("RGBA", (500,250),(248,247,216)) #生成空白頁

draw = ImageDraw.Draw(im)

def blood_lengh1_decrease(image,start_XY,end_XY,full_blood,current_blood):
    thick=2

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]) , (start_XY[0] , start_XY[1]+thick)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (66,62,63))

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]+thick) , (start_XY[0] , start_XY[1]+thick*2)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (65,77,67))

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]+thick*2) , (start_XY[0] , start_XY[1]+10)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (79,108,86))

def blood_lengh2_decrease(image,start_XY,end_XY,full_blood,current_blood):
    
    thick=2
    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]) , (start_XY[0] , start_XY[1]+thick)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (66,62,63))

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]+thick) , (start_XY[0] , start_XY[1]+thick*2)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (65,77,67))

    shape = [(end_XY[0] + ((start_XY[0] - end_XY[0]) * (current_blood / full_blood)),end_XY[1]+thick*2) , (start_XY[0] , start_XY[1]+8)]  #用扣血的
    ImageDraw.Draw(image).rectangle(shape, fill = (79,108,86))

def blood_num(image,start_XY,full_blood,current_blood,font):
    ImageDraw.Draw(image).text((start_XY[0],start_XY[1]), f'{current_blood}/ {full_blood}' ,(71,68,53), font=font,align = "left")


player1_start_XY = [976,268] #XY #主角血條位置右
player1_end_XY = [751,268] #左

player2_start_XY = [403,63] #XY #對手血條位置右
player2_end_XY = [180,63] #左

num_start_XY = [868,279] #左上 #數字顯示

#血量
player1_full_blood = 20
player1_current_blood = 10

player2_full_blood = 20
player2_current_blood = 10

blood_lengh1_decrease(im,player1_start_XY,player1_end_XY,player1_full_blood,player1_current_blood)
blood_lengh2_decrease(im,player2_start_XY,player2_end_XY,player2_full_blood,player2_current_blood)

#影片幀率
picture_num = 50
twinkle_num = 4 #閃爍算2次

picture_name = 0

#資料夾名稱
filename = "w_g_bb_2"

#閃爍
black = Image.open("black.jpg")
twinkle = 0

while twinkle <= twinkle_num:
    stay = 5 #停留時常
    if twinkle % 2 != 0:
        for j in range(stay):
            black.save(f"D://Users//xkllkx//Desktop//all_program//picture_2_movie//{filename[0:3]}//{filename}//{picture_name}.png","png")
            picture_name+=1
        twinkle+=1
    else:
        for j in range(stay):
            im.save(f"D://Users//xkllkx//Desktop//all_program//picture_2_movie//{filename[0:3]}//{filename}//{picture_name}.png","png")
            picture_name+=1
        twinkle+=1


#扣血
player1_current_blood = 0
# player2_current_blood = 10

blood_num(im,num_start_XY,player1_full_blood,player1_current_blood,font)

i=0
while i <= picture_num:
    player1_blood_decrease = (player1_full_blood - player1_current_blood)/picture_num
    # player2_blood_decrease = (player2_full_blood - player2_current_blood)/picture_num

    blood_lengh1_decrease(im,player1_start_XY,player1_end_XY,player1_full_blood,player1_full_blood-player1_blood_decrease*i)
    # blood_lengh2_decrease(im,player2_start_XY,player2_end_XY,player2_full_blood,player2_full_blood-player2_blood_decrease*i)

    im.save(f"D://Users//xkllkx//Desktop//all_program//picture_2_movie//{filename[0:3]}//{filename}//{picture_name+i}.png","png")
    i+=1
    # im.show()

#最後停留
picture_name = picture_name+i
for j in range(stay):
    im.save(f"D://Users//xkllkx//Desktop//all_program//picture_2_movie//{filename[0:3]}//{filename}//{picture_name}.png","png")
    picture_name+=1

#影片
size = (1009,348) #圖片大小
print(size)

#完成寫入物件的建立，第一個引數是合成之後的影片的名稱，第二個引數是可以使用的編碼器，第三個引數是幀率即每秒鐘展示多少張圖片，第四個引數是圖片大小資訊
videowrite = cv2.VideoWriter(f'D://Users//xkllkx//Desktop//all_program//picture_2_movie//{filename[0:3]}//{filename}//test.mp4',-1,20,size)#20是幀數，size是圖片尺寸
img_array=[]

for filename in [f'D://Users//xkllkx//Desktop//all_program//picture_2_movie//{filename[0:3]}//{filename}//{k}.png' for k in range(picture_name)]:
    img = cv2.imread(filename)
    if img is None:
        print(filename + " is error!")
        continue
    img_array.append(img)

for k in range(picture_name):
    videowrite.write(img_array[k])
print('end!')