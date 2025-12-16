from game_utils import end_game, start_game

number, start_time = start_game()

print("GAME ĐOÁN SỐ (1–100)")
print("Bắt đầu lúc:", start_time.strftime("%d/%m/%Y - %H:%M:%S"))

while True:

    try:
        guess = int(input("🔢 Nhập số bạn đoán: "))
    except:
        print("Chỉ được nhập số")
        continue

    if guess < number:
        print("🔻 Thấp quá")
    elif guess > number:
        print("🔺 Cao quá")
    else:
        end_time, play_time = end_game(start_time)
        print("🎮 Chuẩn luôn!")
        print("⏲ Kết thúc lúc:", end_time.strftime("%d/%m/%Y - %H:%M:%S"))
        print("⏲ Thời gian chơi:", play_time)
        break