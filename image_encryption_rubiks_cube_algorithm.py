import cv2
import numpy as np
import os
import base64

def encryption(image,key_file="key.txt"):
    kr,kc,itr_max = load_key(image.shape[0],image.shape[1],key_file)
    for _ in range(itr_max):
        image = shift_rows(image,kr)
        image = shift_cols(image,kc)
        image = xor_rows_cols(image,kr,kc,len(kr),len(kc))
    return image

def rotate180(num,alpha=8):
    return int(format(num,f"0{alpha}b")[::-1],2)

def xor_rows_cols(image,kr,kc,m,n):
    for i in range(m):
        for j in range(n):
            if i%2==0:
                image[i,j,:] = np.bitwise_xor(image[i,j,:],rotate180(kc[j]))
            else:
                image[i,j,:] = np.bitwise_xor(image[i,j,:],kc[j])
            
            if j%2==0:
                image[i,j,:] = np.bitwise_xor(image[i,j,:],rotate180(kr[i]))
            else:
                image[i,j,:] = np.bitwise_xor(image[i,j,:],kr[i])
    return image

def shift_rows(image,kr,flag=1):
    for index,kr_i in enumerate(kr):
        image[index,:,0] = np.roll(image[index,:,0],flag*(1-2*(np.sum(image[index,:,0])%2))*kr_i)
        image[index,:,1] = np.roll(image[index,:,1],flag*(1-2*(np.sum(image[index,:,1])%2))*kr_i)
        image[index,:,2] = np.roll(image[index,:,2],flag*(1-2*(np.sum(image[index,:,2])%2))*kr_i)
    return image
    
def shift_cols(image,kc,flag=1):
    for index,kc_i in enumerate(kc):
        image[:,index,0] = np.roll(image[:,index,0],flag*(1-2*(np.sum(image[:,index,0])%2))*kc_i)
        image[:,index,1] = np.roll(image[:,index,1],flag*(1-2*(np.sum(image[:,index,1])%2))*kc_i)
        image[:,index,2] = np.roll(image[:,index,2],flag*(1-2*(np.sum(image[:,index,2])%2))*kc_i)
    return image

def decryption(image,key_file="key.txt"):
    kr,kc,itr_max = load_key(image.shape[0],image.shape[1],key_file)
    for _ in range(itr_max):
        image = xor_rows_cols(image,kr,kc,len(kr),len(kc))
        image = shift_cols(image,kc,-1)
        image = shift_rows(image,kr,-1)
    return image

def generate_random_key(m,n,itr=3,key_file="key.txt",alpha=8):
    kr = np.random.randint(0,2**alpha,size=m)
    kc = np.random.randint(0,2**alpha,size=n)
    key_string = ''.join([chr(i) for i in kr]) + ''.join([chr(i) for i in kc]) + str(itr)
    encoded_key = base64.b64encode(key_string.encode())
    with open(key_file, "wb") as binary_file:
        binary_file.write(encoded_key)
    return

def load_key(m,n,key_file="key.txt"):
    with open(key_file, 'r') as keyfile:
        data = keyfile.read()
        decoded_key = base64.b64decode(data).decode()
        kr = [ord(i) for i in decoded_key[:m]]
        kc = [ord(i) for i in decoded_key[m:m+n]]
        itr_max = int(decoded_key[m+n:])
    return kr,kc,itr_max

def show_image(image,title="",save=False):
    cv2.imshow(title,cv2.cvtColor(image,cv2.COLOR_RGB2BGR))
    if save:
        cv2.imwrite(f'{title}.jpeg',cv2.cvtColor(image,cv2.COLOR_RGB2BGR))


def input_image():
    file_name = input('Enter file name : ').strip()
    if os.path.exists(file_name):
        image = cv2.imread(file_name,cv2.IMREAD_COLOR)
        rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        show_image(rgb_image,"ORIGINAL IMAGE")
        return rgb_image
    else:
        print("ERROR : FILE DOESNT EXIST")
        quit()

def main():
    itr_max = 3
    image = input_image()
    generate_random_key(image.shape[0],image.shape[1],itr_max)
    encrypted_image = encryption(image)
    show_image(encrypted_image,"ENCRYPTED_IMAGE",save=True)
    decrypted_image = decryption(image)
    show_image(decrypted_image,"DECRYPTED_IMAGE",save=True)
    cv2.waitKey(0) 

main()



