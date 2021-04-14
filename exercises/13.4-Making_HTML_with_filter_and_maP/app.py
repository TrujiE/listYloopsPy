all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li(nombre):
    li_tag='</li>'
    li_tag2="<li>"
    print(li_tag2+ nombre+ li_tag)
    

def filter_colors():
    return color==Red


genera_li=list(filter(lambda nombres : nombres["sexy"], all_colors))
filtro_li=list(map(lambda color : color["label"],genera_li))
li = list(map(generate_li,filtro_li))

