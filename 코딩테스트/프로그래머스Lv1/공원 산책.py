def solution(park, routes):
    park=[list(p) for p in park]
    x_len, y_len=len(park), len(park[0])
    
    now=[]
    for i in range(len(park)):
        if 'S' in park[i]:
            now=[i, park[i].index('S')]
            park[i][now[1]]='O'
            break
            
    four_dir={'E':[0, 1], 'N':[-1, 0], 'S':[1, 0], 'W':[0, -1]}
    next_pos=now.copy()
    for route in routes:
        direct, dist=route.split(" ")
        next_pos[0], next_pos[1]=now[0], now[1]
        for _ in range(int(dist)):
            next_pos=[next_pos[0]+four_dir[direct][0], next_pos[1]+four_dir[direct][1]]
            if (0<=next_pos[0]<x_len and 0<=next_pos[1]<y_len) and park[next_pos[0]][next_pos[1]]!='X':
                continue
            else:
                break
        else:
            now[0], now[1]=next_pos[0], next_pos[1]        
            
    
    return now
