#!/usr/bin/env python3

segments_in = [[-1, 3],
            [-5, -3],
            [3, 5],
            [2, 4],
            [-3, -2],
            [-1, 4],
            [5, 5]]

def solution(segments):
    
    #Define NumChoice as class for storing relevant values
    class NumChoice:
        def __init__(self, value, occurences, segm):
            self.value = value
            self.occurences = occurences
            self.segm = segm
    
    #Define range of numbers to search
    temp_min = segments[0][0]
    temp_max = segments[0][1]
    for i in range(1,len(segments)):
        if segments[i][0] < temp_min:
            temp_min = segments[i][0]
        if segments[i][1] > temp_max:
            temp_max = segments[i][1]
    
    #Define NumChoice class object with values in range
    x = list(range(temp_min, temp_max+1))
    y = [0] * len(x)
    z = [-1] * len(x)
    ncAll = NumChoice(x,y,z)

    #Define starting set of segments as full set
    temp_segments = segments[0:len(segments)]

    #Define output search parameters
    out_vals = []
    segs_inc_sum = 0

    #With iteration until all segments are included
    while segs_inc_sum < len(segments):

        # add values by which is in most remaining segments
        for each in range(0, len(ncAll.value)):
            for s in range(0,len(temp_segments)):
                r = range(temp_segments[s][0],temp_segments[s][1]+1)
                if ncAll.value[each] in r:
                    ncAll.occurences[each] += 1
                    if ncAll.segm[each] == -1:
                        ncAll.segm[each] = [s]
                    else:
                        ncAll.segm[each].append(s)
        
        # identify index of maximum occurences
        new_val_index = ncAll.occurences.index(max(ncAll.occurences))
        # add new value to output list
        out_vals.append(ncAll.value[new_val_index])
        # add number of segments included in output values
        # will terminate here if all are included
        segs_inc_sum += max(ncAll.occurences)
        
        # if not all are included yet,
        # remove already included segments from subsequent search
        segs_remove = ncAll.segm[new_val_index]
        segs_remove.reverse()
        for rem in segs_remove:
            temp_segments.pop(rem)

        # remove value and reset NumChoice object
        ncAll.value.pop(new_val_index)
        ncAll.occurences = [0] * len(ncAll.value)
        ncAll.segm = [-1] * len(ncAll.value)

    
    #Return output values
    return(out_vals)


s = solution(segments_in)

print(s)

        
