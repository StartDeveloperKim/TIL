def solution(wallpaper):
    x_s, y_s, x_e, y_e=51, 51, -1, -1
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[x])):
            if wallpaper[x][y] == "#":
                x_s=min(x_s, x)
                y_s=min(y_s, y)
                x_e=max(x_e, x)
                y_e=max(y_e, y)
    
    return [x_s, y_s, x_e+1, y_e+1]
