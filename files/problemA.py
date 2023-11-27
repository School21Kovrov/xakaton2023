t1, t2 = map(int, input().split())
k = int(input())

hand_time = t1 * k
server_time = t2

if hand_time < server_time:
    print("hand")
elif hand_time==server_time:
    print("same")
else:
    print("server")
