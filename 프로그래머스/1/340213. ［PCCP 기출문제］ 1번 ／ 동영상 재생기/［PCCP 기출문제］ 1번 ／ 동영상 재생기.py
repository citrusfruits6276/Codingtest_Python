def solution(video_len, pos, op_start, op_end, commands):
    def time(times):
        m, s = times.split(":")
        return int(m)*60 + int(s)
    
    video_len = time(video_len)
    pos = time(pos)
    op_start = time(op_start)
    op_end = time(op_end)
    
    for i in commands:
        if op_start <= pos <= op_end:
            pos = op_end
            
        if i == "next":
            if pos >= video_len - 10:
                pos = video_len
            else:
                pos += 10
            
        else:
            if pos < 10:
                pos = 0
            else:
                pos -= 10
    if op_start <= pos <= op_end:
            pos = op_end
    
    mm = pos // 60
    ss = pos % 60
        
    return f"{mm:02}:{ss:02}"