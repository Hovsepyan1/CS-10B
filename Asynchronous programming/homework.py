# # Տրված է images/ թղթապանակը, որտեղ առկա են բարձր որակի նկարներ:
# # Օգտագործելով Pillow (PIL) գրադարանը, իրականացնել հետևյալ գործողությունները.
# # 1. Բացել նկարը:
# # 2. Կատարել Resize (800x800 չափսի):
# # 3. Պահպանել արդյունքը processed/ թղթապանակում:
# # Համեմատել կատարման ժամանակը (Performance Benchmarking):
# # ● Իրականացնել սովորական (sequential) տարբերակով:
# # ● Իրականացնել ProcessPoolExecutor.map()-ի միջոցով:
# # ● time մոդուլի օգնությամբ չափել և տպել, թե որքանով արագացավ պրոցեսը
# # զուգահեռացման դեպքում:

# import os
# import multiprocessing
# import time
# import concurrent.futures
# from PIL import Image

# images = [f"images/{img_name}" for img_name in os.listdir("images")]
# print(images)
# size = (800, 1000)
# def resize_image(image):
#     img = Image.open(image)
#     img.thumbnail(size)

#     img.save(f'processed/{os.path.basename(image)}')
#     print(f'{image} was processed...')


# os.makedirs("processed", exist_ok=True)
# process = []
# for i in range(len(images)):
#     p = multiprocessing.Process(target=resize_image, args=[images[i]])
#     p.start()
#     process.append(p)

# for p in process:
#     p.join()


# Առաջադրանք 4: Պրոցեսների Մոնիտորինգ (Logging & PIDs)
# Ստեղծել ծրագիր, որը կատարում է տարբեր տևողությամբ task-եր զուգահեռ և
# տրամադրում է մանրամասն տեղեկատվություն յուրաքանչյուրի մասին:
# Output-ի ձևաչափը պետք է լինի հետևյալը.
# ● Task [n] started (PID: 1234, Start Time: 14:30:05)
# ● Task [n] finished (End Time: 14:30:08, Result: Finished n)
# Հուշում: Օգտագործել os.getpid()՝ ընթացիկ պրոցեսի ID-ն ստանալու
# համար և datetime մոդուլը՝ ժամանակը ֆիքսելու համար:
# import os
# import multiprocessing
# import time 

# def worker(n):
#     print(f" Task [{n}] started (PID:{os.getpid()} Time:{time.time()})")
#     time.sleep(1)
#     print(f"Task [{n}] finished (End Time: {time.time()} Result: Finished {n})")

# myproc=[]
# for i in range(10):
#     p=multiprocessing.Process(target=worker,args=[i])
#     p.start()
#     myproc.append(p)

# for i in myproc:
#     i.join()





# Log file analyzer Տրված է մեծ .log ֆայլ (կամ ինքն է generate անում)։ 
# Գտնել բոլոր ERROR տողերը։ Sequential vs multiprocessing — ֆայլը բաժանել մասերի, 
# յուրաքանչյուր process մշակում է իր մասը, հետո արդյունքները merge են լինում։

import os
import multiprocessing
import concurrent.futures


with open("trace.log" , "r") as logs:
    content = logs.readlines()



def do_smth(content, start , end. queue):
    ls = []
    for i in content[start, end]:
        if 'ERROR' in i:
          ls.append(i)  
    queue.put(ls)

queue = multiprocessing.Queue()
processes = []
for i in range(0, len(content) , 2):
    p = multiprocessing.Process(target=do_smth, args=[content, i , i + 2, queue])
    p.start()
    processes.append(p)


    
