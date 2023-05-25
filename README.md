# meta_mms
text to speech (in Hindi) using Meta's Massively Multilingual Speech (MMS) project

step by step instruction on how to make it work with PYCharm

step 1: 
> pip install soundfile 
This open source project works with Text-to-speech with The Massively Multilingual Speech (MMS) project. When you reach here, try and open "support_list.txt", massive list of all the languages that MMS supports. For example: hin for Hindi.

step 2:
> curl https://dl.fbaipublicfiles.com/mms/tts/hin.tar.gz --output hin.tar.gz 
notice, 'hin' for Hindi. You can replace 'hin' with 'pol' for Polish and likewise

step 3:
> mkdir -p data && tar -xzf hin.tar.gz -C data/   
make 'data' sub-directory and unzip the tarball you just downloaded above

step 4 
> git clone https://github.com/stillwrinkled/meta_mms.git
and open this as a project in PYCharm and run
