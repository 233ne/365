import time

def focus_timer(minutes):
    seconds = minutes * 60
    end_time = time.time() + seconds

    print(f"Focus timer started for {minutes} minutes.")

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        print(f"Time remaining: {minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

    print("\nFocus timer finished.")

# 设置专注时长为 25 分钟
focus_timer(25)
