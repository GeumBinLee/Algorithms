from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     answer = 1
    # if len(truck_weights) == 1 :
    #     return bridge_length + 1
    
#     queue = deque(truck_weights)

#     first = queue.popleft()
#     for q in queue :
        
#         if first+q > weight :
#             answer += bridge_length
#             first = q
#         else :
#             first += q
#             answer += 1
                
#     return answer+bridge_length

# def solution(bridge_length, weight, truck_weights):
#     if len(truck_weights) == 1 :
#         return bridge_length + 1
    
#     for i in range(1, len(truck_weights)) :
#         if truck_weights[i] + truck_weights[i-1] <= weight :
#             truck_weights[i-1] = 1
#         else :
#             truck_weights[i-1] = bridge_length
    
#     truck_weights[-1] = 1
#     answer = sum(truck_weights) + bridge_length
#     return answer

solution(100, 100, [10,10,10,10,10,10,10,10,10,10])