#### Roll.no &nbsp; Name of Group members
1911019  -  Ritesh Jadav\
1911020 - Kritarth Jain\
1911057 - Saurav Shetty
#### Class : Ty-Computer Engineering
#### Course : CSS
#### Faculty : Dr.Deepak Sharma
#### College : K J Somaiya College Of Engineering
# CSS_IA1_Image_encryption_using_rubiks_cube_algorithm
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
  Given an encrypted image, vectors `Kr` and `Kc` & `ITER_MAX` , decryption can be done by following the reverse procedure - XORing pixels → Rolling Columns → Rolling Rows `ITER_MAX` number of times

## Prerequisites

- Python3 ( https://www.python.org/downloads/ )

- opencv - Run `pip install opencv-python`
## Running 
$ python3 image_encryption_rubiks_cube_algorithm.py\
Before running :\
![image](https://user-images.githubusercontent.com/63907547/154422252-cd5785d5-c0ec-4306-b7d2-5c280785101f.png)\
After running :\
![image](https://user-images.githubusercontent.com/63907547/154423133-11f2b775-a219-43c0-afa3-d86dd1b62042.png)\
Encrypted image is stored at `ENCRYPTED_IMAGE.jpeg`\
Decrypted image is stored at `DECRYPTED_IMAGE.jpeg`\
& key is stored at `key.txt `

## Example -

Original Image : \
![image](https://user-images.githubusercontent.com/63907547/154424039-516714e7-a747-4081-8dcb-4cf3a92e9754.png)\
Encryted Image : \
![image](https://user-images.githubusercontent.com/63907547/154424209-2349de4a-4dfd-4f87-92fb-547b20b8769c.png)\
Decrypted Image :\
![image](https://user-images.githubusercontent.com/63907547/154424302-077656d0-9382-4241-a50e-bb10314e3c73.png)\
key.txt :\
![image](https://user-images.githubusercontent.com/63907547/154424748-11915b9a-57f4-4c9b-92d6-2af5d35acc96.png)






