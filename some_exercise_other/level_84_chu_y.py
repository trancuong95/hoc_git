chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "Yêu"]
tan_ngu = ["Bóng đá", "Xếp hình"]
for i in range(0, 2):
    for j in range(0, 2):
        for k in range(0, 2):
            cau = '%s %s %s.' % (chu_ngu[i], dong_tu[j], tan_ngu[k])
            # chú ý câu lệnh trên
            print(cau)
