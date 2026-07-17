import os
import random
from datetime import datetime, timedelta

# ================= НАСТРОЙКИ =================
REPO_PATH = "."                    # Папка с репозиторием
MIN_COMMITS = 10
MAX_COMMITS = 15
START_DATE = datetime(2024, 1, 1)  # С 1 января 2024
# ============================================

os.chdir(REPO_PATH)

def make_fake_commit(date):
    filename = "activity_log.md"
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"Activity: {date.strftime('%Y-%m-%d %H:%M:%S')} | commit #{random.randint(10000,99999)}\n")
    
    os.system(f"git add {filename}")
    commit_message = f"update: daily activity {date.strftime('%Y-%m-%d')}"
    os.system(f'git commit --date="{date.isoformat()}" -m "{commit_message}"')


print("🚀 Генерация коммитов с 1 января 2024 по сегодня...")
print(f"Коммитов в день: {MIN_COMMITS}-{MAX_COMMITS}\n")

current_date = START_DATE
today = datetime.now()
total_commits = 0
days_processed = 0

while current_date <= today:
    # Небольшая вероятность пропуска дня (чтобы выглядело естественнее)
    if random.random() < 0.07:  
        current_date += timedelta(days=1)
        continue
    
    commits_today = random.randint(MIN_COMMITS, MAX_COMMITS)
    
    for _ in range(commits_today):
        make_fake_commit(current_date)
        total_commits += 1
    
    days_processed += 1
    if current_date.day == 1 or current_date.day == 15:
        print(f"✅ {current_date.strftime('%Y-%m-%d')} — {commits_today} коммитов")

    current_date += timedelta(days=1)

print("\n🎉 Готово!")
print(f"Обработано дней: {days_processed}")
print(f"Всего создано коммитов: {total_commits:,}")
print("\nТеперь выполни:")
print("   git push -f origin main")