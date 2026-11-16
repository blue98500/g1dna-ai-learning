SITES = {
    "해운대" : [35.16, 129.16],
    "서면" : [35.16, 129.06],
    "기장" : [35.24, 129.22],
}

heaundae = SITES["해운대"]
gijang = SITES["기장"]
seomyeon = SITES["서면"]


arrow = [gijang[0] - heaundae[0], gijang[1] - heaundae[1]]
print("해운대 → 기장 화살표:", arrow)
arrow = [seomyeon[0] - heaundae[0], seomyeon[1] - heaundae[1]]
print("해운대 → 서면 화살표:", arrow)

