import random
import threading
import time

def namegen():
    length = random.randint(7, 15) #set your min and max (min, max)
    eval = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
    "S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0",""


    return ''.join(random.choice(eval) for i in range(length))


def main():
    
    email_providers=["@gmail","@yahoo","@outlook","@mail","@gmail","@outlook","@yahoo","@alekdevs","@alek","@streammontero","@streammonteroday","@montero","@lilnasx"]
    domains = [".ru",".us",".ea",".club",".host",".en",".ny",".nj",".ma",".ca"]
    
    random_provider = random.choice(email_providers)
    random_domains = random.choice(domains)
    final_end = random_provider + random_domains
    
    final_email = namegen() + final_end


    print(final_email)

    f1 = open("./output/email.txt", "a+")
    f1.write(f"{final_email}\n")
    f1.close

threads=[]


for i in range(100000):
  t = threading.Thread(target = main)
  t.Daemon = True
  threads.append(t)

for i in range(100000):
  threads[i].start()
  time.sleep(0.2)

for i in range(100000):
  threads[i].join()
