## meta_mms
text to speech (in Hindi) using Meta's Massively Multilingual Speech (MMS) project

step by step instruction on how to make it work with PYCharm

step 1: 
```
pip install ttsmms
```
This open source project works for Text-to-speech with Meta's The Massively Multilingual Speech (MMS) project. When you reach here, try and open "support_list.txt", massive list of all the languages that MMS supports. For example: hin is for Hindi.
```
https://github.com/wannaphong/ttsmms/tree/main
```

step 2:
```
curl https://dl.fbaipublicfiles.com/mms/tts/hin.tar.gz --output hin.tar.gz 
```
Download the meta model. Also, notice 'hin' is for Hindi. You can replace 'hin' with 'pol' for Polish and likewise. Refer "support_list.txt" for exhaustive list

step 3:
```
mkdir -p data && tar -xzf hin.tar.gz -C data/   
```
make 'data' sub-directory and unzip the tarball you just downloaded above

step 4 
```
git clone https://github.com/stillwrinkled/meta_mms.git
```
and open this as a project in PYCharm and run the project
