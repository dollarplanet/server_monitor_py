import psutil
import time
from functools import reduce
import os
import requests

# Penampungan
cpu_percents: list[float] = []
memory_percents: list[float] = []

# Cek persentase setiap 1 detik
time.sleep(1)
cpu_percents.append(psutil.cpu_percent())
memory_percents.append(psutil.virtual_memory().percent)
time.sleep(1)
cpu_percents.append(psutil.cpu_percent())
memory_percents.append(psutil.virtual_memory().percent)
time.sleep(1)
cpu_percents.append(psutil.cpu_percent())
memory_percents.append(psutil.virtual_memory().percent)
time.sleep(1)
cpu_percents.append(psutil.cpu_percent())
memory_percents.append(psutil.virtual_memory().percent)
time.sleep(1)
cpu_percents.append(psutil.cpu_percent())
memory_percents.append(psutil.virtual_memory().percent)
time.sleep(1)
cpu_percents.append(psutil.cpu_percent())
memory_percents.append(psutil.virtual_memory().percent)
time.sleep(1)
cpu_percents.append(psutil.cpu_percent())
memory_percents.append(psutil.virtual_memory().percent)
time.sleep(1)
cpu_percents.append(psutil.cpu_percent())
memory_percents.append(psutil.virtual_memory().percent)

# Hitung rata - rata persentase
final_cpu_percent = round(reduce((lambda a, b: a + b), cpu_percents) / len(cpu_percents), 2)
final_memory_percent = round(reduce((lambda a, b: a + b), memory_percents) / len(memory_percents), 2)
final_disk_percent = psutil.disk_usage(os.environ.get("DISK_PATH")).percent

# Simpan ke database
try:
  requests.post(
    os.environ.get("API_URL") + "/server-usage",
    data = {
      "machine": os.environ.get("MACHINE_ID"),
      "cpu": final_cpu_percent,
      "memory": final_memory_percent,
      "disk": final_disk_percent
    },
    headers = {
      "machine": os.environ.get("MACHINE_ID"),
      "token": os.environ.get("TOKEN")
    }
  )
except Exception as e:
  print(e)
