import simple_draw as sd

x_list = []
y_list = []
length_list = []
color_list_dist = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE,
                   sd.COLOR_PURPLE]
color_list = []


def create_snowflakes(_N):
    for i in range(_N):
        x_list.append(sd.random_number(30, 600))
        y_list.append(sd.random_number(550, 1500))
        length_list.append(sd.random_number(5, 20))
        color_list.append(color_list_dist[sd.random_number(0, 6)])


def displace_snowflakes():
    for _i in range(len(x_list)):
        # if 110 > y_list[_i] > 80:
        #     x_list.append(sd.random_number(30, 600))
        #     y_list.append(sd.random_number(550, 1500))
        #     length_list.append(sd.random_number(5, 20))
        y_list[_i] -= 30
        x_list[_i] += sd.random_number(-15, 15)


def drawing_snowflake(_color=False):
    sd.start_drawing()
    for i in range(len(x_list)):
        point = sd.get_point(x_list[i], y_list[i])
        if not _color:
            sd.snowflake(center=point, length=length_list[i], color=sd.background_color)
        else:
            sd.snowflake(center=point, length=length_list[i], color=color_list[i])
    sd.finish_drawing()


def check_snowflakes():
    del_snowflakes = []
    for i in range(len(y_list)):
        if y_list[i] <= 0:
            del_snowflakes.append(i)
    return del_snowflakes


def delete_snowflakes(_del_snowflakes):
    for i in _del_snowflakes:
        x_list.pop(i)
        y_list.pop(i)
        length_list.pop(i)
        color_list.pop(i)

