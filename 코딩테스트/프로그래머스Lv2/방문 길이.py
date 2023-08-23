def solution(dirs):
    answer = 0
    command={'U':[0, 1], 'D':[0, -1], 'R':[1, 0], 'L':[-1, 0]}
    routes=[]
    
    location=[0, 0]
    for dir in dirs:
        nx=location[0]+command[dir][0]
        ny=location[1]+command[dir][1]
        if (nx>-6 and nx<6) and (ny>-6 and ny<6):
            route=''.join(list(map(str, location+[nx, ny])))
            reverseRoute=''.join(list(map(str, [nx, ny]+location)))
            location=[nx, ny]
            if route not in routes and reverseRoute not in routes:
                routes.append(route)
                routes.append(reverseRoute)
                answer+=1
    return answer
