
def in_interval(outer_interval:list[int],inner_interval:list[int]):
    if outer_interval[0]<=inner_interval[0]:
        if inner_interval[1]<=outer_interval[1]:
            return inner_interval[1]-inner_interval[0]
        else:
            if inner_interval[0]<outer_interval[1]:
                return outer_interval[1]-inner_interval[0]
            else:
                return 0
    else:
        if inner_interval[1]>outer_interval[0]:
            if inner_interval[1]<=outer_interval[1]:
                return inner_interval[1]-outer_interval[0]
            else:
                return outer_interval[1]-outer_interval[0]
        else:
            return 0

def cut_interval(outer_interval:list[int],inner_interval:list[int]):
    if outer_interval[0]<=inner_interval[0]:
        if inner_interval[1]>outer_interval[1]:
            inner_interval[1]=outer_interval[1]
    else:
        if inner_interval[1]>outer_interval[0]:
            if inner_interval[1]<=outer_interval[1]:
                inner_interval[0]=outer_interval[0]
    return inner_interval
def concat_intervals(first_interval:list[int],second_interval:list[int]):
    new_interval=[0,0]
    if first_interval[0]<=second_interval[0]:
        if first_interval[1]<=second_interval[0]:
            return 0
        else:
            if first_interval[1]<=second_interval[1]:
                new_interval[1]=second_interval[1]
                new_interval[0]=first_interval[0]
                return new_interval
            else:
                return first_interval
    else:
        if second_interval[1]<=first_interval[0]:
            return 0
        else:
            if second_interval[1]<=first_interval[1]:
                new_interval[1] = first_interval[1]
                new_interval[0] = second_interval[0]
                return new_interval
            else:
                return second_interval

def appearance(intervals: dict[str, list[int]]) -> int:
        result_time=0
        lesson_interval = [intervals['lesson'][0],intervals['lesson'][1]]
        pupil_intervals = [[intervals['pupil'][i],intervals['pupil'][i+1]] for i in range(0, len(intervals['pupil']),2)]
        tutor_intervals = [[intervals['tutor'][i],intervals['tutor'][i+1]] for i in range(0, len(intervals['tutor']),2)]
       # print(lesson_interval)
       # print(pupil_intervals)
       # print(tutor_intervals)
        i=0
        #for i in range(0,len(pupil_intervals)-2):
        while i<=len(pupil_intervals)-2:
            #print('i='+str(i))
           # if i in deleted_index:
           #     continue
           # print(len(pupil_intervals))
            j=len(pupil_intervals)-1
            while j!=i:
            #for j in range(len(pupil_intervals)-1,i,-1):
                #print(pupil_intervals)
                #print(j)
               # if j in deleted_index:
               #     continue
                if concat_intervals(pupil_intervals[i],pupil_intervals[j])!=0:
                    pupil_intervals[i]=concat_intervals(pupil_intervals[i],pupil_intervals[j])
                    pupil_intervals.pop(j)
                    j=len(pupil_intervals)
                    #print(j)
                j=j-1
            i=i+1
        i = 0
        while i <= len(tutor_intervals) - 2:
            j = len(tutor_intervals) - 1
            while j != i:
                if concat_intervals(tutor_intervals[i],tutor_intervals[j])!=0:
                    tutor_intervals[i]=concat_intervals(tutor_intervals[i],tutor_intervals[j])
                    tutor_intervals.pop(j)
                    j=len(tutor_intervals)
                j = j - 1
            i = i + 1

        for pupil_int in pupil_intervals:
           # print(pupil_int)
          # print(type(pupil_int[1]))
           # print(type(lesson_interval[1]))
            if in_interval(lesson_interval,pupil_int)!=0:
                for tutor_int in tutor_intervals:
                    print(pupil_int)
                    print(cut_interval(lesson_interval,pupil_int))
                    print(tutor_int)
                    add_time=in_interval(cut_interval(lesson_interval,pupil_int),tutor_int)
                    print(add_time)
                    if tutor_int[0]<lesson_interval[1]:
                        result_time=result_time+add_time
                        print(result_time)
                    else:
                        break
            else:
                break
        print(result_time)
        return result_time
tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
    #print (test_answer)
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

