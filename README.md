#### Roll.no &nbsp; Name of Group members
1911019  -  Ritesh Jadav\
1911020 - Kritarth Jain\
1911057 - Saurav Shetty
#### Class : Ty-Computer Engineering
#### Course : CSS
#### Faculty : Dr.Deepak Sharma
#### College : K J Somaiya College Of Engineering
# CSS_IA1_Image_encryption_using_rubiks_cube_algorithm
## Research paper referred : https://www.hindawi.com/journals/jece/2012/173931/

## Functionalities implemented:
1. Generation and storage of random key as base64 strings.
2. Encryption of images using rubiks cube algorithm.
3. Decryption of the encrypted images.

## Improvements implemented:

The rubiks cube algorithm is defined on gray scale images but we have generalized it over 3 channels (R,G,B) to encrypt and decrypt RGB images.

## Algorithm Overview

Given an input image having the three R,G,B matrices of size `M X N`
Hyperparameters include 
`α` - used for vector creation
`ITER_MAX` - maximum number of times to carry out operations

#### A. Encyption
1. Create two vectors `Kr` and `Kc` with `|Kr|=M` & `|Kc|=N`. The values of these vectors are randomly picked from 0 to 2<sup>α </sup>-1
2. Repeat below steps `ITER_MAX` number of times

    i. **Rolling Rows:** 
        
      * The sum of all pixel values of every row of the image RGB matrices are calculated one by one. 
        
      * If the sum of a given row `rowNumber` is even, Roll the row to the right `Kr[rowNumber]` times 
        Otherwise roll to the left `Kr[rowNumber]` times.

    ii. **Rolling Columns:**
    
      * The sum of all pixel values of every column of the image RGB matrices are calculated one by one. 
        
      * If the sum of a given row `columnNumber` is even, roll the column up `Kc[columnNumber]` times.
        Otherwise roll the column down `Kc[columnNumber]` times.

    iii. **XORing Pixels:**
    
      * For every pixel(i,j), XOR the pixel with the below two values
        
         - Value #1 - `Kc[columnNumber]` if `i` is odd else 180 rotated bit version of `Kc[columnNumber]`
        
         - Value #2 - `Kr[rowNumber]` if `j` is even else 180 rotated bit version of `Kr[rowNumber]`


#### B. Decryption
  Given an encrypted image, vectors `Kr` and `Kc` & `ITER_MAX` , decryption can be done by following the reverse procedure - XORing pixels → Reverse direction Rolling Columns → Reverse direction Rolling Rows `ITER_MAX` number of times

## Prerequisites

- Python3 ( https://www.python.org/downloads/ )

- opencv - Run `pip install opencv-python`
## Execution
$ python3 image_encryption_rubiks_cube_algorithm.py\
Before Execution :\
![image](https://user-images.githubusercontent.com/63907547/154470122-f6e0c6af-8976-4acb-aac2-b97d7c0e67b8.png)

After Execution :\
![image](https://user-images.githubusercontent.com/63907547/154470015-66b67c05-7328-4ec7-9a45-402f93d17d2c.png)

Encrypted image is stored at `ENCRYPTED_IMAGE(original.png).jpeg`\
Decrypted image is stored at `DECRYPTED_IMAGE(original.png).jpeg`\
& key is stored at `key(original.png).txt `\
## Sample Output : 
![sample](https://user-images.githubusercontent.com/63907547/154469506-2edbbf53-f1ac-4366-a90c-a94fa9b3da64.jpg)



## Example -

Original Image : \
![image](https://user-images.githubusercontent.com/63907547/154424039-516714e7-a747-4081-8dcb-4cf3a92e9754.png)\
Encryted Image : \
![image](https://user-images.githubusercontent.com/63907547/154424209-2349de4a-4dfd-4f87-92fb-547b20b8769c.png)\
Decrypted Image :\
![image](https://user-images.githubusercontent.com/63907547/154424302-077656d0-9382-4241-a50e-bb10314e3c73.png)\
key.txt :\
![image](https://user-images.githubusercontent.com/63907547/154470441-6f6cb88f-07ad-4a11-96a3-da9cf3575a5b.png)







