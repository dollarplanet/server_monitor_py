import psutil
import time
from functools import reduce
from supabase import create_client, Client
import os

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
  url: str = os.environ.get("SUPABASE_URL")
  key: str = os.environ.get("SUPABASE_KEY")
  serverId: str = os.environ.get("SERVER_ID")
  supabase: Client = create_client(url, key)

  supabase.table("usage").insert({
    "serverId": serverId,
    "cpu": final_cpu_percent,
    "memory": final_memory_percent,
    "disk": final_disk_percent
  }).execute()
except:
  print("Error")
