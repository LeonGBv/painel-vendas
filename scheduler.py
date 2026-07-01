import schedule
import time
import subprocess

def rodar_job():
    print("Executando main.py...")
    subprocess.run(["python", "main.py"])

# agenda: todo dia 08:00
schedule.every().day.at("08:00").do(rodar_job)

# ou teste a cada 1 minuto:
# schedule.every(1).minutes.do(rodar_job)

print("Scheduler rodando...")

while True:
    schedule.run_pending()
    time.sleep(1)