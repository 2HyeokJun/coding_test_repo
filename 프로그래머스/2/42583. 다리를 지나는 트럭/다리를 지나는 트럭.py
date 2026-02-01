class Truck:
    def __init__(self, weight):
        self.weight = weight
        self.position = 0

    def move(self):
        self.position += 1

    def is_arrived(self, length):
        return self.position == length + 1
    
    def __repr__(self):
        return f"Truck({self.weight}, {self.position})"
    
def move_truck(from_array, to_array):
    truck = from_array.pop(0)
    to_array.append(truck)


def solution(bridge_length, weight, truck_weights):
    answer = 0
    weight_in_bridge = 0
    trucks_in_bridge = []
    finished_trucks = []
    count_of_trucks = len(truck_weights)
    while len(finished_trucks) < count_of_trucks:
        answer += 1
        # print(answer, "초 상황:" )
        if truck_weights:
            next_truck = Truck(truck_weights[0])
            # print("현재 다리의 무게:", weight_in_bridge)
            # print("대기 트럭의 무게:", next_truck.weight)
            # print("다음 트럭이 올라갈 수 있나요?", weight_in_bridge + next_truck.weight <= weight)
        else:
            next_truck = Truck(float("inf"))

        # 다리 위 모든 트랙이 1만큼 이동한다.
        for truck in trucks_in_bridge:
            truck.move()
        
        # print("현재 다리 위의 트럭:", trucks_in_bridge)
        # 가장 앞의 트럭이 도착했다면:
        if trucks_in_bridge and trucks_in_bridge[0].is_arrived(bridge_length):
            # 다리를 건너는 트럭에서 pop하고 다리를 지난 트럭에 append한다.
            truck = trucks_in_bridge.pop(0)
            finished_trucks.append(truck)
            weight_in_bridge -= truck.weight
            # print("트럭이 도착했습니다:", truck)
        

         # 현재 무게에 다음 트럭이 올라갈 수 있다면:
        if weight_in_bridge + next_truck.weight <= weight:
            # 대기트럭에서 pop하고 다리를 건너는 트럭에 append한다
            truck_weights.pop(0)
            trucks_in_bridge.append(next_truck)
            weight_in_bridge += next_truck.weight
            next_truck.move()

                
    return answer