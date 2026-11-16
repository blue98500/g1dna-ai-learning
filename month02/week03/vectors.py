import math


SITES = {
    "해운대" : [35.16, 129.16],
    "서면" : [35.16, 129.06],
    "기장" : [35.24, 129.22],
}

haeundae = SITES["해운대"]
gijang = SITES["기장"]
seomyeon = SITES["서면"]


arrow = [gijang[0] - haeundae[0], gijang[1] - haeundae[1]]
print("해운대 → 기장 화살표:", arrow)
arrow = [seomyeon[0] - haeundae[0], seomyeon[1] - haeundae[1]]
print("해운대 → 서면 화살표:", arrow)

def distanc(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    return math.sqrt(dx ** 2 + dy **2)

print(f"해운대-서면 : {distanc(SITES['해운대'], SITES['서면']):.3f}")
print(f"해운대-기장 : {distanc(SITES['해운대'], SITES['기장']):.3f}")
print(f"서면-기장 : {distanc(SITES['서면'], SITES['기장']):.3f}")


